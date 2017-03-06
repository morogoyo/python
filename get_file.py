#! usr/bin/env python
import urllib2
import json

url = 'http://ip.jsontest.com'

response = urllib2.urlopen(url)

html =  response.read()
print(html)
