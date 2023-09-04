#! /usr/local/bin/env python3.4

""" gunicorn config file """

import multiprocessing

bind = "10.70.60.105:8080"
workers = multiprocessing.cpu_count() * 2 + 1
pidfile = '/tmp/gunicorn.pid'
__author__ = "moonmoonbird"
__copyright__ = "Copyright 2015 , The TeenkerOperations Project"
__version__ = "1.0.1"
__maintainer__ = "guanling"
__email__ = "cuimianshiguanling@gmail.com"
__status__ = "Development"
