#!/usr/bin/env python3

__author__ = "Md. Minhazul Haque"
__license__ = "GPLv3"

"""
Copyright (c) 2019 Md. Minhazul Haque
This file is part of mdminhazulhaque/bd-mrp-api
(see https://github.com/mdminhazulhaque/banglalionwimaxapi).
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import print_function, absolute_import, division

import logging
import json

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
from helper import xpath_get, mode_dir, mode_file

if not hasattr(__builtins__, 'bytes'):
    bytes = str

class JSONFuse(LoggingMixIn, Operations):
    def __init__(self, jsonfile):
        try:
            logging.error(jsonfile)
            with open(jsonfile, "r") as fp:
                self.files = json.load(fp)
        except:
            raise Exception("JSON file could not be parsed")
        self.fd = 1
        
    def read(self, path, size, offset, fh):
        """
        Use xpath style access to JSON
        for example,
        
        d = {"foo":{"bar":"hello"}}
        p = "/foo/bar"
        
        xpath_get(d, p) will return "hello"
        
        encoding is necessary to read full bytes
        """
        children = xpath_get(self.files, path)
        if type(children) == str:
            end = offset + min(len(children), size)
            content = str(children)[offset:end].encode('utf-8')
            return content

    def readdir(self, path, fh):
        """
        for object, return keys
        for key, return value
        """
        ret = ['.', '..']
        if path == "/":
            ret += list(self.files.keys())
        else:
            children = xpath_get(self.files, path)
            try:
                ret += list(children.keys())
            except:
                pass
        return ret

    def getattr(self, path, fh=None):
        """
        if object, return mode_dir
        if key, return mode_file
        """
        children = xpath_get(self.files, path)
        if type(children) == str:
            mode = mode_file()
            # return the length of string as filesize
            mode['st_size'] = len(children)
            return mode
        return mode_dir()
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile')
    parser.add_argument('mount')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    fuse = FUSE(JSONFuse(args.jsonfile), args.mount, foreground=True, allow_other=False)
