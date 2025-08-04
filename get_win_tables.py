#!/usr/bin/env python
#
# get_win_tables.py
#
# Get Windows Supported CPU lists from the Microsoft webspages since 2020.
# Extract the data and save in sub_directory win_cpu/ as both .json and .csv files.
#
# Objective:
# Collect the data in order to determine which CPU's were supported on Windows 10,
# but will not be supported on the latest Windows 11.
#
# Note:
# On loading csv or json file into a dictionary use underscore instead of hypen in
# the dictionary name. E.g. Don't use: windows-11-24h2-intel Use: windows_11_24h2_intel = {}
#
# Ian Stewart 2025-08-04 CC0

import os
import sys
import requests
from bs4 import BeautifulSoup
import json
import csv

sub_directory = "win_cpu"

def main():
    """
    Use link_list to get Microsoft Windows webpages with Supported CPU tables.
    Create a filename from the Microsoft URL link.
    Get the date of the document from the webpage.
    Append the date to the filename
    Get the desired data from the tables and place in a dictionary
    Save the dictionary to .json file.
    Save the dictionary data to .csv file.
    """
    print("\nExtracting Supported CPU data from Microsoft website...")

    #print(link_list)  # [['Windows 10 2004- AMD processors', 'https://learn.microsoft.com/...],...]

    for index in range(len(link_list)):
        title_str = link_list[index][0]
        link = link_list[index][1]
        print("\n" + title_str)
        #print(link)

        filename, directory = create_filename(link, title_str)
        #print(filename) #, directory)

        # Get document date and add it to filename
        date_str = get_date(link)
        #print(date_str)
        full_filename = filename + "-" + date_str
        #print("Sub-directory and File name: {}{}".format(directory, full_filename))

        # Get the dictionary of data
        data_dict = get_dict(link)
        #print(data_dict)

        # Write the dictionary out to .json and .csv files.
        dump_to_json(data_dict, directory, full_filename)
        dump_to_csv(data_dict, directory, full_filename)

    print("\nCompleted. json and csv files in subdirectory: {}".format(sub_directory))

def create_filename(link, title_str):
    # Create variables. Use the suffix of the link make a filename:
    # From: windows-11-24h2-supported-intel-processors"
    link_list = link.split("/")
    link_str = link_list.pop()
    #print(link_str)  # windows-11-24h2-supported-intel-processors
    lsl = link_str.split("-")
    #print(lsl)  # ['windows', '11', '24h2', 'supported', 'intel', 'processors']

    # One entry with no nnHn and no Intel/AMD: windows-11-supported-processors
    # Change Windows 11 to Windows 11 21h1.
    if len(lsl) < 6:
        if "intel" in lsl:
            filename = "{}-{}-21h1-intel".format(lsl[0], lsl[1],)

        else: # "amd" in lsl:
            filename = "{}-{}-21h1-amd".format(lsl[0], lsl[1],)

    # Normal entry:
    else:
        filename = "{}-{}-{}-{}".format(lsl[0], lsl[1], lsl[2], lsl[4])

    #print(filename)  # windows-11-24h2-intel

    # Create a sub-directory for the json and csv files. E.g. "win_cpu"
    #print("If required, creating the sub-directory to store json files: {}.".format(directory))
    directory = sub_directory
    os.makedirs(directory, exist_ok=True)
    directory = directory + "/"

    return filename, directory


def dump_to_json(data_dict, directory, filename):
    # Dump the data_dict as a .json file in the sub-directory
    with open(directory + filename + ".json", 'w') as fout:
        fout.write(json.dumps(data_dict, indent = 4))


