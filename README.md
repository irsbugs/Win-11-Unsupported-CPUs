# Win-11-Unsupported-CPUs

2025-08-04

For each release of Windows, Microsoft provides a list of the CPU's that are supported.

The latest Windows 11 release (24H2) supports a total of 781 Intel CPU's and 335 AMD CPU's.

The Windows upgrade process will not upgrade Windows 10 or Windows 11 machines that use older/unsuppported CPU's.

Many of these older/unsupported CPU's will become available in the *used computer market*. Most of them will be suitable for running the latest Linux distros.

Summary as of Aug 2025:
```
Windows 10 first released in:       2015
Releases of Windows 10 before 2000: 9
Releases of Windows 10 since 2000:  5
Windows 10 End of Support:          October 14, 2025
Windows 11 first released in:       2021
Releases of Windows 11:             4
```

The *Supported CPU* data from previous releases of Windows may be compared with the data in the latest Windows 11 release. From this comparision a list of CPU's deemed *Unsupported* in Windows 11 may be generated.

Using this *Unsupported CPU* the specification of CPU's may be obtained. When reviewing computer products available in the *used computer* market, then this information may be helpful in selecting the best performance computer to get for running Linux.

Many of the *supported CPU's* on releases prior to 2000 will not have good performance specifications. Thus, only the CPU's that have gone *unsuppoprted* since 2000 are determined.

The python program: [**get_win_table.py**](/get_win_table.py) will obtain the *supported* CPU lists from Microsoft's website and store them in a sub-directory as .csv and .json files.

The python program: **get_win_unsupported.py** will generate the list of all CPU's since 2000, that are now not supported on the latest Windows 11 release.

