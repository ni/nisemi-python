import sys
import os
import clr

device_control_path = "C:\\Program Files\\National Instruments\\" \
    + "Semi Device Control"

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(device_control_path)

clr.AddReference("SemiconductorDeviceControl")
from SemiconductorDeviceControl import SemiDeviceControlMain  # noqa:E402


class SemiconductorDeviceControl:
    def __init__(self, ISconfigpath):
        '''
        Creates and returns a device control session using the Instrument
        Studio export configuration. IS export configuration contains the
        register map and hardware configuration for Device Control

        Arguments:
            ISconfigpath {path}

        '''
        self.semidevicecontrol_main = None
        self.semidevicecontrol_session = None

        try:
            self.semidevicecontrol_main = SemiDeviceControlMain()
            self.semidevicecontrol_session = (
                self.semidevicecontrol_main.CreateSemiDeviceControlSession(
                    ISconfigpath)
            )

        except Exception as e:
            print("Exception in accessing conf: {}".format(e))
            raise e

    def start(self):
        '''
        Starts the Instrument/Hardware sessions configured for the device
        control, through the IS export configuration.
        '''
        try:
            self.semidevicecontrol_session.Start()

        except Exception as e:
            print("Exception in start(): {}".format(e))
            raise e

    def stop(self):
        '''
        Stops the Instrument/Hardware sessions configured for the
        device control
        '''
        try:
            self.semidevicecontrol_session.Stop()

        except Exception as e:
            print("Exception is stop(): {}".format(e))
            raise e

    def destroy(self):
        '''
        Destroys the device control session and deallocates the reserved
        reference and data in memory
        '''
        try:
            self.semidevicecontrol_main.DestroySemiDeviceControlSession(
                self.semidevicecontrol_session)

        except Exception as e:
            print("Exception is destroy engine: {}".format(e))
            raise e

    # ---------------------------- Register Device ----------------------------

    def write_register_by_name_device(self, register_uid, register_data):
        '''
        Writes the data to the device using the register unique name.

        Register UID: Unique name for the register in the format
        <IP block/Device name>-<Register group>-<Register name>

        Arguments:
            register_uid {string}
            register_data {long}

        '''
        try:
            self.semidevicecontrol_session.WriteRegisterByName_Device(
                register_uid, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_name_device(
            self, register_uid_list, register_data_list):
        '''
        Writes data to multiple registers on the device using the register
        unique name.

        Register UID: Unique name for the register in the format
        <IP block/Device name>-<Register group>-<Register name>

        For each Register UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            register_uid_list {string[]}
            register_data_list {long[]}

        '''
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByName_Device(
                register_uid_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_register_by_address_device(
            self, ip_block_name, register_address, register_data):
        '''
        Writes the data to the device using the register address and
        IP block name.

        Register address: Address of the register from register map

        IP block name: Name of the IP block or Device from register map

        Arguments:
            ip_block_name {string}
            register_address {long}
            register_data {long}

        '''
        try:
            self.semidevicecontrol_session.WriteRegisterByAddress_Device(
                ip_block_name, register_address, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_address_device(
            self, ip_block_name_list,
            register_address_list,
            register_data_list):
        '''
        Writes data to multiple registers on the device, using the register
        address and IP block name.

        Register address: Address of the register from register map

        IP block name: Name of the IP block or Device from register map

        For each Register address & IP block element, the corresponding element
        from the data array will be applied.

        Arguments:
            ip_block_name_list {string[]}
            register_address_list {long[]}
            register_data_list {long[]}

        '''
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByAddress_Device(
                ip_block_name_list, register_address_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def read_register_by_name_device(self, register_uid):
        '''
        Reads the data from the device using the register unique name.

        Register UID: Unique name for the register in the format
        <IP block/Device name>-<Register group>-<Register name>

        Arguments:
            register_uid {string}
        Returns:
            register_data {long}
        '''
        try:
            register_data = (
                self.semidevicecontrol_session.ReadRegisterByName_Device(
                    register_uid)
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_name_device(self, register_uid_list):
        '''
        Reads data from multiple registers on the device using the register
        unique name.

        Register UID: Unique name for the register in the format
        <IP block/Device name>-<Register group>-<Register name>

        For each Register UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            register_uid_list {string[]}
        Returns:
            register_data_list {long[]}
        '''
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByName_Device(
                    register_uid_list)
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    def read_register_by_address_device(self, ip_block_name, register_address):
        '''
        Reads the data from the device using the register address and
        IP block name

        Register address: Address of the register from register map

        IP block name: Name of the IP block or Device from register map

        Arguments:
            ip_block_name {string}
            register_address {long}
        Returns:
            register_data {long}
        '''
        try:
            register_data = (
                self.semidevicecontrol_session.ReadRegisterByAddress_Device(
                    ip_block_name, register_address)
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_address_device(
            self, ip_block_name_list, register_address_list):
        '''
        Reads data from multiple registers on the device using the register
        address and IP block name.

        Register address: Address of the register from register map

        IP block name: Name of the IP block or Device from register map

        For each Register address & IP block element, the corresponding
        element from the data array will be applied.

        Arguments:
            ip_block_name_list {string[]}
            register_address_list {long[]}
        Returns:
            register_data_list {long[]}
        '''
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByAddress_Device(
                    ip_block_name_list, register_address_list)
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    # --------------------------- Register Device ---------------------------

    # ----------------------------- Field Device -----------------------------
    def write_field_by_name_device(self, field_uid, field_data):
        '''
        Writes the data to the device using the field unique name.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        Arguments:
            field_uid {string}
            field_data {long}

        '''
        try:
            self.semidevicecontrol_session.WriteFieldByName_Device(
                field_uid, field_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_field_by_name_device(
            self, field_uid_list, field_data_list):
        '''
        Writes data to multiple fields on the device using the field unique
        name.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        For each Field UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            field_uid_list {string[]}
            field_data_list {long[]}

        '''
        try:
            self.semidevicecontrol_session.WriteMultipleFieldsByName_Device(
                field_uid_list, field_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_field_by_value_definition_device(
            self, field_uid, value_definition):
        '''
        Writes the data to the device using the field unique name and
        field value definition.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        Value Definition: This is defined in the register map for each field.
        Each value of the field can contain a definition string,
        that represents the value.

        Arguments:
            field_uid {string}
            value_definition {string}

        '''
        try:
            self.semidevicecontrol_session.WriteFieldByValueDefinition_Device(
                field_uid, value_definition
            )

        except Exception as e:
            print("")
            raise e

    def read_field_by_name_device(self, field_uid):
        '''
        Reads the data from the device using the field unique name.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        Arguments:
            field_uid {string}
        Returns:
            field_data {long}
        '''
        try:
            field_data = self.semidevicecontrol_session.ReadFieldByName_Device(
                field_uid
            )
            return field_data

        except Exception as e:
            print("")
            raise e

    def read_multi_field_by_name_device(self, field_uid_list):
        '''
        Reads data from multiple fields on the device using the field unique
        name.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        For each Field UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            field_uid_list {string[]}
        Returns:
            field_data_list {long[]}
        '''
        try:
            field_data_list = (
                self.semidevicecontrol_session.ReadMultipleFieldsByName_Device(
                    field_uid_list)
            )
            return field_data_list

        except Exception as e:
            print("")
            raise e

    # ----------------------------- Field Device -----------------------------

    # ---------------------------- Register Cache ----------------------------
    def write_register_by_name_cache(self, register_uid, register_data):
        '''
        Writes the data to the cache using the register unique name.

        Register UID: Unique name for the register in the format
        <IP block/Device name>-<Register group>-<Register name>

        Arguments:
            register_uid {string}
            register_data {long}

        '''
        try:
            self.semidevicecontrol_session.WriteRegisterByName_Cache(
                register_uid, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_name_cache(
            self, register_uid_list, register_data_list):
        '''
        Writes data to multiple registers on the cache using the register
        unique name.

        Register UID: Unique name for the register in the format
        <IP block/Device name>-<Register group>-<Register name>

        For each Register UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            register_uid_list {string[]}
            register_data_list {long[]}

        '''
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByName_Cache(
                register_uid_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_register_by_address_cache(
            self, ip_block_name, register_address, register_data):
        '''
        Writes the data to the cache using the register address and
        IP block name.

        Register address: Address of the register from register map

        IP block name: Name of the IP block or Device from register map

        Arguments:
            ip_block_name {string}
            register_address {long}
            register_data {long}

        '''
        try:
            self.semidevicecontrol_session.WriteRegisterByAddress_Cache(
                ip_block_name, register_address,
                register_data)

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_address_cache(
            self, ip_block_name_list,
            register_address_list,
            register_data_list):
        '''
        Writes data to multiple registers on the cache using the register
        address and IP block name.

        Register address: Address of the register from register map

        IP block name: Name of the IP block or Device from register map

        For each Register address & IP block element, the corresponding
        element from the data array will be applied.

        Arguments:
            ip_block_name_list {string[]}
            register_address_list {long[]}
            register_data_list {long[]}

        '''
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByAddress_Cache(
                ip_block_name_list, register_address_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def read_register_by_name_cache(self, register_uid):
        '''
        Reads the data from the cache using the register unique name.

        Register UID: Unique name for the register in the format
        <IP block/Device name>-<Register group>-<Register name>

        Arguments:
            register_uid {string}
        Returns:
            register_data {long}
        '''
        try:
            register_data = (
                self.semidevicecontrol_session.ReadRegisterByName_Cache(
                    register_uid)
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_name_cache(self, register_uid_list):
        '''
        Reads data from multiple registers on the cache using the register
        unique name.

        Register UID: Unique name for the register in the format
        <IP block/Device name>-<Register group>-<Register name>

        For each Register UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            register_uid_list {string[]}
        Returns:
            register_data_list {long[]}
        '''
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByName_Cache(
                    register_uid_list)
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    def read_register_by_address_cache(self, ip_block_name, register_address):
        '''
        Reads the data from the cache using the register address and
        IP block name.

        Register address: Address of the register from register map

        IP block name: Name of the IP block or Device from register map

        Arguments:
            ip_block_name {string}
            register_address {long}
        Returns:
            register_data {long}
        '''
        try:
            register_data = (
                self.semidevicecontrol_session.ReadRegisterByAddress_Cache(
                    ip_block_name, register_address)
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_address_cache(
            self, ip_block_name_list, register_address_list):
        '''
        Reads data from multiple registers on the cache using the register
        address and IP block name.

        Register address: Address of the register from register map

        IP block name: Name of the IP block or Device from register map

        For each Register address & IP block element, the corresponding
        element from the data array will be applied.

        Arguments:
            ip_block_name_list {string[]}
            register_address_list {long[]}
        Returns:
            register_data_list {long[]}
        '''
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByAddress(
                    ip_block_name_list, register_address_list)
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    # ---------------------------- Register Cache ----------------------------

    # ----------------------------- Field Cache -----------------------------

    def write_field_by_name_cache(self, field_uid, field_data):
        '''
        Writes the data to the cache using the field unique name.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        Arguments:
            field_uid {string}
            field_data {long}

        '''
        try:
            self.semidevicecontrol_session.WriteFieldByName_Cache(
                field_uid, field_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_field_by_name_cache(
            self, field_uid_list, field_data_list):
        '''
        Writes data to multiple fields on the cache using the fields
        unique name.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        For each Field UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            field_uid_list {string[]}
            field_data_list {long[]}

        '''
        try:
            self.semidevicecontrol_session.WriteMultipleFieldsByName_Cache(
                field_uid_list, field_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_field_by_value_definition_cache(
            self, field_uid, value_definition):
        '''
        Writes the data to the cache using the field unique name and
        field value definition.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        Value Definition: This is defined in the register map for each field.
        Each value of the field can contain a definition string,
        that represents the value.

        Arguments:
            field_uid {string}
            value_definition {string}

        '''
        try:
            self.semidevicecontrol_session.WriteFieldByValueDefinition_Cache(
                field_uid, value_definition
            )

        except Exception as e:
            print("")
            raise e

    def read_field_by_name_cache(self, field_uid):
        '''
        Read the data from the cache using the field unique name.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        Arguments:
            field_uid {string}
        Returns:
            field_data {long}
        '''
        try:
            field_data = self.semidevicecontrol_session.ReadFieldByName_Cache(
                field_uid
            )
            return field_data

        except Exception as e:
            print("")
            raise e

    def read_multi_field_by_name_cache(self, field_uid_list):
        '''
        Reads data from multiple fields on the cache using the field
        unique name.

        Field UID: Unique name for the field in the format
        <IP block/Device name>-<Register group>-<Field name>

        For each Field UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            field_uid_list {string[]}
        Returns:
            field_data_list {long[]}
        '''
        try:
            field_data_list = (
                self.semidevicecontrol_session.ReadMultipleFieldsByName_Cache(
                    field_uid_list)
            )
            return field_data_list

        except Exception as e:
            print("")
            raise e

    # ----------------------------- Field Cache -----------------------------

    # -------------------------------- Cache --------------------------------

    def write_from_cache_to_device(self):
        '''
        Writes all the cache register data to the device, in the order it is
        stored in the cache memory. The cache will be auto cleared after
        this operation.
        '''
        try:
            self.semidevicecontrol_session.WriteFromCacheToDevice()

        except Exception as e:
            print("Exception in writing software cache to hardware")
            raise e

    def clear_cache(self):
        '''
        Clears all the cache register data from the device control session
        '''
        try:
            self.semidevicecontrol_session.ClearCache()

        except Exception as e:
            print("Exception in flush software cache")
            raise e

    # ------------------------------ DIO ------------------------------

    def read_pin_state(self, pin_name):
        '''
        Reads the pin state (High / Low / Terminate) using the Pin name
        defined in the register map.

        Arguments:
            pin_name {string}
        Return:
            pin_state {long}


        Pin State corresponding long int values
        2-Terminate
        1=High
        0-Low
        '''

        try:
            pin_state = self.semidevicecontrol_session.ReadPinState(
                pin_name
            )
            return pin_state

        except Exception as e:
            print("Exception occured at read pin state")
            raise e

    def write_pin_state(self, pin_name, pin_state):
        '''
        Puts the pin to High / Low / Terminate state using the Pin name
        defined in the register map.

        Arguments:
            pin_name {string}
            pin_state {long}

            Pin State corresponding long int values
            2-Terminate
            1=High
            0-Low

        '''
        try:
            self.semidevicecontrol_session.WritePinState(
                pin_name, pin_state
            )

        except Exception as e:
            print("Exception occured at write pin state")
            raise e

    # -------------------------------- SCRIPTS ------------------------------

    def execute_script(self, file_name, wait_until_complete=True):
        '''
        Executes the script using the <b>Script Name</b> provided as a input.
        If a script is already running on the semi device control session, this API will throw error indicating that another script is running already.
        Using <b> waitUntilScriptCompletion</b> bool control, developer can configure this API to run the script as a blocking call or run asynchronously. 

        Arguments:
            file_name {string}
            wait_until_complete {bool}
        '''
        
        try:
            self.semidevicecontrol_session.ExecuteScript(file_name, wait_until_complete)

        except Exception as e:
            print("Exception occured at execute script")
            raise e

    def execute_script_command(self, script_string, wait_until_complete=True):
        '''
        Executes the <b>Script String</b> provided as the input to the API.
        If the <b>Script String</b> is invalid, error will be thrown, and execution will be skipped.
        If <b>waitUntilComplete?</b> is <b>True</b>, then the API will wait until the script is executed, else the API will run the script asynchronously and stop.

        Arguments:
            script_string {string}
            wait_until_complete {bool}
        '''
        
        try:
            self.semidevicecontrol_session.ExecuteScriptCommand(script_string, wait_until_complete)

        except Exception as e:
            print("Exception occured at execute script command")
            raise e

    def abort_script(self):
        '''
        Abort Script will abort the currently running script on the semi device control session. 
        '''
        
        try:
            self.semidevicecontrol_session.AbortScript()

        except Exception as e:
            print("Exception occured at abort script")
            raise e

    # -------------------------------- UTILS --------------------------------

    def get_logs(self):
        '''
        Get log details

        Returns:
            logs {2d array of strings}
        '''

        try:
            logs = self.semidevicecontrol_session.GetLogs()
            return logs

        except Exception as e:
            print("Exception occured at log function")
            raise e

    def reset_to_default_state(self):
        '''
        Reset the device software register values and dio states to default.
        '''
        
        try:
            self.semidevicecontrol_session.ResetToDefaultState()

        except Exception as e:
            print("Exception occured at reset to default state")
            raise e
    
    def get_script_names(self):
        '''
        Gets the list of script file names available in the source folder location

        Return:
            script_names {list of strings}
        '''
        
        try:
            script_names = self.semidevicecontrol_session.GetScriptFileName()
            return script_names

        except Exception as e:
            print("Exception occured at get script names")
            raise e

    def get_script_string(self, script_name):
        '''
        This API provides the <b>Script String</b> and <b>IsScriptFileValid</b> status from Device Control session for the given the <b>Script Name</b> input.

        Arguments:
            script_name {string}

        Return:
            Tuple { bool - IsScriptValid, string - ScriptContent}
        '''
        
        try:
            script_detail = self.semidevicecontrol_session.GetScriptString(script_name)
            return script_detail.IsScriptValid, script_detail.ScriptContent

        except Exception as e:
            print("Exception occured at get script string")
            raise e
