#!/usr/bin/python env
import os
import pexpect

def clean_env():
    os.system('rm -rf ~/.ssh/*') 

def auto_generate():
    ret_str = pexpect.spawn('ssh-keygen')
    ret_str.expect('Enter file in which to save the key*')
    ret_str.sendline('\n')
    ret_str.expect('Enter passphrase')
    ret_str.sendline('\n')
    ret_str.expect('Enter same passphrase again*')
    ret_str.sendline('\n')
    ret_str.terminate()

if __name__ == "__main__":
    clean_env()
    auto_generate()
