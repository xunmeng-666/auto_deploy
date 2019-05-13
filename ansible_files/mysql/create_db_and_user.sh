#!/usr/bin/env bash

mysql -se "
create database  yj_manage character set utf8;
create database  yj_workorder character set utf8;
create database  yj_admin character set utf8;
create database  yj_vip character set utf8;
create database  yj_mock character set utf8;

GRANT all privileges on *.* to test@'%' identified by 'test123';
GRANT all privileges on *.* to test@localhost identified by 'test123';
"
