#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''


configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data',
        'db': 'awesome'
    },
    'session': {
        'secret': '\xc6\x7f\xdd\xc2\xfb\x87\xdeP\xe8\x9b\x14|\x08M\x9e$\xfe\x7f\xf1\n\xcf~\xf0\xf1'
    }
}