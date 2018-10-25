# Cat functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import collections
import Common_Functions
import json


# This function accepts the list of dogs and generates the formatted list for browser output
def generate_cat_list(cats):
    # TODO take the cat list and generate HTML/PHP for list output
    pass


# This function accepts animal list from main and parses the dogs
def parse_cats(animals_in):
    cat_list = collections.OrderedDict()

    # get the cats
    for animal in animals_in:
        if animals_in[animal]["Type"] == "Cat":
            cat_list[animal] = animals_in[animal]

    generate_cat_list(cat_list)


def parse_cat_profile(animal):
    return animal["Name"]
