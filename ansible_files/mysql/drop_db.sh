#!/usr/bin/env bash
mysql -uroot -pmysql123 -se "
drop database yj_manage;
drop database yj_workorder;
drop database yj_admin;
drop database yj_vip;
drop database yj_mock;
"