#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''Copyright (c) 2016, Ryo Hanafusa.
All rights reserved.'''

from functools import wraps
from selenium import webdriver
import requests
import lxml.html

_GET_IMAGE_URL_TARGET_ID = 'imgItem'
_IMAGE_URLS_TARGET_CLASS = 'detailOn'
_NEXT_ARTICLE_TARGET_CLASS =\
    'skin-pagingPrev skin-btnPaging ga-pagingEntryPrevTop'


class AblogScrape(object):
    '''AblogScrape'''
    def __init__(self):
        self.driver =\
            webdriver.PhantomJS(service_log_path='/tmp/ghostdriver.log')
        self.latest_article = ''
        self.target_article = ''
        self.next_article = ''
        self.new_latest_article = ''
        self._a_tags = None

    def _checker(self):
        print self.latest_article
        print self.target_article
        print self.next_article
        print self.new_latest_article

    def _decorator(explain):
        def _deco(function):
            @wraps(function)
            def __deco(*args, **kw):
                print '==>', explain, '\n\t',
                function(*args, **kw)
                print
            return __deco
        return _deco

    def _a_tag_parse(self):
        target_html = requests.get(self.target_article).text
        root = lxml.html.fromstring(target_html)
        self._a_tags = root.cssselect('a')

    def get_new_latest_article(self):
        return self.new_latest_article

    @_decorator('Latest article:')
    def set_latest_article(self, latest_article):
        self.latest_article = latest_article
        print self.latest_article

        self.target_article = self.latest_article
        self._a_tag_parse()
        self.next_article = self.get_next_article()

    @_decorator('Target article:')
    def update_target_article(self, next_article):
        self.target_article = next_article
        print self.target_article
        self._a_tag_parse()

    @_decorator('Updated new latest article:')
    def set_new_latest_article(self, target_article):
        self.new_latest_article = target_article
        print self.new_latest_article

    def _get_image_url(self, target_url):
        self.driver.get(target_url)
        root = lxml.html.fromstring(self.driver.page_source)
        img_tags = root.cssselect('img')
        for img_tag in img_tags:
            if img_tag.attrib['id'] == _GET_IMAGE_URL_TARGET_ID:
                return img_tag.attrib['src']

    def get_image_urls(self):
        print 'Getting image URLs'
        img_urls = []
        print '==>', 'Making a list of image URL'
        for a_tag in self._a_tags:
            conditions = [('class' in a_tag.attrib),
                          ('href' in a_tag.attrib)]
            if all(_ for _ in conditions):
                if a_tag.attrib['class'] == _IMAGE_URLS_TARGET_CLASS:
                    img_url = self._get_image_url(a_tag.attrib['href'])
                    img_urls.append(img_url)
        return img_urls

    def get_next_article(self):
        print 'Getting the next article'
        next_article = ''
        for a_tag in self._a_tags:
            conditions = [('class' in a_tag.attrib),
                          ('href' in a_tag.attrib)]
            if all(_ for _ in conditions):
                if a_tag.attrib['class'] == _NEXT_ARTICLE_TARGET_CLASS:
                    next_article = a_tag.attrib['href']
                    break
        return next_article

    def main_scrape(self):
        while self.next_article is not '':
            self.update_target_article(self.next_article)
            image_urls = self.get_image_urls()
            yield image_urls
            self.next_article = self.get_next_article()
            # self._checker()
        self.set_new_latest_article(self.target_article)
