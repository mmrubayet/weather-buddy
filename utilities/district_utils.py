import os
import json

from django.conf import settings

from weathers.models import District


def import_districts():
    static_file_path = os.path.join(
        settings.STATIC_ROOT, 'data/bd-districts.json'
    )

    # Load data from the JSON file
    with open(static_file_path) as f:
        district = json.load(f)
    district_list = district.get("districts")
    for d in district_list:
        district = District.objects.create(
            dist_id=d.get("id"),
            division_id=d.get("division_id"),
            name=d.get("name"),
            bn_name=d.get("bn_name"),
            lat=d.get("lat"),
            long=d.get("long"),
        )
    return 'done'
