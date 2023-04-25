"""Overview:.

Demonstrates how to use the "generate_device_elements" API to generate
the class file that contains all the device elements.

Requirement: Python full development system.
Instructions:
1. Run this python code.
2. Use the python file generated to easily access the register and field names.
"""
# flake8: noqa
import os
import sys


# To add the directory of the source file(nisemidevicecontrol.py) when the
# example is opened from the examples folder or the top level folder
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nisdc.nisemidevicecontrol import SemiconductorDeviceControl  # noqa:E402

# Get Instrument Studio Configuration
ISconfigpath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "conf", "isconfig.sdconfig"
)

# Instantiate the 'Device Control session'using the Instantiate API.
semi_device_control = None

try:
    semi_device_control = SemiconductorDeviceControl(ISconfigpath)

    # Generates the nisdc_device_elements.py with register names and bitfield names
    path = semi_device_control.generate_device_elements()
    print("The generated file is located at ", path)

    semi_device_control.destroy()

except Exception as e:
    print("Exception during close: {}".format(e))
    raise e
