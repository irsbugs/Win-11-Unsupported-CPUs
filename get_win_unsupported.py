#!/usr/bin/env python
#
# get_win_unsupported.py
#
# Get the .json files of the Windows versions supported CPU's
# Compare with supported CPU's in most recent release of Win 11
# Generate a list of CPU hardware no longer supported in the last 5 years.
#
# Ian Stewart 2025-08-05 CC0

import os
import sys
import json
import glob

sub_directory  = "win_cpu"

def main():
    """
    Get intel and amd lists of .json files from sub-directory.
    Create titles from the filenames. Not sure what for. Could be handy?
    Load files into a list/array of dictionaries.
    Last in dictionary in list is the most recent Windows release of supported CPU's.
    Extract the key/CPU model to an array of lists
    Compare the lists and build a master list of unsupported CPU's.
    Copy master lists to master dictionaries
    Dump master dictionary to .json file.
    Open master .json file and dump dictionary key to console
    """
    print("\nCreate a dictionary of CPU's not supported in the latest Windows release.")

    json_intel_file_list = get_json_intel_file_list()
    #print(json_intel_file_list)
    json_intel_title_list = get_json_title_list(json_intel_file_list)
    #print(json_intel_title_list)

    json_amd_file_list = get_json_amd_file_list()
    #print(json_amd_file_list)
    json_amd_title_list = get_json_title_list(json_amd_file_list)
    #print(json_amd_title_list)

    # Intel. Load the json files into and array of dictionaries
    dict_array_intel = get_array_of_dictionaries(json_intel_file_list, json_intel_title_list)
    # AMD
    dict_array_amd = get_array_of_dictionaries(json_amd_file_list, json_amd_title_list)

    # Intel. Make an array of the supported CPU model numbers
    cpu_list_array_intel = make_cpu_list_array(dict_array_intel)
    # AMD
    cpu_list_array_amd = make_cpu_list_array(dict_array_amd)

    # Intel. Add unsupported CPU's to a master list.
    cpu_unsupported_intel_list = cpus_unsupported(cpu_list_array_intel, json_intel_title_list)
    print("\nTotal Unsupported Intel CPU's:    {:>4}".format(len(cpu_unsupported_intel_list)))
    # AMD
    cpu_unsupported_amd_list = cpus_unsupported(cpu_list_array_amd, json_amd_title_list)
    print("\nTotal Unsupported AMD CPU's:      {:>4}".format(len(cpu_unsupported_amd_list)))

    # Intel. Convert list to dict and save master as json file.
    dump_master_dict_intel_to_json(cpu_unsupported_intel_list)
    # AMD.
    dump_master_dict_amd_to_json(cpu_unsupported_amd_list)

    # Intel Load unsupported CPU master file and dump to console
    print("\nIntel CPU's not supported by latest Windows: {}".format(len(cpu_unsupported_intel_list)))
    with open("master_unsupported_intel.json") as fin:
        temp_dict = json.load(fin)
        for key, value in temp_dict.items():
            print(key)
            pass

    # AMD Load unsupported CPU master file and dump to console
    print("\nAMD CPU's not supported by latest Windows: {}".format(len(cpu_unsupported_amd_list)))
    with open("master_unsupported_amd.json") as fin:
        temp_dict = json.load(fin)
        for key, value in temp_dict.items():
            print(key)
            pass


def dump_master_dict_intel_to_json(cpu_unsupported_intel_list):
    """
    Convert unsupported Intel list to dictionary
    Write the dictionary out to .json file.
    """
    master_unsupported_intel_dict = {}
    for item in cpu_unsupported_intel_list:
        master_unsupported_intel_dict[item] = {"Manufacturer": "Intel"}
    # Dump the data_dict as a .json file in the sub-directory
    with open("master_unsupported_intel.json", 'w') as fout:
        fout.write(json.dumps(master_unsupported_intel_dict, indent = 4))


