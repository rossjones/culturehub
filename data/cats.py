#!/usr/bin/env python
import os
import re
import sys
import requests
import calendar

import lxml.etree
"""
for filename in os.listdir('categories'):
    with open('categories/' + filename, 'r') as f:
        cat_id = int(filename[:-4])
        doc = lxml.etree.fromstring(f.read())

        items = doc.xpath('//item')
        for item in items:
            event_id = int(item.xpath('./event_id')[0].text)
            print "INSERT INTO events_event_categories(category_id, event_id) VALUES (%d,%d);" % (cat_id, event_id)

"""


items = [(3, "Craft"),
(310, "Tour De France"),
(12, "Exhibitions"),
(212, "Fair"),
(16, "Film"),
(17, "Food & Drink"),
(18, "Heritage"),
(8, "Literature"),
(223, "Market"),
(43, "Museum"),
(5, "Music"),
(2, "Performance"),
(13, "Outdoor"),
(7, "Social"),
(14, "Sport"),
(1, "VisualArt"),
(11, "Workshop"),
(9, "Festival"),]

url = "http://api.leedsinspired.co.uk/1.0/events.xml?key={0}&category_id=%s&start_date=01-%s-2013&end_date=%s-%s-2013".format(sys.argv[1])

for m in range(1, 13):
    month = '{0}'.format(str(m).zfill(2))

    for id,title in items:
        rr = calendar.monthrange(2013, m)
        u = url % (id, month,rr[1], month,)
        r = requests.get(u)

        if r.status_code == 200:
            doc =lxml.etree.fromstring(r.content)
            c = len(doc.xpath('//item'))
            print "%s,%s,%s" % (title, calendar.month_name[m], c)
        else:
            print 'Failed - ', id, month, r.status_code
            print u
            sys.exit(0)

