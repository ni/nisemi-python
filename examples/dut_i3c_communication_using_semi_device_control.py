'''
Overview: Demonstrates how to use the Semi Device Control APIs to establish
communication sequence with the DUT using I3C protocol
Requirement: Python full development system

Instructions:
    1. Run this python code
    2. View the read register value being printed in the terminal for each
    iteration
'''

import os
import sys
import time

# To add the directory of the source file(nisemidevicecontrol.py) when the
# example is opened from the examples folder or the top level folder
sys.path.append(os.path.normpath(os.getcwd() + os.sep + os.pardir))
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nisdc.nisemidevicecontrol import SemiconductorDeviceControl  # noqa:E402
from nisdc_i3c.nisdc_i3c import SemiDeviceControlI3CSession  # noqa:E402

# Get Instrument Studio Configuration
ISconfigpath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'conf', 'LPS22HH I3C.sdconfig'
)


# Instantiate the 'Device Control session' and start the 'Hardware session'
# using the Instantiate and Start API respectively. These have to always be
# the two APIs used at the start/during setup sequence to create the required
# handles internally
semi_device_control = None
i3c_session = None

try:

    semi_device_control = SemiconductorDeviceControl(ISconfigpath)
    semi_device_control.start()

    interface_name = "NI 657x"
    protocol_name = "I3C"
    # Create I3C Session
    i3c_session = SemiDeviceControlI3CSession(semi_device_control, interface_name, protocol_name)

    # Using the Script APIs to control Board/Device Pins

    semi_device_control.write_pin_state("Vdd", 1)
    semi_device_control.write_pin_state("Vdd_IO", 1)
    semi_device_control.write_pin_state("CS", 1)
    semi_device_control.write_pin_state("SDO", 0)

    # Wait for DUT to start up
    time.sleep(0.5)

    # Using the write register and read register APIs to perform device operation in I2C mode
    semi_device_control.write_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H", 10)
    reg_data = semi_device_control.read_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H")
    print(hex(reg_data))

    '''
    CCC Types corresponding long int values
    1=Direct
    0=Broadcast
    '''
    
    SETDASA_command = 135
    GETPID_command = 141
    RSTDAA_command = 6

    # SETDASA command in Dynamic Addressing mode
    i3c_session.execute_dynamic_addressing_ccc(1, SETDASA_command, 37)

    # GETPID command in SDR CCC mode
    print("The device PID value is " + i3c_session.execute_sdr_ccc_read(1, GETPID_command))

    # Using the write register and read register APIs to perform device operation in I3C mode
    semi_device_control.write_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H", 15)
    reg_data = semi_device_control.read_register_by_name_device(
            "LPS22HH-Control_Register-THS_P_H")
    print(hex(reg_data))
    time.sleep(0.5)

    # RSTDAA command that resets the DUT in Dynamic Addressing mode
    i3c_session.execute_dynamic_addressing_ccc(0, RSTDAA_command)

    semi_device_control.write_pin_state("Vdd_IO", 0)
    semi_device_control.write_pin_state("Vdd", 0)
    semi_device_control.write_pin_state("CS", 0)

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