def dump_master_dict_amd_to_json(cpu_unsupported_amd_list, ):
    """
    Convert unsupported AMD list to dictionary
    Write the dictionary out to .json file.
    """
    master_unsupported_amd_dict = {}
    for item in cpu_unsupported_amd_list:
        master_unsupported_amd_dict[item] = {"Manufacturer": "AMD"}
    # Dump the data_dict as a .json file in the sub-directory
    with open("master_unsupported_amd.json", 'w') as fout:
        fout.write(json.dumps(master_unsupported_amd_dict, indent = 4))


def cpus_unsupported(cpu_list_array, cpu_title_list):
    """
    In the cpu_list_array the last item in the list is the latest Win 11 release.
    The CPU's in preceeding releases are checked to see if they are in the most recent release.
    If the CPU's are not supported they are added to the master_unsupported_list
    """
    master_unsupported_cpu_list = []
    diff_now = 0
    diff_prev = 0
    total_added = 0
    for index in range(len(cpu_list_array)):
        temp_list = []

        print("\n{}: {}".format(cpu_title_list[index], index))
        print("Number of CPU's in list:          {:>4}".format(len(cpu_list_array[index])))

        for item in cpu_list_array[index]:
            if item not in cpu_list_array[len(cpu_list_array)-1]:
                temp_list.append(item)
        print("Number of unsupported CPU's:      {:>4}".format(len(temp_list)))

        # From the temp_list, add the CPU's to the master_list, if not already in master_list
        for item in temp_list:
            if item not in master_unsupported_cpu_list:
                master_unsupported_cpu_list.append(item)
        print("Master list unsupported CPU's:    {:>4}".format(len(master_unsupported_cpu_list)))

        # Calculate how many unsupported CPU's added to the Master list.
        diff_now = len(master_unsupported_cpu_list)
        total_added = diff_now - diff_prev
        print("Total CPU's added to Master list: {:>4}".format(total_added))
        diff_prev = diff_now

    return sorted(master_unsupported_cpu_list)


def make_cpu_list_array(dict_array):
    """
    From the array of dictionaries, use the keys to make an array list of the CPU models.
    """
    cpu_list_array = []
    for a_dict in dict_array:
        temp_list = []
        for key, value in a_dict.items():
            temp_list.append(key)
        cpu_list_array.append(temp_list)
    return cpu_list_array


def get_array_of_dictionaries(json_file_list, json_title_list):
    """
    Load the intel or amd json files into an array/list of dictionaries
    """
    dict_array = []
    print("\nTotal of CPU models in each dictionary...")
    for index, filename in enumerate(json_file_list):
        with open(filename) as fin:
            temp_dict = json.load(fin)
            dict_array.append(temp_dict)
            print("{}: {:>4}".format(json_title_list[index], len(temp_dict)-1 ))
    print("Total dictionaries:", len(dict_array))
    return dict_array


def get_json_intel_file_list():
    """
    Use glob to search for the intel json files in sub directory.
    Needs to be sorted to ensure the last entry is the most recent Win release.
    """
    json_intel_file_list = sorted(glob.glob(sub_directory + "/*intel*.json"))
    return json_intel_file_list

def get_json_amd_file_list():
    json_amd_list = sorted(glob.glob(sub_directory + "/*amd*.json"))
    return json_amd_list

def get_json_title_list(json_file_list):
    """
    From the filename construct a title using underscores instead of hyphens. E.g.
    From: win_cpu/windows-11-24h2-intel-2025-02-28.json
    Get:  windows_11_24h2_intel
    """
    json_title_list = []
    for file in json_file_list:
        # Remove sub-directory
        temp_str = file.split("/").pop()
        tl = temp_str.split("-")
        json_title_list.append("{}_{}_{}_{}".format(tl[0], tl[1], tl[2], tl[3]))
    for index, name in enumerate(json_title_list):
        #print(name, ":", json_intel_file_list_file_list[index])
        pass
    return json_title_list


