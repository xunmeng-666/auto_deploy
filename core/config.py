# -*- coding:utf-8-*-
import os
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ansible_file = os.path.join(PATH,'ansible_files')
RABBITMQ = {
    "mq1":{
        "host":"10.211.55.100",
        "port":22,
        "username":"root",
        "password":"benet123```",
        "key_file": "",
        "config":{
            "rabbitmq_default_vhost":"ecscloud",
            "rabbitmq_default_user":"ecscloud",
            "rabbitmq_default_pass":"ecscloud",
        }
    },

}

REDIS = {
    "redis1":{
        "host":"10.211.55.100",
        "port":22,
        "username":"root",
        "password":"benet123```",
        "key_file": "",
        "config":{
            "REDIS_OPENAPI_DB":3,
            "REDIS_HOST":"10.211.55.100",
            "REDIS_PORT": 6379,
        }
    },

}

MEMCACHE = {
    "memcache1":{
        "host":"10.211.55.100",
        "port":22,
        "username":"root",
        "password":"benet123```",
        "key_file": "",

    },

}

MYSQL = {
    "mysql1":{
        "host":"10.211.55.100",
        "port":22,
        "username":"root",
        "password":"benet123```",
        "key_file": "",

    },
}

REGISTRY = {
    'registry' : {
        'host':"10.211.55.102",
        'port': 5555,
    }
}

VIP = {
    "vip1" :{
        "host":"10.211.55.100",
        "port":22,
        "username":"root",
        "password":"benet123```",
        "key_file":"",
    },
}
DOCKER = {
    "admin1" :{
        "host":"10.211.55.102",
        "port":22,
        "username":"root",
        "password":"benet123```",
        "key_file":"",
    }
}

MSGHANDLER = {
    "msghandler" :{
        "host":"10.211.55.100",
        "port":22,
        "username":"root",
        "password":"benet123```",
        "key_file":"",
    }
}
MOCK = {
    "os_mock1" :{
        "host":"10.211.55.101",
        "port":22,
        "username":"root",
        "password":"benet123```",
        "key_file":"",
    },
    "cs_mock1" :{
        "host":"10.211.55.101",
        "port":22,
        "username":"root",
        "password":"benet123```",
        "key_file":"",
    }

}

