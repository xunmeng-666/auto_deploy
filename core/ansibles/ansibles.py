# -*- coding:utf-8-*-
#!/usr/local/bin/python


import os
import json
import logging
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase
from ansible.errors import AnsibleParserError



class AnsibleTaskResultCallback(CallbackBase):
    def __init__(self,*args):
        super(AnsibleTaskResultCallback,self).__init__(*args)
        self.ok = json.dumps({})
        self.fail = json.dumps({})
        self.unreachable = json.dumps({})
        self.playbook = ""
        self.no_host = False
        self.fails = []

    def v2_runner_on_ok(self, result,**kwargs):
        host = result._host

        logging.info(json.dumps({host.name:result._result},indent=4))


    def v2_runner_on_failed(self, result, ignore_errors=False,**kwargs):
        #执行失败的playbook日志
        host = result._host
        data = json.dumps({host:result._result},indent=4)
        self.fail = data
        print "failed",result


    def v2_runner_on_unreachable(self, result,**kwargs):
        #未能连接到playbook的日志
        host = result._host
        data = json.dumps({host:result._result},indent=4)
        self.unreachable = data
        self.fails.append('Connect to host fails: %s' %self.unreachable)

    def v2_playbook_on_play_start(self, play):
        #记录正在执行的playbook
        self.playbook_on_play_start(play.name)
        self.playbook = play.name

    def v2_playbook_on_no_hosts_matched(self):
        #未能匹配到任何playbook， 不执行任何操作
        self.playbook_on_no_hosts_matched()
        self.no_host = True
        logging.info(LOG_INFO= "No_Host:%s" %self.no_host,LOG_LEVEL= logging.WARNING)

class AnsibleTask:
    def __init__(self, hosts_list, extra_vars=None):
        self.hosts_file = hosts_list
        Options = namedtuple('Options',
                             ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                              'diff', 'host_key_checking', 'listhosts', 'listtasks', 'listtags', 'syntax'])
        self.options = Options(connection='ssh', module_path=None, forks=10,
                               become=None, become_method=None, become_user=None, check=False, diff=False,
                               host_key_checking=False, listhosts=None, listtasks=None, listtags=None, syntax=None)
        self.loader = DataLoader()
        self.passwords = dict(vault_pass='secret')

        self.inventory = InventoryManager(loader=self.loader, sources=[self.hosts_file])
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        if extra_vars:
            self.variable_manager.extra_vars = extra_vars
            logging.info('variable111',self.variable_manager.extra_vars)

    def exec_playbook(self, playbooks):
        if not os.path.exists(playbooks[0]):
            logging.error('not fund playbook')
            code = 1000
            complex = {"playbook":playbooks,'msg':playbooks +"playbook does not exist",'flag':False}
            simple = 'playbook does not exist about' + playbooks
            return code,complex,simple
        results_callback = AnsibleTaskResultCallback()
        playbook = PlaybookExecutor(playbooks=playbooks, inventory=self.inventory,
                                    variable_manager=self.variable_manager,
                                    loader=self.loader, options=self.options, passwords=self.passwords)
        setattr(getattr(playbook, '_tqm'), '_stdout_callback', results_callback)
        try:
            playbook.run()
        except AnsibleParserError as e:
            print 'Error: %s' %e


def run_ansi(playbook,inventory):
    task = AnsibleTask(hosts_list=inventory)
    task.exec_playbook([playbook])