if __name__=="__main__":

    main()

"""
Console output:

$ python3.12 get_win_unsupported.py

Create a dictionary of CPU's not supported in the latest Windows release.

Total of CPU models in each dictionary...
windows_10_2004_intel:  881
windows_10_20h2_intel:  918
windows_10_21h1_intel:  942
windows_10_21h2_intel:  992
windows_10_22h2_intel: 1022
windows_11_21h1_intel:  903
windows_11_22h2_intel:  909
windows_11_24h2_intel:  781
Total dictionaries: 8

Total of CPU models in each dictionary...
windows_10_2004_amd:  348
windows_10_20h2_amd:  348
windows_10_21h1_amd:  348
windows_10_21h2_amd:  377
windows_10_22h2_amd:  460
windows_11_21h1_amd:  283
windows_11_22h2_amd:  319
windows_11_24h2_amd:  335
Total dictionaries: 8

windows_10_2004_intel: 0
Number of CPU's in list:           882
Number of unsupported CPU's:       533
Master list unsupported CPU's:     533
Total CPU's added to Master list:  533

windows_10_20h2_intel: 1
Number of CPU's in list:           919
Number of unsupported CPU's:       570
Master list unsupported CPU's:     570
Total CPU's added to Master list:   37

windows_10_21h1_intel: 2
Number of CPU's in list:           943
Number of unsupported CPU's:       594
Master list unsupported CPU's:     594
Total CPU's added to Master list:   24

windows_10_21h2_intel: 3
Number of CPU's in list:           993
Number of unsupported CPU's:       591
Master list unsupported CPU's:     605
Total CPU's added to Master list:   11

windows_10_22h2_intel: 4
Number of CPU's in list:          1023
Number of unsupported CPU's:       456
Master list unsupported CPU's:     607
Total CPU's added to Master list:    2

windows_11_21h1_intel: 5
Number of CPU's in list:           904
Number of unsupported CPU's:       299
Master list unsupported CPU's:     655
Total CPU's added to Master list:   48

windows_11_22h2_intel: 6
Number of CPU's in list:           910
Number of unsupported CPU's:       302
Master list unsupported CPU's:     673
Total CPU's added to Master list:   18

windows_11_24h2_intel: 7
Number of CPU's in list:           782
Number of unsupported CPU's:         0
Master list unsupported CPU's:     673
Total CPU's added to Master list:    0

Total Unsupported Intel CPU's:     673

windows_10_2004_amd: 0
Number of CPU's in list:           349
Number of unsupported CPU's:       230
Master list unsupported CPU's:     230
Total CPU's added to Master list:  230

windows_10_20h2_amd: 1
Number of CPU's in list:           349
Number of unsupported CPU's:       230
Master list unsupported CPU's:     230
Total CPU's added to Master list:    0

windows_10_21h1_amd: 2
Number of CPU's in list:           349
Number of unsupported CPU's:       230
Master list unsupported CPU's:     230
Total CPU's added to Master list:    0

windows_10_21h2_amd: 3
Number of CPU's in list:           378
Number of unsupported CPU's:       214
Master list unsupported CPU's:     230
Total CPU's added to Master list:    0

windows_10_22h2_amd: 4
Number of CPU's in list:           461
Number of unsupported CPU's:       220
Master list unsupported CPU's:     236
Total CPU's added to Master list:    6

windows_11_21h1_amd: 5
Number of CPU's in list:           284
Number of unsupported CPU's:         0
Master list unsupported CPU's:     236
Total CPU's added to Master list:    0

windows_11_22h2_amd: 6
Number of CPU's in list:           320
Number of unsupported CPU's:         0
Master list unsupported CPU's:     236
Total CPU's added to Master list:    0

windows_11_24h2_amd: 7
Number of CPU's in list:           336
Number of unsupported CPU's:         0
Master list unsupported CPU's:     236
Total CPU's added to Master list:    0

Total Unsupported AMD CPU's:       236
"""
