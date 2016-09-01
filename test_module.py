#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'flyghost'


class Student(object):
    def __init__(self, s_name, score):
        self.name = s_name
        self.score = score

    def print_score(self):
        print('name:%s, score:%d' % (self.name, self.score))
