'''
Overview: Demonstrates how to use the NI Digital Instance through
Semi Device Control APIs to establish communication sequence with the DUT
Requirement: Python full development system

Instructions:
    1. Run this python code
    2. View the read register value being printed in the terminal for each
    iteration
'''

import os
import sys
import time
import nidigital

# To add the directory of the source file(nisemidevicecontrol.py) when the
# example is opened from the examples folder or the top level folder
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nisdc.nisemidevicecontrol import SemiconductorDeviceControl  # noqa:E402

# Get Instrument Studio Configuration
ISconfigpath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'conf', 'LPS22HH I3C.sdconfig'
)


# Instantiate the 'Device Control session' and start the 'Hardware session'
# using the Instantiate and Start API respectively. These have to always be
# the two APIs used at the start/during setup sequence to create the required
# handles internally
semi_device_control = None
nidigital_session = None

try:

    semi_device_control = SemiconductorDeviceControl(ISconfigpath)
    semi_device_control.start()

    # Get the 657x session 
    session_id = semi_device_control.get_instrument_session("NI 657x")
    nidigital_session =  nidigital.Session.from_handle(session_id)

    # Using the NI Digital DIO APIs to control Board/Device Pins
    pinset = nidigital_session.channels["3"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ONE)

    pinset = nidigital_session.channels["4"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ONE)

    pinset = nidigital_session.channels["7"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ONE)

    pinset = nidigital_session.channels["0"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ZERO)

    # Wait for DUT to start up
    time.sleep(0.5)

    # Using the Write Register APIs to burst the register data to the device
    # Using the Read Register APIs to read the register data from the device
    for i in range(25):
        semi_device_control.write_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H", i)

        reg_data = semi_device_control.read_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H")

        print(hex(reg_data))
        time.sleep(0.5)

    pinset = nidigital_session.channels["4"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ZERO)

    pinset = nidigital_session.channels["3"]
    pinset.selected_function = nidigital.SelectedFunction.DIGITAL
    pinset.write_static(nidigital.WriteStaticPinState.ZERO)

except Exception as e:
    print("Exception occurred: {}".format(e))
    raise e

# Stop the Hardware sessions that are previously initialized during the Start
# operation, and closing the Device Control session using the destroy API
finally:
    try:
        semi_device_control.stop()
        semi_device_control.destroy()

    except Exception as e:
        print("Exception during close: {}".format(e))
        raise e
