# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import re
import functools
import os
import sys
import urllib

import requests


SRC_DIR = '../raw'
DST_DIR = '../content'


class Blog(object):
    
    def __init__(self, file_name, src_dir_name, dst_dir_name, input_encoding='utf-8', output_encoding='utf-8'):
        self.src_file_path = src_dir_name + '/' + file_name
        self.file_name = file_name
        # self.src_dir_name = src_dir_name
        self.dst_dir_name = dst_dir_name
        self.input_encoding = input_encoding
        self.output_encoding = output_encoding

        self.title = None
        self.slug = None
        self.category = None
        self.category_en = None
        self.static_dir_name = None

    def get_create_time(self):
        stat_info = os.stat(self.src_file_path)
        return datetime.datetime.fromtimestamp(stat_info.st_ctime)

    def convert(self):
        content = ''
        with open(self.src_file_path, 'r') as f:
            for line in f:
                if self.input_encoding:
                    line = line.decode(self.input_encoding)
                content += self._convert_to_pelican(line)

        if self.output_encoding:
            content = content.encode(self.output_encoding)

        category = '/' + self.category if self.category else ''
        dst_file_path = self.dst_dir_name + category + '/' + self.file_name
        if not os.path.exists(os.path.dirname(dst_file_path)):
            os.makedirs(os.path.dirname(dst_file_path))
        with open(dst_file_path, 'w') as f:
            f.write(content)

        return content

    def _download(self, url):
        # print url
        if not os.path.exists(self.static_dir_name):
            os.makedirs(self.static_dir_name)

        file_name = os.path.basename(url)

        path = self.static_dir_name + '/' + file_name
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
        return os.path.relpath(path, self.dst_dir_name)

    def _convert_to_pelican(self, line):
        """
            Title: My super title
            Date: 2010-12-03 10:20
            Modified: 2010-12-05 19:30
            Category: Python
            Tags: pelican, publishing
            Slug: my-super-post
            Authors: Alexis Metaireau, Conan Doyle
            Summary: Short version for index and feeds

            {filename}/images/han.jpg
        """
        line = line.replace('\t', ' '*4)

        title_regexp = re.compile(r'^# (?P<title>.*)\s*\n')
        slug_regexp = re.compile(r'^<!-- Slug\:\s*(?P<slug>[\w\-_]+) -->\s*\n')
        category_regexp = re.compile(r'^<!-- Category\:\s*(?P<category>.+) -->\s*\n')
        code_block_regexp = re.compile(r'(\s*)<!-- (?P<lang>:::\w+) -->\s*\n')
        image_regexp = re.compile(r'!\[(.*)\]\((?P<url>.*)\)')

        # 标题
        m = title_regexp.match(line)
        if m:
            title = m.groupdict()['title']
            self.title = title
            create_time = self.get_create_time().strftime('%Y-%m-%d %H:%M:%S')
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            new_content = 'Title: {title}\nDate: {date}\nModified: {modified}\n'.format(
                title=title, 
                date=create_time,
                modified=now
            )
            return new_content

        # Slug
        m = slug_regexp.match(line)
        if m:
            slug = m.groupdict()['slug']
            category_en = '/' + self.category_en if self.category_en else ''
            # print category_en
            self.static_dir_name = self.dst_dir_name + '/images' + category_en + '/' + slug
            self.slug = slug
            new_content = 'Slug: ' + slug + '\n'
            return new_content

        # 分类
        m = category_regexp.match(line)
        if m:
            category = m.groupdict()['category'].split('/')
            self.category = category[0]
            if len(category) > 1:
                self.category_en = category[1]
            new_content = 'Category: ' + self.category + '\n'
            return new_content

        # 代码块
        m = code_block_regexp.match(line)
        if m:
            new_content = m.group(1) + ' '*4 + m.groupdict()['lang'] + '\n'
            return new_content

        # 图片引用
        m = image_regexp.match(line)
        if m:
            url = m.groupdict()['url']
            path = self._download(url)
            new_content = line.replace(url, '{filename}/'+path)
            return new_content

        return line

    def convert_to_ghost(text):
        pass

    def __repr__(self):
        return str(self.__dict__)


if __name__ == '__main__':
    for obj in os.listdir(SRC_DIR):
        if obj.endswith('.md'):
            b = Blog(obj, SRC_DIR, DST_DIR, input_encoding='utf-8', output_encoding='utf-8')
            b.convert()
            print b
