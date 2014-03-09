#!/usr/bin/env python
import sys
import lxml.etree
import json

def create_dict(item):
    add1 = item.xpath('./AddressLine1')
    add1 = add1[0].text if add1 else ""
    add2 = item.xpath('./AddressLine2')
    add2 = add2[0].text if add2 else ""
    pc = item.xpath('./PostCode')
    pc = pc[0].text if pc else ""

    address = "%s,%s,%s" % (add1, add2, pc)

    lat = item.xpath('./Geocode/Latitude')
    lat = lat[0].text if lat else None

    lon = item.xpath('./Geocode/Longitude')
    lon = lon[0].text if lon else None

    hrating = 0
    srating = 0
    mrating = 0
    scores = item.xpath('./Scores')
    if scores:
        hrating = item.xpath('./Scores/Hygiene')
        hrating = hrating[0].text if hrating else 0

        srating = item.xpath('./Scores/Structural')
        srating = srating[0].text if srating else 0

        mrating = item.xpath('./Scores/ConfidenceInManagement')
        mrating = mrating[0].text if mrating else 0

    if hrating == 'Exempt':
        hrating = 0
    if srating == 'Exempt':
        rating = 0
    if mrating == 'Exempt':
        mrating = 0

    rating = item.xpath('./RatingValue')
    rating = rating[0].text if rating else 0
    if rating == 'Exempt':
        rating = 0

    return {
        'model': 'places.restaurant',
        'pk': item.xpath('./FHRSID')[0].text,
        'fields': {
            "name": item.xpath('./BusinessName')[0].text,
            "address": address,
            "rating": rating,
            "hygiene_rating": hrating,
            "structural_rating": srating,
            "management_rating": mrating,
            "lat": lat,
            "long": lon,
        }
    }


res = []
doc = lxml.etree.fromstring(open("food-hygiene-leeds.xml", "r").read())
for node in doc.xpath("//EstablishmentDetail"):
    res.append(create_dict(node))

json.dump(res, sys.stdout)

"""
<EstablishmentDetail>
    <FHRSID>321605</FHRSID>
    <LocalAuthorityBusinessID>06/00739/COMM</LocalAuthorityBusinessID>
    <BusinessName>114 The Arch Restaurant</BusinessName>
    <BusinessType>Restaurant/Cafe/Canteen</BusinessType>
    <AddressLine1>114 Richardshaw Lane</AddressLine1><AddressLine2>Stanningley</AddressLine2>
    <AddressLine3>Pudsey</AddressLine3><AddressLine4>Leeds</AddressLine4>
    <PostCode>LS28 6BN</PostCode>
    <RatingValue>4</RatingValue>
    <RatingKey>fhrs_4_en-GB</RatingKey><RatingDate>2014-01-20</RatingDate>
    <LocalAuthorityCode>413</LocalAuthorityCode><LocalAuthorityName>Leeds</LocalAuthorityName>
    <LocalAuthorityWebSite>http://www.leeds.gov.uk/</LocalAuthorityWebSite>
    <LocalAuthorityEmailAddress>food.safety@leeds.gov.uk</LocalAuthorityEmailAddress>
    <Scores>
        <Hygiene>5</Hygiene>
        <Structural>10</Structural>
        <ConfidenceInManagement>5</ConfidenceInManagement>
    </Scores>
    <Geocode>
        <Longitude>-1.66545500000000</Longitude>
        <Latitude>53.80284000000000</Latitude>
"""