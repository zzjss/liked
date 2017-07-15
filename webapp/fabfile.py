#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os,re
from datetime import datetime

from fabric.api import *

env.user='zzjss'

env.sudo_user='root'

env.hosts=['182.61.22.192']

db_user = 'www-data'
db_password = 'www-data'

_TAR_FILE = 'dist-webapp.tar.gz'

def build():
    includes = ['static','templates','transwarp','favicon.ocp','*.py']
    excludes = ['test', '.*','*.pyc','*.pyo']
    local('rm -f dist/%s' % _TAR_FILE)
    with lcd(os.pqth.join(os.path.abspath('.'), 'www')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=/'%s/''% ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))
		
_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
_REMOTE_BASE_DIR = '/srv/awesome'

def deploy():
    newdir = 'www-%s' % datetime.now().strftime('%y-%m-%d_%H.%M.%S')
    # 删除已有的tar文件:
    run('rm -f %s' % _REMOTE_TMP_TAR)
    # 上传新的tar文件:
    put('dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    # 创建新目录:
    with cd(_REMOTE_BASE_DIR):
        sudo('mkdir %s' % newdir)
    # 解压到新目录:
    with cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    # 重置软链接:
    with cd(_REMOTE_BASE_DIR):
        sudo('rm -f www')
        sudo('ln -s %s www' % newdir)
        sudo('chown www-data:www-data www')
        sudo('chown -R www-data:www-data %s' % newdir)
    # 重启Python服务和nginx服务器:
    with settings(warn_only=True):
        sudo('supervisorctl stop awesome')
        sudo('supervisorctl start awesome')
        sudo('/etc/init.d/nginx reload')