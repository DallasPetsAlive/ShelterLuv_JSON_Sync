# ShelterLuv sync to local Dallas Pets Alive filesystem script
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import requests
import collections
import json
import logging
import operator
from local_defines import (
    API_KEY,
    ANIMALS_FILE,
    PROFILES_DIRECTORY,
    OTHER_LIST_FILE,
    DOG_LIST_FILE,
    CAT_LIST_FILE,
    HOMEPAGE_LIST_FILE,
    NEW_DIGS_DOG_LIST_FILE,
    NEW_DIGS_CAT_LIST_FILE,
    NEW_DIGS_PROFILES_DIRECTORY,
    NEW_DIGS_ANIMALS_FILE,
    AIRTABLE_API_KEY,
    AIRTABLE_BASE,
    PETS_FILE_KEY,
)
from common_functions import (
    parse_animal_profile,
    parse_new_digs_animal_profile,
    generate_homepage_pet_list,
    generate_pet_list,
    generate_new_digs_pet_list,
)
import os
import codecs

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# First fetch the entire list of animals
def shelterluv_sync():
    headers = {'x-api-key': API_KEY}
    offset = 0
    animals_dict = {}
    # total_count = 0

    while 1:
        url = (
            'https://www.shelterluv.com/api/v1/' +
            'animals?status_type=publishable&offset=' + str(offset)
        )
        # print 'fetching ' + url
        response = requests.get(url, headers=headers)

        # check http response code
        if response.status_code != 200:
            print('invalid response code')
            exit(1)

        response_json = response.json()

        if response_json["success"] != 1:
            print('invalid attempt')
            exit(2)

        total_count = response_json["total_count"]

        if total_count == 0:
            print('no animals found - error')
            exit(3)

        # add each animal to the dict
        for animal in response_json["animals"]:
            ID = animal["ID"]
            if ID in animals_dict:
                print('animal already exists')
                continue

            animals_dict[ID] = animal

        # check for more animals
        if response_json["has_more"]:
            offset += 100
        else:
            break

    # we should have all the animals now
    if str(animals_dict.__len__()) != str(total_count):
        print('something went wrong, missing animals')

    # write animals out to file for searching later
    with open(ANIMALS_FILE, 'w+') as animals_file_obj:
        animals_file_obj.write(json.dumps(animals_dict))

    # sort the list of animals by name
    name_dict = {}
    for animal in animals_dict:
        name_dict[animal] = animals_dict[animal]["Name"]
    ordered_names = collections.OrderedDict(
        sorted(name_dict.items(), key=operator.itemgetter(1))
    )

    ordered_animals = collections.OrderedDict()
    for animal in ordered_names:
        ordered_animals[animal] = animals_dict[animal]

    # get the homepage featured pets
    get_homepage_pets(animals_dict)

    # parse the profiles
    parse_profiles(ordered_animals)

    # create the pet lists
    parse_lists(ordered_animals)


# This function accepts the list of animals
# and generates profile pages for browser output
def parse_profiles(animals):
    output_file_list = []

    # get current list of animal pages
    profiles_current = os.listdir(PROFILES_DIRECTORY)

    # add the test file so it doesn't get deleted by the script
    output_file_list.append("1.php")

    for animal in animals:
        filename = animal + ".php"
        output_file_list.append(filename)

        with codecs.open(PROFILES_DIRECTORY + filename, 'w+') as pet_file:
            output = parse_animal_profile(animals[animal])
            pet_file.write(output)

    # delete stagnant pages
    for profile in profiles_current:
        if profile not in output_file_list:
            print("deleting " + PROFILES_DIRECTORY + profile)
            if os.path.isfile(PROFILES_DIRECTORY + profile):
                os.remove(PROFILES_DIRECTORY + profile)


def parse_lists(pets):
    dog_list = collections.OrderedDict()
    cat_list = collections.OrderedDict()
    other_list = collections.OrderedDict()

    # divide up the pets
    for pet in pets:
        if pets[pet]["Type"] == "Dog":
            dog_list[pet] = pets[pet]
        elif pets[pet]["Type"] == "Cat":
            cat_list[pet] = pets[pet]
        else:
            other_list[pet] = pets[pet]

    generate_pet_list(dog_list, DOG_LIST_FILE)
    generate_pet_list(cat_list, CAT_LIST_FILE)
    generate_pet_list(other_list, OTHER_LIST_FILE)


def get_homepage_pets(pets):
    # get a list of the 6 ID's that are longest stays
    longest_stays = {}

    for pet in pets:
        if len(longest_stays) < 6:
            longest_stays[pet] = pets[pet]["LastIntakeUnixTime"]
            continue
        max_pet = max(longest_stays, key=lambda key: longest_stays[key])
        max_pet_time = longest_stays[max_pet]
        if pets[pet]["LastIntakeUnixTime"] < max_pet_time:
            del longest_stays[max_pet]
            longest_stays[pet] = pets[pet]["LastIntakeUnixTime"]

    final_longest_stay_list = {}
    for pet in longest_stays:
        final_longest_stay_list[pet] = pets[pet]

    generate_homepage_pet_list(final_longest_stay_list, HOMEPAGE_LIST_FILE)


def new_digs_sync():
    # get new digs pets from airtable
    url = "https://api.airtable.com/v0/" + AIRTABLE_BASE + "/Pets"
    headers = {"Authorization": "Bearer " + AIRTABLE_API_KEY}

    offset = None
    quit = False
    pets_list = []

    while not quit:
        params = {}
        if offset:
            params = {
                "offset": offset
            }

        response = requests.get(url, headers=headers, params=params)
        if(response.status_code != requests.codes.ok):
            logger.error("Airtable response: ")
            logger.error(response)
            logger.error("URL: " + url)
            logger.error("Headers: " + str(headers))
            return

        airtable_response = response.json()

        if not airtable_response.get("offset"):
            quit = True
        else:
            offset = airtable_response["offset"]

        pets_list += airtable_response["records"]

    # write animals out to file for searching later
    with open(NEW_DIGS_ANIMALS_FILE, 'w+') as animals_file_obj:
        animals_file_obj.write(json.dumps(airtable_response))

    parse_new_digs_profiles(pets_list)


def parse_new_digs_profiles(pets):
    dog_list = []
    cat_list = []
    output_file_list = []
    # get current list of animal pages
    profiles_current = os.listdir(NEW_DIGS_PROFILES_DIRECTORY)

    for pet in pets:
        fields = pet["fields"]

        status = fields.get("Status")
        if status != "Published - Available for Adoption":
            continue

        id = fields.get("Pet ID - do not edit")

        species = fields.get("Pet Species", None)
        if species == "Dog":
            dog_list.append(pet)
        elif species == "Cat":
            cat_list.append(pet)

        filename = str(id) + ".php"
        output_file_list.append(filename)

        with codecs.open(NEW_DIGS_PROFILES_DIRECTORY + filename, 'w+') as pet_file:
            output = parse_new_digs_animal_profile(pet)
            output = output.replace('\u2028', '')
            pet_file.write(output)

    # delete stagnant pages
    for profile in profiles_current:
        if profile not in output_file_list:
            print("deleting " + NEW_DIGS_PROFILES_DIRECTORY + profile)
            if os.path.isfile(NEW_DIGS_PROFILES_DIRECTORY + profile):
                os.remove(NEW_DIGS_PROFILES_DIRECTORY + profile)

    generate_new_digs_pet_list(dog_list, NEW_DIGS_DOG_LIST_FILE)
    generate_new_digs_pet_list(cat_list, NEW_DIGS_CAT_LIST_FILE)


shelterluv_sync()
new_digs_sync()
