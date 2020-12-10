#!/usr/bin/env python3
#create a list of strings

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across the list called farms
for x in farms:
    print(f"The {x['name']} has: {x['agriculture']}")
    print(f"The {x['name']} has:")
    for ag in farm['agriculture']:
        print(f"    {ag}")
