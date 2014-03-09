#!/usr/bin/env python
import os
import sys
import json
import re
import lxml.etree
from datetime import datetime


data = []

doc = lxml.etree.fromstring(open('categories.xml').read())
items = doc.xpath('//item')
for item in items:
    d = {
        'model': 'categories.category',
        'pk': item.xpath('./category_id')[0].text,
        'fields': {
            'title': item.xpath('./category_title')[0].text,
            'interesting': False
        }
    }
    data.append(d)

doc = lxml.etree.fromstring(open('places.xml').read())
items = doc.xpath('//item')
for item in items:
    d = {
        'model': 'places.place',
        'pk': item.xpath('./place_id')[0].text,
        'fields': {
            'title': item.xpath('./place_title')[0].text,
            'description': item.xpath('./description')[0].text,
            'thumbnail':  item.xpath('./image_thumbnail')[0].text,
            'image':  item.xpath('./image_original')[0].text,
        }
    }
    data.append(d)


d1Match = re.compile('(.*) (.*) (.*) - (.*) (.*) (.*)')
d2Match = re.compile('(.*) (.*) (.*) (.*) - (.*)')
d3Match = re.compile('(.*) (.*) (.*)')
doc = lxml.etree.fromstring(open('events.xml').read())
items = doc.xpath('//item')
for item in items:

    success = False
    start_date = ''
    end_date = ''
    event_date = item.xpath('./event_date')[0].text
    m = d1Match.match(event_date)
    if m:
        start_date = datetime.strptime("%s %s %s" % (m.groups()[0],m.groups()[1],m.groups()[2]), "%d %b %Y")
        end_date = datetime.strptime("%s %s %s" % (m.groups()[3],m.groups()[4],m.groups()[5]), "%d %b %Y")
        success = True

    if not success:
        m = d2Match.match(event_date)
        if m:
            s = ' '.join(m.groups()[0:4])
            start_date = datetime.strptime(s.replace('am','AM').replace('pm','PM'), "%d %b %Y %I:%M%p")
            end_date = datetime.strptime("%s %s %s %s" % (m.groups()[0],m.groups()[1],m.groups()[2],m.groups()[4].upper()), "%d %b %Y %I:%M%p")
            success = True

    if not success:
        m = d3Match.match(event_date)
        if m:
            s = ' '.join(m.groups()).strip()
            try:
                start_date = datetime.strptime(s, "%d %b %Y")
                end_date = start_date
            except:
                start_date = datetime.strptime(s, "%d %b %Y %I:%M%p")
                end_date = start_date

            success = True

    if not success:
        from pdb import set_trace; set_trace()
    d = {
        'model': 'events.event',
        'pk': item.xpath('./event_id')[0].text,
        'fields': {
            'title': item.xpath('./event_title')[0].text,
            'description': item.xpath('./description')[0].text,
            'image_thumb':  item.xpath('./image_thumbnail')[0].text,
            'image':  item.xpath('./image_original')[0].text,
            'place': item.xpath('./place_id')[0].text,
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat()
        }
    }
    data.append(d)


"""
item>
<event_id><![CDATA[3868]]></event_id>
<event_title><![CDATA[Inkwell Arts Cafe: Eat, Drink, Create]]></event_title>
<description><![CDATA[Every Saturday you can enjoy delicious, home-cooked vegetarian food, homemade cakes, fresh coffee and a variety of other drinks.  Each week we have a variety of craft workshops for you to try, including batik, jewellery, upcycled crafts, pottery.

Sit and relax in our spacious gallery, surrounded by work from local artists, take advantage of free WiFi and, on sunnier days, enjoy our garden. We also have craft workshops and activities for children.

Cafe opening times 10 - 4 every Saturday
Workshop times are 10.30 to 12.30 and then 1.30 to 3.30

We will be expanding this service, in the near future and hope to offer you all this on a Sunday too!
More details can be found on our website http://www.inkwellarts.org.uk/saturday-cafe/ or if you have any enquiries, please get in touch!

Reviews:
 http://www.aboutmyarea.co.uk/site/content.asp?area=398&type=3&story=241215
http://theculturevulture.co.uk/blog/reviews/food-and-drink-reviews/inkwellcafe/
http://www.veggieplaces.co.uk/list_reviews.php?place_id=3745

]]></description>
<place_id><![CDATA[1614]]></place_id>
<place_title><![CDATA[Inkwell]]></place_title>
<organiser_id><![CDATA[3657]]></organiser_id>
<organiser_title><![CDATA[Inkwell Arts]]></organiser_title>
<event_date><![CDATA[6 Apr 2013 - 13 Dec 2014]]></event_date>
<image_thumbnail><![CDATA[http://www.leedsinspired.co.uk/sites/default/files/styles/190x190/public/images/events/3868.jpg]]></image_thumbnail>
<image_original><![CDATA[http://www.leedsinspired.co.uk/sites/default/files/images/events/3868.jpg]]></image_original>
</item>
"""

json.dump(data, sys.stdout)
