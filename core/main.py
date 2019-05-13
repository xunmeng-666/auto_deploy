# -*- coding:utf-8-*-

import paramiko
from config import *
from create_inventory import InventoryCreate
from ansibles.ansibles import run_ansi

def shelld():

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
    for host in DOCKER:
        s = ssh.connect(hostname=DOCKER[host]['host'],port=DOCKER[host]['port'],
                        username=DOCKER[host]['username'],password=DOCKER[host]['password'])
        print '登录到主机：%s' %DOCKER[host]['host']

        _,stdout,stderr = ssh.exec_command("cd /tmp/docker-compose/ && sh docker_sql.sh" )
        for line in stdout:
            print line.strip("\n")

        err = stderr.read()
        if len(err) > 0:
            print 'Err\n%s' % err
    ssh.close()

def run(playbook,inventory):
    create_inventory()
    run_ansible(playbook,inventory)
    shelld()

def run_ansible(playbook,inventory):
    os.system('ansible-playbook -i %s %s' %(inventory,playbook))

def create_inventory():
    InventoryCreate().run()

if __name__ == '__main__':
    shelld()
    exit(0)


