# Cat functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import collections
import Common_Functions
import json


def generate_cat_pages(cats):
    Common_Functions.manage_pages(0, cats)


def generate_cat_page_php(cat):
    # TODO generate HTML/PHP for cats
    return str(json.dumps(cat))


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

    generate_cat_pages(cat_list)
