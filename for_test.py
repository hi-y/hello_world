#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import subprocess

class Ping(object):
    def __init__(self, hosts):
        for host in hosts:
            ping = subprocess.Popen(
                ["ping", "-c", "1", host],
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE
            )
            out, error = ping.communicate()
            if error:
                print('[NG]: ' + 'ServerName->' + host + ', Msg->\'' + error.rstrip() + '\'')
                raise PingError(error.rstrip())
            else:
                print('[OK]: ' + 'ServerName->' + host)

class TestFunctions(unittest.TestCase):
    def setUp(self):
        print 'setUp'

    def test1(self):
        print 'test1'

    def test2(self):
        print 'test2'

    def test3(self):
        print 'test3'

#    def test4(self):
#        r = 10 / 0

    def test5(self):
        r = 10 / 5
        print r

    def test_ping_to_localhost(self):
        hosts = [
            'localhost',
        ]
        Ping(hosts)

    def test_ping_to_gateway(self):
        hosts = [
            '192.168.0.1',
        ]
        Ping(hosts)

    def test_ping_to_www(self):
        hosts = [
            'www.google.com',
        ]
        Ping(hosts)

    def test8(self):
        hosts = [
            'www.yahoo.co.jp',
        ]
        Ping(hosts)



class PingError(Exception):
    pass

if __name__=='__main__':
    unittest.main()
