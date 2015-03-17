#!/usr/bin/python env
import pexpect

def handle(exe, expect_list, send_list):
    if len(expect_list) != len(send_list):
        print "Error:expect list is not equal list"
        return
    expect_list += [pexpect.TIMEOUT, pexpect.EOF]
    while True:
        index = exe.expect(expect_list)
        if len(expect_list) - 1  == index:
            break 
        elif len(expect_list) - 2 == index:
            continue 
        else:
            exe.sendline(send_list[index])

