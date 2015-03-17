#!/usr/bin/python env
import os
import string
import pexpect
import ssh_keygen
import sync_ssh_keys
import expect

if __name__ == '__main__':
    local_ips = os.popen('hostname -I').read()
    local_ip = local_ips.split()[0]
    
    host_list = "hadoop@10.239.131.160,luyuan@10.239.82.87,jiyou@10.239.82.96"
    hosts = map(string.strip, host_list.split(','))
    passwd_list = "hadoop,zaq12wsx,zaq12wsx"
    passwds = map(string.strip, passwd_list.split(','))
    host_passwd_pair = dict(zip(hosts, passwds))
    ssh_keygen.clean_env()
    for host in hosts:
        print "host:%s" % host
        print "scp files"
        ret_handle = pexpect.spawn('scp -r ssh_keygen.py sync_ssh_keys.py expect.py %s:/tmp/' %(host))
        expect.handle(ret_handle, ['yes/no', 'password'], ['yes', host_passwd_pair[host]])
        ret_handle.interact() 
        
        print "install pexpect"
        ret_handle = pexpect.spawn('ssh -t %s sudo yum install -y pexpect' % (host))
        expect.handle(ret_handle, ['password', 'sudo'], [host_passwd_pair[host], host_passwd_pair[host]])
        ret_handle.interact()
        
        print "exec ssh-keygen"
        ret_handle = pexpect.spawn('ssh -t %s python /tmp/ssh_keygen.py' % (host))
        expect.handle(ret_handle, ['password'], [host_passwd_pair[host]])
        ret_handle.interact()

        print "sync ssh keys"
        ret_handle = pexpect.spawn('ssh -t %s python /tmp/sync_ssh_keys.py %s %s' % (host, host_list, passwd_list))
        expect.handle(ret_handle, ['yes/no', 'password'], ['yes', host_passwd_pair[host]])
        ret_handle.interact()
        print "--------------------"

