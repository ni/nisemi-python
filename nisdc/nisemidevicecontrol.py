"""This file is used for Semi Device Control API."""
import os
import sys

import clr
# flake8: noqa
device_control_path = (
    "C:\\Program Files\\National Instruments\\" + "Semi Device Control")

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(device_control_path)

clr.AddReference("SemiconductorDeviceControl")
from SemiconductorDeviceControl import SemiDeviceControlMain  # noqa:E402

def generate_class_string(element_type, device_element_list): 
    """This method generates the class string to be written to the auto generated file."""
    """Arguments: element_type {string},device_element_list {list}"""
    """Return: string - The entire string generated for the class """
    ipblock = ""
    registergroup = ""
    class_content = ""
    class_string = "class "
    hyphen_delimiter = "-"

    class_content += class_string + element_type + "():\n"
    for device_element in device_element_list:
        device_element_details = device_element.split(hyphen_delimiter)
        current_ipblock = device_element_details[0]
        current_register_group = device_element_details[1]
        current_device_element = device_element_details[2]

        if current_ipblock != ipblock:
            class_content += str.format(
                "\t" + class_string + "{}():\n", current_ipblock
            )
            ipblock = current_ipblock

        if current_register_group != registergroup:
            class_content += str.format(
                "\t\t" + class_string + "{}():\n", current_register_group
            )
            registergroup = current_register_group

        class_content += str.format(
            '\t\t\t{} = "{}"\n', current_device_element, device_element
        )
    class_content += "\n\n"
    return class_content


