from django.core.management.base import BaseCommand, CommandError
from culturehub.places.models import Restaurant
import geojson

class Command(BaseCommand):
    args = '<>'
    help = 'Generates GeoJSON for restaurant'

    def handle(self, *args, **options):
        res = []
        for r in Restaurant.objects.filter(lat__isnull=False):
            res.append(make_dict(r))

        print res


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
