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

from stat import S_IFDIR, S_IFREG
from time import time

def xpath_get(mydict, path):
    elem = mydict
    try:
        for x in path.strip("/").split("/"):
            elem = elem.get(x)
    except:
        pass
    return elem

def mode_file():
    return dict(
        st_mode=(S_IFREG | 0o400),
        st_size=0,
        st_ctime=time(),
        st_mtime=time(),
        st_atime=time()
    )

def mode_dir():
    return dict(
        st_mode=(S_IFDIR | 0o400),
        st_nlink=1,
        st_ctime=time(),
        st_mtime=time(),
        st_atime=time()
    )

if __name__ == "__main__":
    pass