class SemiconductorDeviceControl:
    """This class is used for Instrument Studio export configuration."""

    def __init__(self, isconfigpath):
        """Create and return device control session using Instrument Studio export configuration.

        IS export configuration contains the register map and hardware configuration
        for Device Control.

        Args:
            isconfigpath : the isconfig path.
        """
        self.semidevicecontrol_main = None
        self.semidevicecontrol_session = None

        try:
            self.semidevicecontrol_main = SemiDeviceControlMain()
            self.semidevicecontrol_session = (
                self.semidevicecontrol_main.CreateSemiDeviceControlSession(isconfigpath)
            )

        except Exception as e:
            print("Exception in accessing conf: {}".format(e))
            raise e

    def start(self):
        """Description:.

        Starts the Instrument/Hardware sessions configured for the device control
        through the IS export configuration.
        """
        try:
            self.semidevicecontrol_session.Start()

        except Exception as e:
            print("Exception in start(): {}".format(e))
            raise e

    def stop(self):
        """Stops the Instrument/Hardware sessions configured for the device control."""
        try:
            self.semidevicecontrol_session.Stop()

        except Exception as e:
            print("Exception is stop(): {}".format(e))
            raise e

    def destroy(self):
        """Destroys the device control session.

        Deallocates the reserved reference and data in memory.
        """
        try:
            self.semidevicecontrol_main.DestroySemiDeviceControlSession(
                self.semidevicecontrol_session
            )

        except Exception as e:
            print("Exception is destroy engine: {}".format(e))
            raise e

    # ---------------------------- Register Device ----------------------------

    def write_register_by_name_device(self, register_uid, register_data):
        """Writes the data to the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid: string register uid
            register_data: int register data

        """
        try:
            self.semidevicecontrol_session.WriteRegisterByName_Device(
                register_uid, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_name_device(
        self, register_uid_list, register_data_list
    ):
        """Writes data to multiple registers on the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element,the corresponding element from the data array will be applied.

        Args:
            register_uid_list: {list of string}
            register_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByName_Device(
                register_uid_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_register_by_address_device(
        self, ip_block_name, register_address, register_data
    ):
        """Writes the data to the device using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Args:
            ip_block_name: {string} ip black name
            register_address: {int} register address
            register_data: {int} register data
        """
        try:
            self.semidevicecontrol_session.WriteRegisterByAddress_Device(
                ip_block_name, register_address, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_address_device(
        self, ip_block_name_list, register_address_list, register_data_list
    ):
        """Write data to multiple registers on the device, using the register address.

        And IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding element
        from the data array will be applied.

        Args:
            ip_block_name_list: list of string
            register_address_list: list of int
            register_data_list: list of int
        """
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByAddress_Device(
                ip_block_name_list, register_address_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_custom_register_by_address_device(
        self,
        register_address,
        address_size,
        register_data,
        register_size,
        interface_name,
        protocol_name,
    ):
        """Writes the data using the register address and register size.

           To the device with the given interface and protocol.

        Register address: Address of the register.

        Address size: Size of the address.

        Size: Size of the register.

        Interface name: Name of the interface to use.

        Protocol name: Name of the protocol to use.

        Args:
            register_address: {int}
            address_size: {int}
            register_data: {int}
            register_size: {int}
            interface_name: {string}
            protocol_name: {string}
        """
        try:
            self.semidevicecontrol_session.WriteCustomRegisterByAddress_Device(
                register_address,
                address_size,
                register_data,
                register_size,
                interface_name,
                protocol_name,
            )
        except Exception as e:
            print("")
            raise e

    def read_register_by_name_device(self, register_uid):
        """Reads the data from the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid : {string}

        Returns:
            register_data : {int}
        """
        try:
            register_data = self.semidevicecontrol_session.ReadRegisterByName_Device(
                register_uid
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_name_device(self, register_uid_list):
        """Reads data from multiple registers on the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element, the corresponding element from the data
        array will be applied.

        Args:
            register_uid_list : {list of string}

        Returns:
            register_data_list : {list of int}
        """
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByName_Device(
                    register_uid_list
                )
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    def read_register_by_address_device(self, ip_block_name, register_address):
        """Reads the data from the device using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Args:
            ip_block_name : {string}
            register_address : {int}

        Returns:
            register_data : {int}
        """
        try:
            register_data = self.semidevicecontrol_session.ReadRegisterByAddress_Device(
                ip_block_name, register_address
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_address_device(
        self, ip_block_name_list, register_address_list
    ):
        """Reads data from multiple registers on the device.

        Using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding.

        Element from the data array will be applied.

        Args:
            ip_block_name_list : {list of string}
            register_address_list : {list of int}

        Returns:
            register_data_list : {list of int}
        """
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByAddress_Device(
                    ip_block_name_list, register_address_list
                )
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    def read_custom_register_by_address_device(
        self,
        register_address,
        address_size,
        register_size,
        interface_name,
        protocol_name,
    ):
        """Reads the data using the register address and register size from the device.

        With the given interface and protocol.

        Register address: Address of the register.

        Address size: Size of the address.

        Size: Size of the register.

        Interface name: Name of the interface to use.

        Protocol name: Name of the protocol to use.

        Arguments:
            register_address: {int}
            address_size: {int}
            register_size: {int}
            interface_name: {string}
            protocol_name: {string}

        Returns:
            register_data: {int}
        """
        try:
            register_data = (
                self.semidevicecontrol_session.ReadCustomRegisterByAddress_Device(
                    register_address,
                    address_size,
                    register_size,
                    interface_name,
                    protocol_name,
                )
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def get_register_addresses(self):
        """Gets the list of unique ID and Register addresses.

        Returns:
            register_uid_list: {list of string}
            register_address_list: {list of int
        """
        try:
            register_details = self.semidevicecontrol_session.GetRegisterAddresses()
            register_uid_list = list(register.UniqueID for register in register_details)
            register_address_list = list(
                register.Address for register in register_details
            )
            return register_uid_list, register_address_list

        except Exception as e:
            raise e

    # --------------------------- Register Device ---------------------------

    # ----------------------------- Field Device -----------------------------
    def write_field_by_name_device(self, field_uid, field_data):
        """Writes the data to the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}
            field_data :{int}
        """
        try:
            self.semidevicecontrol_session.WriteFieldByName_Device(
                field_uid, field_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_field_by_name_device(self, field_uid_list, field_data_list):
        """Writes data to multiple fields on the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data.

        Array will be applied.

        Args:
            field_uid_list: {list of string}
            field_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleFieldsByName_Device(
                field_uid_list, field_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_field_by_value_definition_device(self, field_uid, value_definition):
        """Write the data to the device using the field unique name.

        And field value definition.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Value Definition: This is defined in the register map for each field.

        Each value of the field can contain a definition string.

        That represents the value.

        Args:
            field_uid: {string}
            value_definition: {string}
        """
        try:
            self.semidevicecontrol_session.WriteFieldByValueDefinition_Device(
                field_uid, value_definition
            )

        except Exception as e:
            print("")
            raise e

    def read_field_by_name_device(self, field_uid):
        """Reads the data from the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}

        Returns:
            field_data: {int}
        """
        try:
            field_data = self.semidevicecontrol_session.ReadFieldByName_Device(
                field_uid
            )
            return field_data

        except Exception as e:
            print("")
            raise e

    def read_multi_field_by_name_device(self, field_uid_list):
        """Reads data from multiple fields on the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            field_uid_list: {list of string}

        Returns:
            field_data_list: {list of int}
        """
        try:
            field_data_list = (
                self.semidevicecontrol_session.ReadMultipleFieldsByName_Device(
                    field_uid_list
                )
            )
            return field_data_list

        except Exception as e:
            print("")
            raise e

    def get_field_definition_details(self, field_uid):
        """Gets the field display values, field values and field size for given unique ID.

        Arguments:
            field_uid: {string}

        Returns:
            field_display_values {list of string}
            field_values {list of int}
            field_size {int}
        """
        try:
            field_definition = self.semidevicecontrol_session.GetFieldDefinitionDetails(
                field_uid
            )
            return (
                list(field_definition.DisplayValues),
                list(field_definition.Values),
                field_definition.Size,
            )

        except Exception as e:
            raise e

    # ----------------------------- Field Device -----------------------------

    # ---------------------------- Register Cache ----------------------------
    def write_register_by_name_cache(self, register_uid, register_data):
        """Writes the data to the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid: {string}
            register_data: {int}
        """
        try:
            self.semidevicecontrol_session.WriteRegisterByName_Cache(
                register_uid, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_name_cache(self, register_uid_list, register_data_list):
        """Writes data to multiple registers on the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element, the corresponding element from the data.

        Array will be applied.

        Arguments:
            register_uid_list: {list of string}
            register_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByName_Cache(
                register_uid_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_register_by_address_cache(
        self, ip_block_name, register_address, register_data
    ):
        """Writes the data to the cache using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Arguments:
            ip_block_name: {string}
            register_address: {int}
            register_data: {int}
        """
        try:
            self.semidevicecontrol_session.WriteRegisterByAddress_Cache(
                ip_block_name, register_address, register_data
            )

        except Exception as e:
            print("")
            raise e

    def write_multi_register_by_address_cache(
        self, ip_block_name_list, register_address_list, register_data_list
    ):
        """Writes data to multiple registers on the cache.

        Using the register, address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding.

        Element from the data array will be applied.

        Arguments:
            ip_block_name_list: {list of string}
            register_address_list: {list of int}
            register_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleRegistersByAddress_Cache(
                ip_block_name_list, register_address_list, register_data_list
            )

        except Exception as e:
            print("")
            raise e

    def read_register_by_name_cache(self, register_uid):
        """Reads the data from the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid: {string}

        Returns:
            register_data :{int}
        """
        try:
            register_data = self.semidevicecontrol_session.ReadRegisterByName_Cache(
                register_uid
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_name_cache(self, register_uid_list):
        """Reads data from multiple registers on the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element, the corresponding element from the data.
        array will be applied.

        Arguments:
            register_uid_list: {list of string}

        Returns:
            register_data_list: {list of int}
        """
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByName_Cache(
                    register_uid_list
                )
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    def read_register_by_address_cache(self, ip_block_name, register_address):
        """Reads the data from the cache using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Args:
            ip_block_name: {string}
            register_address: {int}

        Returns:
            register_data :{int}
        """
        try:
            register_data = self.semidevicecontrol_session.ReadRegisterByAddress_Cache(
                ip_block_name, register_address
            )
            return register_data

        except Exception as e:
            print("")
            raise e

    def read_multi_register_by_address_cache(
        self, ip_block_name_list, register_address_list
    ):
        """Reads data from multiple registers on the cache.

        Using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding.

        Element from the data array will be applied.

        Args:
            ip_block_name_list: {list of string}
            register_address_list: {list of int}

        Returns:
            register_data_list: {list of int}
        """
        try:
            register_data_list = (
                self.semidevicecontrol_session.ReadMultipleRegistersByAddress(
                    ip_block_name_list, register_address_list
                )
            )
            return register_data_list

        except Exception as e:
            print("")
            raise e

    # ---------------------------- Register Cache ----------------------------

    # ----------------------------- Field Cache -----------------------------

    def write_field_by_name_cache(self, field_uid, field_data):
        """Writes the data to the cache using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}
            field_data: {int}
        """
        try:
            self.semidevicecontrol_session.WriteFieldByName_Cache(field_uid, field_data)

        except Exception as e:
            print("")
            raise e

    def write_multi_field_by_name_cache(self, field_uid_list, field_data_list):
        """Writes data to multiple fields on the cache using the fields unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data.

        Array will be applied.

        Args:
            field_uid_list: {list of string}
            field_data_list: {list of int}
        """
        try:
            self.semidevicecontrol_session.WriteMultipleFieldsByName_Cache(
                field_uid_list, field_data_list
            )

        except Exception as e:
            print("")
            raise e

    def write_field_by_value_definition_cache(self, field_uid, value_definition):
        """Writes the data to the cache using the field unique name.

        And field value definition.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Value Definition: This is defined in the register map for each field.

        Each value of the field can contain a definition string.

        That represents the value.

        Args:
            field_uid: {string}
            value_definition: {string}
        """
        try:
            self.semidevicecontrol_session.WriteFieldByValueDefinition_Cache(
                field_uid, value_definition
            )

        except Exception as e:
            print("")
            raise e

    def read_field_by_name_cache(self, field_uid):
        """Read the data from the cache using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}

        Returns:
            field_data: {int}
        """
        try:
            field_data = self.semidevicecontrol_session.ReadFieldByName_Cache(field_uid)
            return field_data

        except Exception as e:
            print("")
            raise e

    def read_multi_field_by_name_cache(self, field_uid_list):
        """Reads data from multiple fields on the cache using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data.

        Array will be applied.

        Args:
            field_uid_list: {list of string}

        Returns:
            field_data_list: {list of int}
        """
        try:
            field_data_list = (
                self.semidevicecontrol_session.ReadMultipleFieldsByName_Cache(
                    field_uid_list
                )
            )
            return field_data_list

        except Exception as e:
            print("")
            raise e

    # ----------------------------- Field Cache -----------------------------

    # -------------------------------- Cache --------------------------------
    def write_from_cache_to_device(self):
        """Writes all the cache register data to the device, in the order.

        It is stored in the cache memory. The cache will be auto cleared.

        After this operation.
        """
        try:
            self.semidevicecontrol_session.WriteFromCacheToDevice()

        except Exception as e:
            print("Exception in writing software cache to hardware")
            raise e

    def clear_cache(self):
        """Clears all the cache register data from the device control session."""
        try:
            self.semidevicecontrol_session.ClearCache()

        except Exception as e:
            print("Exception in flush software cache")
            raise e

    # ------------------------------ DIO ------------------------------
    def read_pin_state(self, pin_name):
        """Reads the pin state (High / Low / Terminate) using the Pin name.

        Defined in the register map.

        Pin State corresponding int values.2-Terminate, 1=High, 0-Low.

        Args:
            pin_name: {string}

        Return:
            pin_state: {int}
        """
        try:
            pin_state = self.semidevicecontrol_session.ReadPinState(pin_name)
            return pin_state

        except Exception as e:
            print("Exception occured at read pin state")
            raise e

    def write_pin_state(self, pin_name, pin_state):
        """Puts the pin to High / Low / Terminate state using the Pin name.

        defined in the register map.

        Args:
            pin_name: {string}
            pin_state: {int}

            Pin State corresponding int values.

            2-Terminate, 1=High, 0-Low.
        """
        try:
            self.semidevicecontrol_session.WritePinState(pin_name, pin_state)

        except Exception as e:
            print("Exception occured at write pin state")
            raise e

    # -------------------------------- SCRIPTS ------------------------------
    def execute_script(self, file_name, wait_until_complete=True):
        """Executes the script using the Script Name provided as a input.

        If a script is already running on the semi device control session.

        This API will throw error indicating that another script is running already.

        Using waitUntilScriptCompletion bool control, developer can configure.

        This API to run the script as a blocking call or run asynchronously.

        Args:
            file_name: {string}
            wait_until_complete: {bool}

        Returns:
            Array of string, each  string is the result of the command.

            Executed from the script in JSON format {list of string}
        """
        try:
            return self.semidevicecontrol_session.ExecuteScript(
                file_name, wait_until_complete
            )

        except Exception as e:
            print("Exception occured at execute script")
            raise e

    def execute_script_command(self, script_string, wait_until_complete=True):
        """Executes the Script String provided as the input to the API.

        If the Script String is invalid, error will be thrown, and execution will be skipped.
        If waitUntilComplete? is True, then the API will wait until the script is executed.
        Else the API will run the script asynchronously and stop.

        Args:
            script_string :{string}
            wait_until_complete: {bool}

        Returns:
            Array of string, each  string is the result of the command.

            Executed from the script in JSON format {list of string}.
        """
        try:
            return self.semidevicecontrol_session.ExecuteScriptCommand(
                script_string, wait_until_complete
            )

        except Exception as e:
            print("Exception occured at execute script command")
            raise e

    def abort_script(self):
        """Abort Script will abort the current running script on the semi device control session."""
        try:
            self.semidevicecontrol_session.AbortScript()

        except Exception as e:
            print("Exception occured at abort script")
            raise e

    # -------------------------------- UTILS --------------------------------
    def get_logs(self):
        """Get log details.

        Returns:
            logs {2d array of strings}
        """
        try:
            logs = self.semidevicecontrol_session.GetLogs()
            return logs

        except Exception as e:
            print("Exception occured at log function")
            raise e

    def reset_to_default_state(self):
        """Reset the device software register values and dio states to default."""
        try:
            self.semidevicecontrol_session.ResetToDefaultState()

        except Exception as e:
            print("Exception occured at reset to default state")
            raise e

    def get_script_names(self):
        """Gets the list of script file names available in the source folder location.

        Return:
            script_names {list of strings}
        """
        try:
            script_names = self.semidevicecontrol_session.GetScriptFileName()
            return script_names

        except Exception as e:
            print("Exception occured at get script names")
            raise e

    def get_protocol_dynamic_setting(self, interface_name, protocol_name, setting_name):
        """Gets the dynamic protocol setting value of the protocol setting.

        Args:
            interface_name: {string}
            protocol_name: {string}
            setting_name: {string}

        Return:
            setting_value {string}
        """
        try:
            return self.semidevicecontrol_session.GetProtocolDynamicSetting(
                interface_name, protocol_name, setting_name
            )

        except Exception as e:
            print("Exception occured at get protocol settings")
            raise e

    def set_protocol_dynamic_setting(
        self, interface_name, protocol_name, setting_name, setting_value
    ):
        """Updates the dynamic protocol settings of the protocol.

        Args:
            interface_name: {string}
            protocol_name: {string}
            setting_name: {string}
            setting_value: {string}
        """
        try:
            self.semidevicecontrol_session.SetProtocolDynamicSetting(
                interface_name, protocol_name, setting_name, setting_value
            )

        except Exception as e:
            print("Exception occured at update dynamic protocol settings")
            raise e

    def get_interface_dynamic_setting(self, interface_name, setting_name):
        """Gets the dynamic interface setting value of the interface setting.

        Args:
            interface_name: {string}
            setting_name: {string}

        Return:
            setting_value: {string}
        """
        try:
            return self.semidevicecontrol_session.GetInterfaceDynamicSetting(
                interface_name, setting_name
            )

        except Exception as e:
            print("Exception occured at get interface settings")
            raise e

    def set_interface_dynamic_setting(
        self, interface_name, setting_name, setting_value
    ):
        """Updates the dynamic interface setting value of the interface setting.

        Args:
            interface_name: {string}
            setting_name: {string}
            setting_value: {string}
        """
        try:
            self.semidevicecontrol_session.SetInterfaceDynamicSetting(
                interface_name, setting_name, setting_value
            )

        except Exception as e:
            print("Exception occured at update dynamic interface settings")
            raise e

    def get_instrument_session(self, interface_name):
        """Gets the session ID of the instrument.

        Return:
            int {session ID}
        """
        try:
            return self.semidevicecontrol_session.GetInterfaceSessionID(interface_name)

        except Exception as e:
            print("Exception occured at get instrument session")
            raise e

    def get_interface_details(self):
        """Gets the list of interface name and interface type.

        Return:
            interface_name_list {list of string}
            interface_type_list {list of string}
        """
        try:
            interface_details = self.semidevicecontrol_session.GetInterfaceDetails()
            interface_name_list = list(
                interface.Name for interface in interface_details
            )
            interface_type_list = list(
                interface.Type for interface in interface_details
            )
            return interface_name_list, interface_type_list

        except Exception as e:
            print("Exception occured at get interface details")
            raise e

    def get_script_string(self, script_name):
        """API provides the Script String and IsScriptFileValid status from Device Control session.

        For the given the Script Name input.

        Args:
            script_name: {string}

        Return:
            Tuple { bool - IsScriptValid, string - ScriptContent}
        """
        try:
            script_detail = self.semidevicecontrol_session.GetScriptString(script_name)
            return script_detail.IsScriptValid, script_detail.ScriptContent

        except Exception as e:
            print("Exception occured at get script string")
            raise e

    def generate_device_elements(self, directory=""):
        """This API generates a class file in the specified directory.

        That contains the register and field elements from the register map
        configured in the sdcconfig file.
        If the directory provided is empty, the file will be created in the working directory.

        Args:
            directory: {string}

        Return:
            string - The path where the file is created
        """
        try:
            if directory == "":
                directory = os.getcwd()
            elif not (os.path.exists(directory)):
                raise "Invalid path to generate the class file"
            directory += "\\nisdc_device_elements.py"
            device_state_keys = self.semidevicecontrol_session.GetDeviceStateKeys()

            with open(directory, "w+") as class_file:
                class_file.write(
                    generate_class_string(
                        "Register", list(device_state_keys.RegisterUIDs)
                    )
                )
                class_file.write(
                    generate_class_string("Field", list(device_state_keys.FieldUIDs))
                )
            return directory
        except Exception as e:
            print("Exception occured at generate device elements")
            raise e
