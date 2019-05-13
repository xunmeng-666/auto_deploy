#!/usr/bin/env bash
dir=$(pwd)
which pip
if [ $? -ne 0 ];then
    yum -y install epel-release
    yum install -y python2-pip
    pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com --upgrade pip
fi

which ansible
if [ $? -ne 0 ];then
#    pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com ansible==2.7.10
    yum install -y ansible-2.7.10-1.el7
fi
sed -i "s/#host_key_checking = False/host_key_checking = False/g" /etc/ansible/ansible.cfg

which sshpass
if [ $? -ne 0 ];then
    yum install -y sshpass
fi


python $dir/main.py
cd $dir/ansible_files/
ansible-playbook -i $dir/ansible_files/inventory $dir/ansible_files/mysql/mysql_sql.yaml
