# About
NI Semiconductor Device Control Python API Support provides Python APIs and examples to develop python test programs and communicate with a device using the setup configuration exported from the Semiconductor Device Control Add-On for InstrumentStudio.

This library is dependent on Semiconductor Device Control addon for InstrumentStudio.


# Semiconductor Device Control Python API Status

**Setup and cleanup functions**
1. Instantiate - using IS configuration file  
2. Attach to Existing Session
3. Destroy  
4. Start  
5. Stop  

**Hardware Read & Write to Register and Field** 

6. Write Register by name (Device)  
7. Read Register by name (Device)  
8. Write Register by Address (Device)  
9. Read Register by Address (Device)  
10. Write Custom Register by Address (Device) 
11. Read Custom Register by Address (Device) 
12. Write Field by Name (Device)  
13. Read Field by Name (Device)  
14. Write Field by value definition (Device)  

**Hardware multiple Read & Write to Register and Field**

15. Write Multiple Register by Name (Device)  
16. Read Multiple Register by name (Device)  
17. Write Multiple Register by Address (Device)  
18. Read Multiple Register by Address (Device)  
19. Write Multiple Fields by Name (Device)  
20. Read Multiple Field by Name (Device)  

**Cache Read & Write to Register and Field**

21. Write Register by name (Cache)  
22. Read Register by name (Cache)  
23. Write Register by Address (Cache)  
24. Read Register by Address (Cache)  
25. Write Field by Name (Cache)  
26. Read Field by Name (Cache)  
27. Write Field by value definition (cache)  
28. Write from Cache to Device  
29. Clear Cache  

**Cache multiple Read & Write to Register and Field**  

30. Write Multiple Register by Name (Cache)  
31. Read Multiple Register by name (Cache)  
32. Write Multiple Register by Address (Cache)  
33. Read Multiple Register by Address (Cache)  
34. Write Multiple Fields by Name (Cache)  
35. Read Multiple Field by Name (Cache) 

**DIO operation**

36. Write Pin State  
37. Read Pin State 

**Utils**

38. Get Dynamic Protocol Settings
39. Update Dynamic Protocol Settings
40. Get Instrument Session **
41. Get Session Options

(** This API is deprecated from 2023 Q4 version of Semiconductor Device Control Addon.
Refer to the [user manual](https://www.ni.com/documentation/en/semiconductor-device-control/latest/manual/manual-overview/) for more information.)

# Installation   
**Dependency Installation**  
1. Semiconductor Device Control addon for InstrumentStudio 2024 Q3.  
2. pythonnet 3.0.3 - [pypi download](https://pypi.org/project/pythonnet/#description)  

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
