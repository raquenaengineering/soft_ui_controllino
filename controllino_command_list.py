


"""
To be able to synchronize easily any changes in the communication between the controllino and the UI,
- The command list will be implemented as a separate file.
- A script that autogenerates the expected commands on the firmware side will be created.
- The output of the script will be copied to the folder where the firmware is compiled (as a source file)
- So, it can be read and compiled with the firmware everytime there is a change.

ui side: controllino_command_list.py
    - class with a lot of variables?
        - probably best option
firmware side: command_list.cpp
    - defines
    - const chars? --> probably this option better.
"""

class controllino_command_list():


    pin_d0_hi_cmd = b'+'
    pin_d0_lo_cmd = b'*'

    pin_d1_hi_cmd = b'1'
    pin_d1_lo_cmd = b'!'

    pin_d2_hi_cmd = b'2'
    pin_d2_lo_cmd = b'"'

    pin_d3_hi_cmd = b'3'
    pin_d3_lo_cmd = b'-'            # problematic, not an ASCII character.






    request_inputs_cmd = '-'

    def __init__(self):             # not needed, this class is just a variable container.
        pass


if __name__ == "__main__":
    # ccl = controllino_command_list()
    # for param in vars(ccl):
    #     print(param)

    for param in vars(controllino_command_list):
        print(param)