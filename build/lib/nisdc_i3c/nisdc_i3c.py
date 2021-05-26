import sys
import os
import clr

device_control_path = "C:\\Program Files\\National Instruments\\Semi Device Control"

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(device_control_path)
clr.AddReference("SemiconductorDeviceControl.NIDigitalI3C.APISupport")

from SemiconductorDeviceControl.NIDigitalI3C.APISupport import SemiconductorDeviceControlI3CSession  # noqa:E402


class SemiDeviceControlI3CSession:
    def __init__(self, semidevicecontrol_session, interface_name, protocol_name):
        '''
        Creates and returns a I3C session using the Semi Device Control session

        Arguments:
            semidevicecontrol_session {Semi Device Control session object}
            interface_name {string}
            protocol_name {string}

        '''

        self.i3c_session = None

        try:
            self.i3c_session = SemiconductorDeviceControlI3CSession(semidevicecontrol_session.semidevicecontrol_session, interface_name, protocol_name)

        except Exception as e:
            print("Exception in accessing I3C Session: {}".format(e))
            raise e

    def execute_dynamic_addressing_ccc(self, ccc_type, command_id, dynamic_address = -1):
        '''
        Executes the CCC used for dynamic addressing based on the given inputs. 
        If for a given <b> Command ID</b> the dynamic address is not applicable then it will not be applied. 
        And if the Command ID doesn’t match with the CCC Type and CCC Operation an exception will be thrown.

        Arguments:
            ccc_type { long }
            command_id {byte}
            dynamic_address {sbyte}

            CCC Type corresponding long int values
            1=Direct
            0-Broadcast
        '''
        try:
            self.i3c_session.ExecuteDynamicAddressingCCC(ccc_type, command_id, dynamic_address)

        except Exception as e:
            print("Exception in execute_dynamic_addressing_ccc(): {}".format(e))
            raise e

    def execute_dynamic_addressing_ccc_with_read(self, ccc_type, command_id, dynamic_address = -1):
        '''
        Executes the CCC used for dynamic addressing based on the given inputs and returns the data read back from the DUT. 
        This API is only applicable for the ENTDAA in the current spec. 
        If for a given <b> Command ID</b> the dynamic address is not applicable then it will not be applied.  
        And if the Command ID doesn’t match with the CCC Type and CCC Operation an exception will be thrown. 

        Arguments:
            ccc_type { long }
            command_id {byte}
            dynamic_address {sbyte}

            CCC Type corresponding long int values
            1=Direct
            0-Broadcast

        Return:
            read_data {byte[]}
        '''
        try:
            read_data = self.i3c_session.ExecuteDynamicAddressingCCCWithRead(ccc_type, command_id, dynamic_address)
            return read_data

        except Exception as e:
            print("Exception in execute_dynamic_addressing_ccc_with_read(): {}".format(e))
            raise e

    def execute_sdr_ccc_write(self, ccc_type, command_id, defining_byte = -1, write_data = None):
        '''
        Executes the write CCC commands used in SDR mode based on the given inputs.  
        If for a given <b> Command ID</b> the <b>defining byte</b> and <b>data</b> are not applicable then they will be ignored.  
        And if the Command ID doesn’t match with the CCC Type and CCC Operation an exception will be thrown. 
        
        Arguments:
            ccc_type { long }
            command_id {byte}
            defining_byte {short}
            write_data {byte[]}

            CCC Type corresponding long int values
            1=Direct
            0-Broadcast

        '''
        try:
            self.i3c_session.ExecuteSDRCCCWrite(ccc_type, command_id, defining_byte, write_data)

        except Exception as e:
            print("Exception in execute_sdr_ccc_write: {}".format(e))
            raise e

    def execute_sdr_ccc_read(self, ccc_type, command_id, defining_byte = -1, read_byte_length = -1):
        '''
        Executes the read CCC commands used in SDR mode based on the given inputs and returns the read data. 
        If for a given <b> Command ID</b> the <b>Defining Byte</b> is not applicable then they will be ignored. 
        The <b> read Data Length</b> will only be considered if the value is not provided in the csv file else it will take the value from the csv file.
        And if the Command ID doesn’t match with the CCC Type and CCC Operation an exception will be thrown.
        
        Arguments:
            ccc_type { long }
            command_id {byte}
            defining_byte {short}
            read_byte_length {int}

            CCC Type corresponding long int values
            1=Direct
            0-Broadcast

        Returns:
            read_data {byte[]}
        '''
        try:
            read_data = self.i3c_session.ExecuteSDRCCCRead(ccc_type, command_id, defining_byte, read_byte_length)
            return read_data

        except Exception as e:
            print("Exception in execute_sdr_ccc_read: {}".format(e))
            raise e
