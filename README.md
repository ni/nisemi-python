# About
NI Semiconductor Device Control Python API Support provides Python APIs and examples to develop python test programs and communicate with a device using the setup configuration exported from the Semiconductor Device Control Add-On for InstrumentStudio.

This library is dependent on Semiconductor Device Control addon for InstrumentStudio.


# Semiconductor Device Control Python API Status

** Setup and cleanup functions  **  
1. Instantiate - using IS configuration file  
2. Destroy  
3. Start  
4. Stop  
** Hardware Read & Write to Register and Field  **  
5. Write Register by name (Device)  
6. Read Register by name (Device)  
7. Write Register by Address (Device)  
8. Read Register by Address (Device)  
9. Write Field by Name (Device)  
10. Read Field by Name (Device)  
11. Write Field by value definition (Device)  
** Hardware multiple Read & Write to Register and Field  **  
12. Write Multiple Register by Name (Device)  
13. Read Multiple Register by name (Device)  
14. Write Multiple Register by Address (Device)  
15. Read Multiple Register by Address (Device)  
16. Write Multiple Fields by Name (Device)  
18. Read Multiple Field by Name (Device)  
** Cache Read & Write to Register and Field  **  
19. Write Register by name (Cache)  
20. Read Register by name (Cache)  
21. Write Register by Address (Cache)  
22. Read Register by Address (Cache)  
23. Write Field by Name (Cache)  
24. Read Field by Name (Cache)  
25. Write Field by value definition (cache)  
26. Write from Cache to Device  
27. Clear Cache  
** Cache multiple Read & Write to Register and Field  **  
28. Write Multiple Register by Name (Cache)  
29. Read Multiple Register by name (Cache)  
30. Write Multiple Register by Address (Cache)  
31. Read Multiple Register by Address (Cache)  
32. Write Multiple Fields by Name (Cache)  
33. Read Multiple Field by Name (Cache)  
** DIO operation  **  
34. Write Pin State  
35. Read Pin State  
** Utils **
36. Get Dynamic Protocol Settings
37. Update Dynamic Protocol Settings
38. Get Instrument Session


# Installation

** Dependency Installation **  
1. Semiconductor Device Control addon for InstrumentStudio 2023 - `ni download <update the download link>`_.  
2. pythonnet 2.5.1 - [pypi download](https://pypi.org/project/pythonnet/#description)  

** Work with github source code **  
3. Clone the github repository - '[semiconductor device control python api github repo]<link>'_ 
4. Use the APIs from 'nisdc' folder in your program  

** Work with Semiconductor Device Control Python API from pypi **  
3. Go to Semiconductor Device Contro Python API location in `pypi <ni pypi download link>`_.  
4. Install the package and use the api libraries in your program  

# Usage

Reference example is available in the 'github repository <link>'_ for developers (under examples folder), to refer on how to use the python APIs in the test program.

# Documentation

Documentation is available from ni resource website - [here](https://www.ni.com/documentation/en/semiconductor-device-control/latest/manual/manual-overview/).

# Contributing

We welcome contributions! You can clone the project repository, make changes, build it, and install it by [following these instructions](CONTRIBUTING.md). This also has instruction on how to contribute your changes back to the main repository.

# Bugs / Feature Requests

To report a bug or submit a feature request specific feature, please use the `GitHub issues page <>`_.

Fill in the issue template as completely as possible and we will respond as soon
as we can.

For hardware support or any other questions not specific to this GitHub project, please visit [NI Community Forums](https://forums.ni.com/).

# License

[License file](LICENSE)

**semi device control python api** is licensed under an MIT-style license
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.
