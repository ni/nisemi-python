# About
NI Semiconductor Device Control Python API Support provides Python APIs and examples to develop python test programs and communicate with a device using the setup configuration exported from the Semiconductor Device Control Add-On for InstrumentStudio.

This library is dependent on Semiconductor Device Control addon for InstrumentStudio.


# Semiconductor Device Control Python API Status

**Setup and cleanup functions**
1. Instantiate - using IS configuration file  
2. Destroy  
3. Start  
4. Stop  

**Hardware Read & Write to Register and Field** 

5. Write Register by name (Device)  
6. Read Register by name (Device)  
7. Write Register by Address (Device)  
8. Read Register by Address (Device)  
9. Write Custom Register by Address (Device) 
10. Read Custom Register by Address (Device) 
11. Write Field by Name (Device)  
12. Read Field by Name (Device)  
13. Write Field by value definition (Device)  

**Hardware multiple Read & Write to Register and Field**

14. Write Multiple Register by Name (Device)  
15. Read Multiple Register by name (Device)  
16. Write Multiple Register by Address (Device)  
17. Read Multiple Register by Address (Device)  
18. Write Multiple Fields by Name (Device)  
19. Read Multiple Field by Name (Device)  

**Cache Read & Write to Register and Field**

20. Write Register by name (Cache)  
21. Read Register by name (Cache)  
22. Write Register by Address (Cache)  
23. Read Register by Address (Cache)  
24. Write Field by Name (Cache)  
25. Read Field by Name (Cache)  
26. Write Field by value definition (cache)  
27. Write from Cache to Device  
28. Clear Cache  

**Cache multiple Read & Write to Register and Field**  

29. Write Multiple Register by Name (Cache)  
30. Read Multiple Register by name (Cache)  
31. Write Multiple Register by Address (Cache)  
32. Read Multiple Register by Address (Cache)  
33. Write Multiple Fields by Name (Cache)  
34. Read Multiple Field by Name (Cache) 

**DIO operation**

35. Write Pin State  
36. Read Pin State 

**Utils**

37. Get Dynamic Protocol Settings
38. Update Dynamic Protocol Settings
39. Get Instrument Session **

(** This API is deprecated from 2023 Q4 version of Semiconductor Device Control Addon.
Refer to the [user manual](https://www.ni.com/documentation/en/semiconductor-device-control/latest/manual/manual-overview/) for more information.)

# Installation   
**Dependency Installation**  
1. Semiconductor Device Control addon for InstrumentStudio 2023 Q4.  
2. pythonnet 2.5.2 - [pypi download](https://pypi.org/project/pythonnet/#description)  

**Work with github source code**  

3. Clone the github repository - [semiconductor device control python api github repo](https://github.com/ni/nisemi-python).  
4. Use the APIs from 'nisdc' folder in your program  

**Work with Semiconductor Device Control Python API from PyPI**

5. Go to Semiconductor Device Control Python API location in the github repository.  
6. Install the package and use the api libraries in your program  

# Usage

Reference example is available in the(https://github.com/ni/nisemi-python) for developers (under examples folder), to refer on how to use the python APIs in the test program.

# Documentation

Documentation is available from ni resource website - [here](https://www.ni.com/documentation/en/semiconductor-device-control/latest/manual/manual-overview/).

# Contributing

We welcome contributions! You can clone the project repository, make changes, build it, and install it by [following these instructions](CONTRIBUTING.md). This also has instruction on how to contribute your changes back to the main repository.

# Bugs / Feature Requests

To report a bug or submit a feature request specific feature, please use the https://github.com/ni/nisemi-python/issues.

Fill in the issue template as completely as possible and we will respond as soon
as we can.

For hardware support or any other questions not specific to this GitHub project, please visit [NI Community Forums](https://forums.ni.com/).

# License

[License file](LICENSE)

**semi device control python api** is licensed under an MIT-style license
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.
