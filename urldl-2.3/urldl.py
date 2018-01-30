#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''Copyright (c) 2016, Ryo Hanafusa.
All rights reserved.'''

from functools import wraps
import shutil
import requests

import settings as _STG


class URLDownload(object):
    '''URLDownload Class'''
    def __init__(self):
        self._savepath = ''

    def _decorator(explain):
        def _deco(function):
            @wraps(function)
            def __deco(*args, **kw):
                special = ['generator', 'list']
                if any(spc in function.__name__ for spc in special):
                    print explain, '\n',
                else:
                    print '==>', explain, '\n\t',
                function(*args, **kw)
            return __deco
        return _deco

    @_decorator('Savepath')
    def load_savepath(self, savepath=_STG.SAVEPATH):
        if savepath[-1] is not "/":
            savepath += "/"
        self._savepath = savepath
        print self._savepath

    @_decorator('Downloading')
    def download(self, url):
        print url
        res = requests.get(url, stream=True)
        filename = url.split('/')[-1]
        filepath = self._savepath + filename
        with open(filepath, 'wb') as fobj:
            shutil.copyfileobj(res.raw, fobj)

    @_decorator('Downloading with list')
    def list_download(self, urls):
        for url in urls:
            self.download(url)

    def _generator_download(self, urls):
        for url in urls:
            self.download(url)
            yield

    @_decorator('Downloading with generator')
    def generator_download(self, urls):
        dls = self._generator_download(urls)
        for _ in range(len(urls)):
            dls.next()
