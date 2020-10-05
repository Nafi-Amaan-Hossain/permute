import string
import time
import sys

def cracker(passarg):
    starttime = time.time()
    chars = ['#','@','$','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password_buffer = ""

    for x in string.ascii_letters:
        chars += x

    for x in string.digits:
        chars += x

    password = passarg
    print('[*]Started to crack at: %s, this may take a while....\r' %(starttime))

    for a1 in chars:
        password_buffer += a1
        if password_buffer == password:
            print('Password is: ' , password_buffer); sys.exit;
        for a2 in chars:
            password_buffer += a2
            if password_buffer == password:
                print('Password is: ' , password_buffer); sys.exit;
            for a3 in chars:
                password_buffer += a3
                if password_buffer == password:
                    print('Password is: ' , password_buffer); sys.exit;
                for a4 in chars:
                    password_buffer += a4
                    if password_buffer == password:
                        print('Password is: ' , password_buffer); sys.exit;
                    for a5 in chars:
                        password_buffer += a5
                        if password_buffer == password:
                            print('Password is: ' , password_buffer); sys.exit;
                        for a6 in chars:
                            password_buffer += a6
                            if password_buffer == password:
                                print('Password is: ' , password_buffer); sys.exit;
                            for a7 in chars:
                                password_buffer += a7
                                if password_buffer == password:
                                    print('Password is: ' ,password_buffer); sys.exit;
                                for a8 in chars:
                                    password_buffer += a8
                                    if a8 == password:
                                        print('Password is: ' ,password_buffer); sys.exit;
                                    for a9 in chars:
                                        password_buffer += a9
                                        if password_buffer == password:
                                            print('Password is: ' ,password_buffer); sys.exit;
                                        password_buffer = ''
