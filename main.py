# -*- coding:utf-8-*-
import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PATH)
from core.config import *

from core.main import run
# from test import run

if __name__ == '__main__':
    playbook = os.path.join(ansible_file,'main.yaml')
    inventory = os.path.join(ansible_file,'inventory')
    print 'playbook',playbook
    print 'inventory',inventory
    run(playbook=playbook,inventory=inventory)
    # run()
