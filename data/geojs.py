#!/usr/bin/env python
import geojson

def make_dict(restaurant):
    pt = geojson.Point([restaurant.lat, restaurant.long])


    return {
        "type": "Feature",
        "properties": {
            "name": restaurant.name,
            "rating": restaurant.rating,
            "popupContent": "%s (%s)" % (restaurant.name, restaurant.rating)
        },
        "geometry": geojson.dumps(pt)
    }

"""
 {
    "type": "Feature",
    "properties": {
        "name": "Coors Field",
        "amenity": "Baseball Stadium",
        "popupContent": "This is where the Rockies play!"
    },
    "geometry": {
        "type": "Point",
        "coordinates": [-104.99404, 39.75621]
    }
};

"""