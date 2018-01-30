#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''Copyright (c) 2016, Ryo Hanafusa.
All rights reserved.'''

import os
import sys


class FileOperation(object):
    '''FileOperation'''
    def __init__(self):
        self._folder_path = os.path.abspath(os.path.dirname(__file__))
        self.filepath = ''
        self.loaded_file = None

    def make_filepath(self, filename):
        filepath = self._folder_path + '/' + filename
        return filepath

    def load_file(self, filename):
        self.filepath = self.make_filepath(filename)
        try:
            self.loaded_file = open(self.filepath, 'r+')
        except IOError:
            print >> sys.stderr, 'cannot open "%s"' % self.filepath
            sys.exit(1)
        finally:
            pass

    def readline(self):
        return self.loaded_file.readline().strip()

    def readlines(self):
        pass

    def update_content(self, content):
        try:
            self.loaded_file.seek(0)
            self.loaded_file.write(content)
            self.loaded_file.truncate()
        except IOError:
            print >> sys.stderr, 'cannot write to "%s"' % self.filepath
            sys.exit(1)
        finally:
            pass

    def update_contents(self, contents):
        pass

    def __del__(self):
        self.loaded_file.close()
        print 'Closing file ... Complete'