def dump_to_csv(data_dict, directory, filename):
    # Dump the data_dict as a csv file. CSV expects a list of lists
    csv_list = []
    for key, value in data_dict.items():
        temp_list = []
        #print(key, value) # x7211E {'Manufacturer': 'Intel', 'Brand': 'Atom'}
        temp_list.append(key)
        for sub_key, sub_value in value.items():
            #print(sub_value)
            temp_list.append(sub_value)
        #print(temp_list)
        csv_list.append(temp_list)

    # Use csv to write list to sub-directory csv file
    with open(directory + filename + ".csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_list)


def get_date(link):
    """
    Get the date of the document from the webpage. HTML is like this:

    <ul class="metadata page-metadata" data-bi-name="page info" lang="en-us" dir="ltr">
        <li class="visibility-hidden-visual-diff">
    <local-time
        format="twoDigitNumeric"
            datetime="2024-03-01T11:55:00.000Z"
            data-article-date-source="calculated"
            class="is-invisible"
        >
            2024-03-01
    </local-time>
    """
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    for i in soup.find_all("ul", {"class": "metadata page-metadata"}):
        date_str = i.getText()
        date_str = date_str.strip()
    return date_str


def get_dict(link):
    """
    Get supported CPU's webpage from Microsoft.
    The returned html has a table with 3 or 4 columns in each row.
    Get the data from the relevant columns into a list.
    Build a dictionary from the list data like this:
    {'x7211E': {'Manufacturer': 'Intel', 'Brand': 'Atom'}, 'x7213E': {'Manufacturer': ...}}
    """
    data_dict = {}

    response = requests.get(link)
    #print(response.status_code)
    #print(response.content)
    soup = BeautifulSoup(response.content, 'html.parser')

    counter = 0
    for i in soup.find_all('tr'):
        counter +=1
        # Table Row <tr> has newline delimited Table Data <td>.
        tr_str = i.getText()

        # Remove Tradmarks, footnotes, etc. from Table Row string.
        tr_str = ("").join(tr_str.split("®"))
        tr_str = ("").join(tr_str.split("™"))
        tr_str = ("").join(tr_str.split("[1]"))
        tr_str = ("").join(tr_str.split("[2]"))

        # Make a list of Table Data. <td>
        td_list = tr_str.split("\n")

        # Cut down the td_list. 0 and then above 3, to get relevant table data <td>.
        td_list.pop(0)
        while len(td_list) > 3:
            td_list.pop()

        #print(counter, td_list)

        # Add tr_list data to dictionary with CPU model number as the key.
        data_dict[td_list[2]] = {"Manufacturer":td_list[0], "Brand":td_list[1],}

    # Take off 1 for the header row.
    print("Entries in dictionary:", len(data_dict)-1)
    return data_dict



# List of the titles and the links to the MS Supported CPU webpages...

# Note: The Win10 1909 and Win10 2004 releases are the same.
# ['Windows 10 1909 - AMD processors','https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-1909-supported-amd-processors'],
# ['Windows 10 1909 - Intel processors','https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-1909-supported-intel-processors'],

link_list = [
['Windows 10 2004- AMD processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-2004-supported-amd-processors'],
['Windows 10 2004- Intel processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-2004-supported-intel-processors'],

['Windows 10 20H2 - AMD processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-20h2-supported-amd-processors'],
['Windows 10 20H2 - Intel processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-20h2-supported-intel-processors'],

['Windows 10 21H1 - AMD processors',  'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-21h1-supported-amd-processors'],
['Windows 10 21H1 - Intel processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-21h1-supported-intel-processors'],

['Windows 10 21H2 - AMD processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-21h2-supported-amd-processors'],
['Windows 10 21H2 - Intel processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-21h2-supported-intel-processors'],

['Windows 10 22H2 - AMD processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-22h2-supported-amd-processors'],
['Windows 10 22H2 - Intel processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-10-22h2-supported-intel-processors'],

['Windows 11 21H1- AMD processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-supported-amd-processors'],
['Windows 11 21H1- Intel processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-supported-intel-processors'],

['Windows 11 22H2/23H2 - AMD processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-22h2-supported-amd-processors'],
['Windows 11 22H2/23H2 - Intel processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-22h2-supported-intel-processors'],

['Windows 11 24H2 - AMD processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-24h2-supported-amd-processors'],
['Windows 11 24H2 - Intel processors', 'https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-24h2-supported-intel-processors'],
]

if __name__=="__main__":

    main()

"""
Console output when running the program:

$ python3.12 get_win_tables.py

Extracting Supported CPU data from Microsoft website...

Windows 10 2004- AMD processors
Entries in dictionary: 348

Windows 10 2004- Intel processors
Entries in dictionary: 881

Windows 10 20H2 - AMD processors
Entries in dictionary: 348

Windows 10 20H2 - Intel processors
Entries in dictionary: 918

Windows 10 21H1 - AMD processors
Entries in dictionary: 348

Windows 10 21H1 - Intel processors
Entries in dictionary: 942

Windows 10 21H2 - AMD processors
Entries in dictionary: 377

Windows 10 21H2 - Intel processors
Entries in dictionary: 992

Windows 10 22H2 - AMD processors
Entries in dictionary: 460

Windows 10 22H2 - Intel processors
Entries in dictionary: 1022

Windows 11 21H1- AMD processors
Entries in dictionary: 283

Windows 11 21H1- Intel processors
Entries in dictionary: 903

Windows 11 22H2/23H2 - AMD processors
Entries in dictionary: 319

Windows 11 22H2/23H2 - Intel processors
Entries in dictionary: 909

Windows 11 24H2 - AMD processors
Entries in dictionary: 335

Windows 11 24H2 - Intel processors
Entries in dictionary: 781

Completed. json and csv files in subdirectory: win_cpu

Time taken: ~ 20 secs

$ ls win_cpu/ -1

windows-10-2004-amd-2021-11-10.csv
windows-10-2004-amd-2021-11-10.json
windows-10-2004-intel-2021-11-10.csv
windows-10-2004-intel-2021-11-10.json

windows-10-20h2-amd-2021-11-10.csv
windows-10-20h2-amd-2021-11-10.json
windows-10-20h2-intel-2024-02-26.csv
windows-10-20h2-intel-2024-02-26.json

windows-10-21h1-amd-2021-11-10.csv
windows-10-21h1-amd-2021-11-10.json
windows-10-21h1-intel-2022-05-18.csv
windows-10-21h1-intel-2022-05-18.json

windows-10-21h2-amd-2023-05-23.csv
windows-10-21h2-amd-2023-05-23.json
windows-10-21h2-intel-2024-02-26.csv
windows-10-21h2-intel-2024-02-26.json

windows-10-22h2-amd-2023-05-23.csv
windows-10-22h2-amd-2023-05-23.json
windows-10-22h2-intel-2023-05-23.csv
windows-10-22h2-intel-2023-05-23.json


windows-11-21h1-amd-2023-07-25.csv
windows-11-21h1-amd-2023-07-25.json
windows-11-21h1-intel-2024-03-01.csv
windows-11-21h1-intel-2024-03-01.json

windows-11-22h2-amd-2024-04-08.csv
windows-11-22h2-amd-2024-04-08.json
windows-11-22h2-intel-2023-11-30.csv
windows-11-22h2-intel-2023-11-30.json

windows-11-24h2-amd-2025-04-08.csv
windows-11-24h2-amd-2025-04-08.json
windows-11-24h2-intel-2025-02-28.csv
windows-11-24h2-intel-2025-02-28.json

=====

https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions

Windows 10 was: NT 10.0     Threshold   July 29, 2015       1507    10240   May 9, 2017
Windows 10 version 1511     Threshold 2 November 10, 2015   1511    10586   October 10, 2017
Windows 10 version 1607     Redstone 1  August 2, 2016      1607    14393   April 10, 2018
Windows 10 version 1703     Redstone 2  April 5, 2017       1703    15063   October 9, 2018
Windows 10 version 1709     Redstone 3  October 17, 2017    1709    16299   April 9, 2019
Windows 10 version 1803     Redstone 4  April 30, 2018      1803    17134   November 12, 2019
Windows 10 version 1809     Redstone 5  November 13, 2018   1809    17763   November 10, 2020
Windows 10 version 1903     19H1        May 21, 2019        1903    18362   December 8, 2020
Windows 10 version 1909     Vanadium    November 12, 2019   1909    18363   May 11, 2021

Win10 since 2000
Windows 10 version 2004     Vibranium   May 27, 2020        2004    19041   December 14, 2021
Windows 10 version 20H2                 October 20, 2020    20H2    19042   August 9, 2022
Windows 10 version 21H1                 May 18, 2021        21H1    19043   December 13, 2022
Windows 10 version 21H2                 November 16, 2021   21H2    19044   June 13, 2023
Windows 10 version 22H2                 October 18, 2022    22H2    19045   October 14, 2025

Win 11 since 2021
Windows 11                  Cobalt[g]   October 4, 2021     21H2            October 10, 2023
Windows 11 version 22H2     Nickel[i]   September 20, 2022  22H2    22621   October 8, 2024[h]
Windows 11 version 23H2                 October 31, 2023    23H2    22631   November 11, 2025[h]
Windows 11 version 24H2     Germanium   October 1, 2024     24H2    26100   October 13, 2026[h]

Summary as of Aug 2025:

Windows 10 first released in: 2015
Releases of Windows 10 before 2000: 9
Releases of Windows 10 since 2000: 5
Windows 10 End of Support: October 14, 2025
Windows 11 first released in: 2021
Releases of Windows 11: 4

=====

Windows Processor Requirements Lists
https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-24h2-supported-intel-processors

...Before 2000...
Windows 7 and earlier - AMD processors
Windows 7 and earlier - Intel processors
Windows 8.1 - AMD processors
Windows 8.1 - Intel processors
Windows 10 1511 - AMD processors
Windows 10 1511 - Intel processors
Windows 10 1607 - AMD processors
Windows 10 1607 - Intel processors
Windows 10 1703 - AMD processors
Windows 10 1703 - Intel processors
Windows 10 1709 - AMD processors
Windows 10 1709 - Intel processors
Windows 10 1709 - Qualcomm processors
Windows 10 1803 - AMD processors
Windows 10 1803 - Intel processors
Windows 10 1803 - Qualcomm processors
Windows 10 1809 - AMD processors
Windows 10 1809 - Intel processors
Windows 10 1809 - Qualcomm processors
Windows 10 1903 - AMD processors
Windows 10 1903 - Intel processors
Windows 10 1903 - Qualcomm processors
Windows 10 1909 - AMD processors
Windows 10 1909 - Intel processors
Windows 10 1909 - Qualcomm processors

...Since 2000...
Windows 10 2004- AMD processors
Windows 10 2004- Intel processors
Windows 10 2004 - Qualcomm processors
Windows 10 20H2 - AMD processors
Windows 10 20H2 - Intel processors
Windows 10 20H2 - Qualcomm processors
Windows 10 21H1 - AMD processors
Windows 10 21H1 - Intel processors
Windows 10 21H1 - Qualcomm processors
Windows 10 21H2 - AMD processors
Windows 10 21H2 - Intel processors
Windows 10 21H2 - Qualcomm processors
Windows 10 22H2 - AMD processors
Windows 10 22H2 - Intel processors
Windows 10 22H2 - Qualcomm processors

Windows 10 LTSB 1507 - AMD processors
Windows 10 LTSB 1507 - Intel processors
Windows 10 LTSB 1607 - AMD processors
Windows 10 LTSB 1607 - Intel processors
Windows 10 LTSB 1809 - AMD processors
Windows 10 LTSB 1809 - Intel processors
Windows 10 LTSB 2021- AMD processors
Windows 10 LTSB 2021- Intel processors

Windows 11 22H2/23H2 - AMD processors
Windows 11 22H2/23H2 - Intel processors
Windows 11 22H2/23H2 - Qualcomm processors
Windows 11 24H2 - AMD processors
Windows 11 24H2 - Intel processors
Windows 11 24H2 - Qualcomm processors
Windows 11 - AMD processors (21h1)
Windows 11 - Intel processors (21h1)
Windows 11 - Qualcomm processors (21h1)
"""
