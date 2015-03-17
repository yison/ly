#!/usr/bin/env python
import os
import sys
import string
import pexpect

def sync(host_list, host_passwd_pair):
    for host in host_list:
        ret = pexpect.spawn('ssh-copy-id %s' % host)
        
        while True:
            index = ret.expect(['yes/no', 'password', pexpect.EOF, pexpect.TIMEOUT])
            if 0 == index:
                ret.sendline('yes')
            elif 1 == index:
                ret.sendline(host_passwd_pair[host])
            elif 2 == index:
                break
            elif 3 == index:
                print ret.before()
                continue
            

if __name__ == "__main__":
    hosts = map(string.strip, sys.argv[1].split(','))
    passwds = map(string.strip, sys.argv[2].split(','))
    host_passwd_pair = dict(zip(hosts, passwds))
    print hosts
    print host_passwd_pair
    sync(hosts, host_passwd_pair)
