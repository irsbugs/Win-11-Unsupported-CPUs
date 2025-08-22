# Win-11-Unsupported-CPUs

2025-08-04

For each release of Windows, Microsoft provides a list of the CPU's that are supported.

The latest Windows 11 release (24H2) provides a list of 781 Intel and 335 AMD CPU's that are *supported*. Refer to the [Intel](https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-24h2-supported-intel-processors) and [AMD](https://learn.microsoft.com/en-us/windows-hardware/design/minimum/supported/windows-11-24h2-supported-amd-processors) Windows 11 24H2 supported CPU lists.

Computers with CPU's that were *supported* in previous versions of Windows, may fail to upgrade to the latest version of Windows 11 if these computers use CPU's that are not included the latest Windows *supported* list. 

From the Microsoft *supported* lists it is possible to make lists of the CPU's that have gone *unsupported*. Since 2015 there were 12 releases of Windows 10 and two releases of Windows 11 that preceed the latest Windows 11 24H2. The totals of CPU models in these previous lists that are no longer supported by Windows 11 24H3 are:

* 673 Intel
* 236 AMD

The *used computer* market should be boosted with computers using *unsupported* CPU's being discarded when Windows Users realise their computer hardware will no longer run the latest version of Windows 11. 

Most of these discarded computers will be suitable for running the latest Linux distros.

From all the Windows 10 and 11 *supported* lists, generated lists can be made of the CPU's that have gone *unsupported*. The following are the lists of *unsupported* CPU's. It is hoped that using these lists may help with selecting the better performance computers from those available in the *used computer* market. 




Summary as of Aug 2025:
```
Windows 10 first released in:       2015
Releases of Windows 10 before 2000: 9
Releases of Windows 10 since 2000:  5
Windows 10 End of Support:          October 14, 2025
Windows 11 first released in:       2021
Releases of Windows 11:             3
```

The *Supported CPU* data from previous releases of Windows may be compared with the data in the latest Windows 11 release. From this comparision a list of CPU's deemed *unsupported* in Windows 11 may be generated.

Using this *Unsupported CPU* list the specification of CPU's may be researched. When reviewing computers available in the *used computer* market, then this information may be helpful in selecting the best performance computer to obtain for running Linux.

Many of the *supported CPU's* on releases prior to 2000 will not have very good performance specifications. Thus, only the CPU's that have become *unsupported* since 2000 are determined.

The python program: [get_win_tables.py](./get_win_tables.py) was used to obtain the *supported* CPU lists from Microsoft's website and store them in a sub-directory as .csv and .json files.

The python program: [get_win_unsupported.py](./get_win_unsupported.py) was used to generate the list of all CPU's since 2000, that are now not supported on the latest Windows 11 release.

The lists of the *unsupported* CPU's: 

