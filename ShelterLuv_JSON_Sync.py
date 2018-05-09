# ShelterLuv sync to local Dallas Pets Alive filesystem script
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import requests
import collections
import json
import operator
from Local_Defines import API_KEY, ANIMALS_FILE
from Dog_Functions import parse_dogs
from Cat_Functions import parse_cats

# First fetch the entire list of animals

headers = {'x-api-key': API_KEY}
offset = 0
animals_dict = {}
total_count = 0

while 1:
    url = 'https://www.shelterluv.com/api/v1/animals?status_type=publishable&offset=' + str(offset)
    print 'fetching ' + url
    response = requests.get(url, headers=headers)

    # check http response code
    if response.status_code != 200:
        print 'invalid response code'
        exit(1)

    response_json = response.json()

    if response_json["success"] != 1:
        print 'invalid attempt'
        exit(2)

    total_count = response_json["total_count"]

    if total_count == 0:
        print 'no animals found - error'
        exit(3)

    # add each animal to the dict
    for animal in response_json["animals"]:
        ID = animal["ID"]
        if ID in animals_dict:
            print 'animal already exists'
            continue

        animals_dict[ID] = animal

    # check for more animals
    if response_json["has_more"]:
        offset += 100
    else:
        break

# we should have all the animals now
if str(animals_dict.__len__()) != str(total_count):
    print 'something went wrong, missing animals'

# write animals out to file for searching later
with open(ANIMALS_FILE, 'w') as animals_file_obj:
    animals_file_obj.write(json.dumps(animals_dict))

# sort the list of animals by name
name_dict = {}
for animal in animals_dict:
    name_dict[animal] = animals_dict[animal]["Name"]
ordered_names = collections.OrderedDict(sorted(name_dict.items(), key=operator.itemgetter(1)))

ordered_animals = collections.OrderedDict()
for animal in ordered_names:
    ordered_animals[animal] = animals_dict[animal]

# parse the dogs
parse_dogs(ordered_animals)

# parse the cats
parse_cats(ordered_animals)

