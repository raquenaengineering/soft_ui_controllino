


"""
To be able to synchronize easily any changes in the communication between the controllino and the UI,
- The command list will be implemented as a separate file.
- A script that autogenerates the expected commands on the firmware side will be created.
- The output of the script will be copied to the folder where the firmware is compiled (as a source file)
- So, it can be read and compiled with the firmware everytime there is a change.

ui side: controllino_command_list.py
    - class with a lot of variables?
        - probably best option
firmware side: command_list.h
    - defines
    - const chars? --> probably this option better.
"""

import pathlib

class controllino_command_list():

    # SPECIAL #

    cmd_software_reset = b' '                        # IMPOOOOOOOORTANT!

    # ANALOG INPUTS #

    cmd_request_analog_inputs = b'-'
    cmd_request_digital_outputs = b'_'
    cmd_request_relay_outputs = b','
    cmd_request_all = b';'


    # DIGITAL OUTPUTS #

    cmd_pin_d0_on = b'+'
    cmd_pin_d0_off = b'*'

    cmd_pin_d1_on = b'1'
    cmd_pin_d1_off = b'!'

    cmd_pin_d2_on = b'2'
    cmd_pin_d2_off = b'"'

    cmd_pin_d3_on = b'3'
    cmd_pin_d3_off = b'#'            # original command was '·', but is not an ASCII character


    cmd_pin_d4_on = b'4'
    cmd_pin_d4_off = b'$'

    cmd_pin_d5_on = b'5'
    cmd_pin_d5_off = b'%'

    cmd_pin_d6_on = b'6'
    cmd_pin_d6_off = b'&'

    cmd_pin_d7_on = b'7'
    cmd_pin_d7_off = b'/'


    cmd_pin_d8_on = b'8'
    cmd_pin_d8_off = b'('

    cmd_pin_d9_on = b'9'
    cmd_pin_d9_off = b')'

    cmd_pin_d10_on = b'0'
    cmd_pin_d10_off = b'='

    cmd_pin_d11_on = b':'
    cmd_pin_d11_off = b'?'

    # RELAY OUTPUTS #

    cmd_pin_r0_on = b'q'
    cmd_pin_r0_off = b'Q'

    cmd_pin_r1_on = b'w'
    cmd_pin_r1_off = b'W'

    cmd_pin_r2_on = b'e'
    cmd_pin_r2_off = b'E'

    cmd_pin_r3_on = b'r'
    cmd_pin_r3_off = b'R'


    cmd_pin_r4_on = b't'
    cmd_pin_r4_off = b'T'

    cmd_pin_r5_on = b'y'
    cmd_pin_r5_off = b'Y'

    cmd_pin_r6_on = b'u'
    cmd_pin_r6_off = b'U'

    cmd_pin_r7_on = b'i'
    cmd_pin_r7_off = b'I'


    cmd_pin_r8_on = b'o'
    cmd_pin_r8_off = b'O'

    cmd_pin_r9_on = b'p'
    cmd_pin_r9_off = b'P'

    cmd_all_off = b'<'

    def __init__(self):             # not needed, this class is just a variable container.
        pass

    #
    # def get_variables(self):
    #     return [(name, value) for name, value in vars(self).items()]


if __name__ == "__main__":


    # ccl = controllino_command_list()
    # for param in vars(ccl):
    #     print(param)

    # for param in vars(controllino_command_list):
    #     print(param)


    # Create an instance of the class
    ccl = controllino_command_list()

    # Get a list of variable names and values
    command_list = [(name, getattr(ccl, name)) for name in dir(controllino_command_list) if
                      not name.startswith("__")]

    # # Print the list
    # for name, value in command_list:
    #     print(name + " = " + str(value) + ";")

    working_dir = pathlib.Path.cwd()

    print("Current working directory: ")
    print(working_dir)

    command_h_file = open("firm/firm_ui_controllino_io/src/command_list_autogenerated.h", 'w')
    # Write the header guard
    command_h_file.write("#ifndef COMMAND_LIST_H\n")
    command_h_file.write("#define COMMAND_LIST_H\n\n")
    command_h_file.write("\n\n")

    for command, value in command_list:

        # we need to identify the type of value, then convert it to either a "char", or  a number. #
        print("Type of incoming value")
        print(type(value))
        if(type(value) == bytes):
            value_str = str(value)
            value_str = value_str[1:]       # removes the b added as a first character to indicate is a bytes type in python.
            print(value_str)


        command_h_file.write("const char " + command + " = " + value_str + ";\n")


    command_h_file.write('\n')
    command_h_file.write("#endif\n\n")


    command_h_file.close()

    print("FINISHED")

