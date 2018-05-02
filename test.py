#!/usr/bin/env python
# coding=utf-8
file =open('res.4');
for line in file:
    if float(line)>10000:
        print line
