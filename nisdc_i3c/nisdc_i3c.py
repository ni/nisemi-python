"""This file is used for Semi Device Control I3C API."""
import os
import sys

import clr


device_control_path = "C:\\Program Files\\National Instruments\\Semi Device Control"

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(device_control_path)
clr.AddReference("SemiconductorDeviceControl.NIDigitalI3C.APISupport")

from SemiconductorDeviceControl.NIDigitalI3C.APISupport import (SemiconductorDeviceControlI3CSession,)  # noqa:E402

class SemiDeviceControlI3CSession:
    """"This class is used to create I3C session."""
    def __init__(self, semidevicecontrol_session, interface_name, protocol_name):
        """Creates and returns a I3C session using the Semi Device Control session.

        Args:
            semidevicecontrol_session: {Semi Device Control session object}
            interface_name: {string}
            protocol_name: {string}
        """
        self.i3c_session = None
        try:
            self.i3c_session = SemiconductorDeviceControlI3CSession(
                semidevicecontrol_session.semidevicecontrol_session,
                interface_name,
                protocol_name,
            )

        except Exception as e:
            print("Exception in accessing I3C Session: {}".format(e))
            raise e

    def execute_dynamic_addressing_ccc(self, ccc_type, command_id, dynamic_address=-1):
        """Executes the CCC used for dynamic addressing based on the given inputs.
        
        If for a given Command ID the dynamic address is not applicable then it will not be applied
        and if the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values.1=Direct,0-Broadcast.

        Args:
            ccc_type: { int }
            command_id: {int}
            dynamic_address: {int}
        """
        try:
            self.i3c_session.ExecuteDynamicAddressingCCC(
                ccc_type, command_id, dynamic_address
            )

        except Exception as e:
            print("Exception in execute_dynamic_addressing_ccc(): {}".format(e))
            raise e

    def execute_dynamic_addressing_ccc_with_read(
        self, ccc_type, command_id, dynamic_address=-1
    ):
        """Executes the CCC used for dynamic addressing based on the given inputs.
        
        And returns the data read back from the DUT.
        This API is only applicable for the ENTDAA in the current spec.
        If for a given Command ID the dynamic address is not applicable then it will not be applied
        and if the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values. 1=Direct, 0-Broadcast.

        Args:
            ccc_type: { int }
            command_id: {int}
            dynamic_address: {int}

        Return:
            read_data {list of int}
        """
        try:
            read_data = self.i3c_session.ExecuteDynamicAddressingCCCWithRead(
                ccc_type, command_id, dynamic_address
            )
            return read_data

        except Exception as e:
            print(
                "Exception in execute_dynamic_addressing_ccc_with_read(): {}".format(e)
            )
            raise e

    def execute_sdr_ccc_write(
        self, ccc_type, command_id, defining_byte=-1, write_data=None
    ):
        """Executes the write CCC commands used in SDR mode based on the given inputs.
        
        If for a given Command ID the defining byte
        and data are not applicable then they will be ignored.
        If the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values. 1=Direct, 0-Broadcast.

        Arguments:
            ccc_type: { int }
            command_id: {int}
            defining_byte: {int}
            write_data: {list of int}
        """
        try:
            self.i3c_session.ExecuteSDRCCCWrite(
                ccc_type, command_id, defining_byte, write_data
            )

        except Exception as e:
            print("Exception in execute_sdr_ccc_write: {}".format(e))
            raise e

    def execute_sdr_ccc_read(
        self, ccc_type, command_id, defining_byte=-1, read_byte_length=-1
    ):
        """Executes the read CCC commands used in SDR mode based on the given inputs.
        
        And returns the read data.
        If for a given Command ID the Defining Byte is not applicable then they will be ignored.
        The  read Data Length will only be considered if the value is not provided in the csv file
        else it will take the value from the csv file.
        and if the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values. 1=Direct, 0-Broadcast.

        Arguments:
            ccc_type: { int }
            command_id: {int}
            defining_byte: {int}
            read_byte_length: {int}

        Returns:
            read_data {list of int}
        """
        try:
            read_data = self.i3c_session.ExecuteSDRCCCRead(
                ccc_type, command_id, defining_byte, read_byte_length
            )
            return read_data

        except Exception as e:
            print("Exception in execute_sdr_ccc_read: {}".format(e))
            raise e
