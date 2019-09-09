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

import json
import os

if __name__ == '__main__':
    
    data = {}
    base = "../country-json/src/"
    
    def load_info(filename, key):
        with open(base +  filename, "r") as fp:
            j = json.load(fp)
            for i in j:
                country = i['country']
                value = i[key]
                try:
                    data[country][key] = value
                except:
                    data[country] = {}
                    data[country][key] = value
                
    load_info("country-by-capital-city.json", "city")
    load_info("country-by-population.json", "population")
    load_info("country-by-calling-code.json", "calling_code")
    load_info("country-by-continent.json", "continent")
    load_info("country-by-domain-tld.json", "tld")
    
    with open("countries.json", "w") as fp:
        json.dump(data, fp, indent=4)
    