* [**Intel CPU's**](./unsupported_cpu_intel.md)

* [**AMD CPU's**](unsupported_cpu_amd.md)


Summary of Releases:

Looking at the first release of Windows 10 in 2015.
Windows 10 1511 listed 398 supported CPU's. (Manufacturing date must be prior to Nov 2015)
All 398 CPU's remained supported for the 10 x Windows releases up to and including Windows 10 21H2.
At this point they started to be removed from the supported lists.
298 CPU's remained supported in release 10 22H2
76 CPU's remained supported in release 11 21H1
76 CPU's remained supported in release 11 22H2
0 CPU's remained supported in release 11 24H2
i.e. None of these CPU's are supported in the latest Windows 11 24h2

Windows 10 1709 listed 521 supported CPU's. Of these CPU's 112 are supported in Windows 11 24h2

        398
        398
        398
        521
        573
        816
        881
        881
        881
        918
        942
        992
        1022
        903
        909
        781


```
windows_10_1511_intel CPU's contained in windows_10_1607_intel totals: 398 Total: 398
windows_10_1511_intel CPU's contained in windows_10_1703_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_1709_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_1803_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_1809_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_1903_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_1909_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_2004_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_20h2_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_21h1_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_21h2_intel totals: 398
windows_10_1511_intel CPU's contained in windows_10_22h2_intel totals: 298
windows_10_1511_intel CPU's contained in windows_11_21h1_intel totals:  76
windows_10_1511_intel CPU's contained in windows_11_22h2_intel totals:  76
windows_10_1511_intel CPU's contained in windows_11_24h2_intel totals:   0

windows_10_1607_intel CPU's contained in windows_10_1703_intel totals: 398 Total: 398
windows_10_1607_intel CPU's contained in windows_10_1709_intel totals: 398
windows_10_1607_intel CPU's contained in windows_10_1803_intel totals: 398
windows_10_1607_intel CPU's contained in windows_10_1809_intel totals: 398
windows_10_1607_intel CPU's contained in windows_10_1903_intel totals: 398
windows_10_1607_intel CPU's contained in windows_10_1909_intel totals: 398
windows_10_1607_intel CPU's contained in windows_10_2004_intel totals: 398
windows_10_1607_intel CPU's contained in windows_10_20h2_intel totals: 398
windows_10_1607_intel CPU's contained in windows_10_21h1_intel totals: 398
windows_10_1607_intel CPU's contained in windows_10_21h2_intel totals: 398
windows_10_1607_intel CPU's contained in windows_10_22h2_intel totals: 298
windows_10_1607_intel CPU's contained in windows_11_21h1_intel totals:  76
windows_10_1607_intel CPU's contained in windows_11_22h2_intel totals:  76
windows_10_1607_intel CPU's contained in windows_11_24h2_intel totals:   0

windows_10_1703_intel CPU's contained in windows_10_1709_intel totals: 398 Total: 398
windows_10_1703_intel CPU's contained in windows_10_1803_intel totals: 398
windows_10_1703_intel CPU's contained in windows_10_1809_intel totals: 398
windows_10_1703_intel CPU's contained in windows_10_1903_intel totals: 398
windows_10_1703_intel CPU's contained in windows_10_1909_intel totals: 398
windows_10_1703_intel CPU's contained in windows_10_2004_intel totals: 398
windows_10_1703_intel CPU's contained in windows_10_20h2_intel totals: 398
windows_10_1703_intel CPU's contained in windows_10_21h1_intel totals: 398
windows_10_1703_intel CPU's contained in windows_10_21h2_intel totals: 398
windows_10_1703_intel CPU's contained in windows_10_22h2_intel totals: 298
windows_10_1703_intel CPU's contained in windows_11_21h1_intel totals:  76
windows_10_1703_intel CPU's contained in windows_11_22h2_intel totals:  76
windows_10_1703_intel CPU's contained in windows_11_24h2_intel totals:   0

windows_10_1709_intel CPU's contained in windows_10_1803_intel totals: 521 Total: 521
windows_10_1709_intel CPU's contained in windows_10_1809_intel totals: 521
windows_10_1709_intel CPU's contained in windows_10_1903_intel totals: 521
windows_10_1709_intel CPU's contained in windows_10_1909_intel totals: 521
windows_10_1709_intel CPU's contained in windows_10_2004_intel totals: 521
windows_10_1709_intel CPU's contained in windows_10_20h2_intel totals: 521
windows_10_1709_intel CPU's contained in windows_10_21h1_intel totals: 521
windows_10_1709_intel CPU's contained in windows_10_21h2_intel totals: 518
windows_10_1709_intel CPU's contained in windows_10_22h2_intel totals: 417
windows_10_1709_intel CPU's contained in windows_11_21h1_intel totals: 196
windows_10_1709_intel CPU's contained in windows_11_22h2_intel totals: 196
windows_10_1709_intel CPU's contained in windows_11_24h2_intel totals: 112

windows_10_1803_intel CPU's contained in windows_10_1809_intel totals: 573 Total: 573
windows_10_1803_intel CPU's contained in windows_10_1903_intel totals: 573
windows_10_1803_intel CPU's contained in windows_10_1909_intel totals: 573
windows_10_1803_intel CPU's contained in windows_10_2004_intel totals: 573
windows_10_1803_intel CPU's contained in windows_10_20h2_intel totals: 573
windows_10_1803_intel CPU's contained in windows_10_21h1_intel totals: 573
windows_10_1803_intel CPU's contained in windows_10_21h2_intel totals: 570
windows_10_1803_intel CPU's contained in windows_10_22h2_intel totals: 469
windows_10_1803_intel CPU's contained in windows_11_21h1_intel totals: 248
windows_10_1803_intel CPU's contained in windows_11_22h2_intel totals: 248
windows_10_1803_intel CPU's contained in windows_11_24h2_intel totals: 162

windows_10_1809_intel CPU's contained in windows_10_1903_intel totals: 816 Total: 816
windows_10_1809_intel CPU's contained in windows_10_1909_intel totals: 816
windows_10_1809_intel CPU's contained in windows_10_2004_intel totals: 816
windows_10_1809_intel CPU's contained in windows_10_20h2_intel totals: 816
windows_10_1809_intel CPU's contained in windows_10_21h1_intel totals: 816
windows_10_1809_intel CPU's contained in windows_10_21h2_intel totals: 809
windows_10_1809_intel CPU's contained in windows_10_22h2_intel totals: 708
windows_10_1809_intel CPU's contained in windows_11_21h1_intel totals: 485
windows_10_1809_intel CPU's contained in windows_11_22h2_intel totals: 485
windows_10_1809_intel CPU's contained in windows_11_24h2_intel totals: 300

windows_10_1903_intel CPU's contained in windows_10_1909_intel totals: 881 Total: 881
windows_10_1903_intel CPU's contained in windows_10_2004_intel totals: 881
windows_10_1903_intel CPU's contained in windows_10_20h2_intel totals: 881
windows_10_1903_intel CPU's contained in windows_10_21h1_intel totals: 881
windows_10_1903_intel CPU's contained in windows_10_21h2_intel totals: 874
windows_10_1903_intel CPU's contained in windows_10_22h2_intel totals: 773
windows_10_1903_intel CPU's contained in windows_11_21h1_intel totals: 548
windows_10_1903_intel CPU's contained in windows_11_22h2_intel totals: 548
windows_10_1903_intel CPU's contained in windows_11_24h2_intel totals: 348

windows_10_1909_intel CPU's contained in windows_10_2004_intel totals: 881 Total: 881
windows_10_1909_intel CPU's contained in windows_10_20h2_intel totals: 881
windows_10_1909_intel CPU's contained in windows_10_21h1_intel totals: 881
windows_10_1909_intel CPU's contained in windows_10_21h2_intel totals: 874
windows_10_1909_intel CPU's contained in windows_10_22h2_intel totals: 773
windows_10_1909_intel CPU's contained in windows_11_21h1_intel totals: 548
windows_10_1909_intel CPU's contained in windows_11_22h2_intel totals: 548
windows_10_1909_intel CPU's contained in windows_11_24h2_intel totals: 348

windows_10_2004_intel CPU's contained in windows_10_20h2_intel totals: 881 Total: 881
windows_10_2004_intel CPU's contained in windows_10_21h1_intel totals: 881
windows_10_2004_intel CPU's contained in windows_10_21h2_intel totals: 874
windows_10_2004_intel CPU's contained in windows_10_22h2_intel totals: 773
windows_10_2004_intel CPU's contained in windows_11_21h1_intel totals: 548
windows_10_2004_intel CPU's contained in windows_11_22h2_intel totals: 548
windows_10_2004_intel CPU's contained in windows_11_24h2_intel totals: 348

windows_10_20h2_intel CPU's contained in windows_10_21h1_intel totals: 918 Total: 918
windows_10_20h2_intel CPU's contained in windows_10_21h2_intel totals: 911
windows_10_20h2_intel CPU's contained in windows_10_22h2_intel totals: 773
windows_10_20h2_intel CPU's contained in windows_11_21h1_intel totals: 585
windows_10_20h2_intel CPU's contained in windows_11_22h2_intel totals: 570
windows_10_20h2_intel CPU's contained in windows_11_24h2_intel totals: 348

windows_10_21h1_intel CPU's contained in windows_10_21h2_intel totals: 928 Total: 942
windows_10_21h1_intel CPU's contained in windows_10_22h2_intel totals: 790
windows_10_21h1_intel CPU's contained in windows_11_21h1_intel totals: 585
windows_10_21h1_intel CPU's contained in windows_11_22h2_intel totals: 570
windows_10_21h1_intel CPU's contained in windows_11_24h2_intel totals: 348

windows_10_21h2_intel CPU's contained in windows_10_22h2_intel totals: 854 Total: 992
windows_10_21h2_intel CPU's contained in windows_11_21h1_intel totals: 649
windows_10_21h2_intel CPU's contained in windows_11_22h2_intel totals: 634
windows_10_21h2_intel CPU's contained in windows_11_24h2_intel totals: 401

windows_10_22h2_intel CPU's contained in windows_11_21h1_intel totals: 769 Total: 1022
windows_10_22h2_intel CPU's contained in windows_11_22h2_intel totals: 769
windows_10_22h2_intel CPU's contained in windows_11_24h2_intel totals: 566

windows_11_21h1_intel CPU's contained in windows_11_22h2_intel totals: 888 Total: 903
windows_11_21h1_intel CPU's contained in windows_11_24h2_intel totals: 604

windows_11_22h2_intel CPU's contained in windows_11_24h2_intel totals: 607 Total: 909


Total Supported in windows_10_1511_intel: 398.    0 in Latest release windows_11_24h2_intel
Total Supported in windows_10_1607_intel: 398.    0 in Latest release windows_11_24h2_intel
Total Supported in windows_10_1703_intel: 398.    0 in Latest release windows_11_24h2_intel
Total Supported in windows_10_1709_intel: 521.  112 in Latest release windows_11_24h2_intel
Total Supported in windows_10_1803_intel: 573.  162 in Latest release windows_11_24h2_intel
Total Supported in windows_10_1809_intel: 816.  300 in Latest release windows_11_24h2_intel
Total Supported in windows_10_1903_intel: 881.  348 in Latest release windows_11_24h2_intel
Total Supported in windows_10_1909_intel: 881.  348 in Latest release windows_11_24h2_intel
Total Supported in windows_10_2004_intel: 881.  348 in Latest release windows_11_24h2_intel
Total Supported in windows_10_20h2_intel: 918.  348 in Latest release windows_11_24h2_intel
Total Supported in windows_10_21h1_intel: 942.  348 in Latest release windows_11_24h2_intel
Total Supported in windows_10_21h2_intel: 992.  401 in Latest release windows_11_24h2_intel
Total Supported in windows_10_22h2_intel:1022.  566 in Latest release windows_11_24h2_intel
Total Supported in windows_11_21h1_intel: 903.  604 in Latest release windows_11_24h2_intel
Total Supported in windows_11_22h2_intel: 909.  607 in Latest release windows_11_24h2_intel
```
