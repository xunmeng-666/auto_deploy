# -*- coding:utf-8-*-
import config
import os

PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print 'PATH',PATH
class InventoryCreate(object):
    def __init__(self):
        path = os.path.join(PATH,'ansible_files')
        self.inventory = os.path.join(path,'inventory')
        self.group_list = []



    def run(self):
        if os.path.exists(self.inventory):
            os.remove(self.inventory)
        for k,v in config.__dict__.items():
            if type(v) == dict:
                for k1,v1 in v.items():
                    if type(v1) == dict:
                        db = v
                        self.write_inventory(db)


    def write_inventory(self,db):
        group_vars = []
        master = []
        slave = []

        for index,hostname in enumerate(db):
            group_name = hostname[:-1]
            group_vars.append(db[hostname]['host'])
            if index == 0:
                group_master = "%s_master" % group_name
                self.group_list.append(group_name)
                master.append(self.msg(db[hostname], hostname=hostname))
            else:
                group_slave = "%s_slave" % group_name
                slave.append(self.msg(db[hostname], hostname=hostname))


        with open(self.inventory,'a') as f:

            try:
                f.write("\n[%s:children]\n%s\n%s\n" %(group_name,group_master,group_slave))
            except UnboundLocalError:
                f.write("\n[%s:children]\n%s\n" %(group_name,group_master))
            f.write("\n[%s:vars]\n" %group_name)
            for index,var in enumerate(group_vars):
                f.write("\nnode%s=%s\n" %(index,var))
            f.write("\n[%s]\n" %group_master)
            for info in master:
                f.write(info)
            try:
                f.write("\n[%s]\n" % group_slave)
                for info in slave:
                    f.write(info)
            except UnboundLocalError:
                pass

        f.close()

    def msg(self,dict,hostname=None):
        if hostname:
            try:
                msgs = '''
%s ansible_ssh_host=%s ansible_ssh_port=%s ansible_ssh_user=%s ansible_ssh_pass=%s
''' %(hostname,dict['host'],dict['port'],dict['username'],dict['password'])
            except KeyError:
                msgs = '''
%s ansible_ssh_host=%s ansible_ssh_port=%s ''' % (hostname, dict['host'], dict['port'])

        else:
            msgs = '''
ansible_ssh_host=%s ansible_ssh_port=%s ansible_ssh_user=%s ansible_ssh_pass=%s
''' % (dict['host'], dict['port'], dict['username'], dict['password'])

        return msgs

if __name__ == '__main__':
    InventoryCreate().run()
    exit(0)