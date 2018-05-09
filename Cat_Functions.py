# Cat functions for ShelterLuv sync
import collections


def parse_cats(animals_in):
    cat_list = collections.OrderedDict()

    # get the cats
    for animal in animals_in:
        if animals_in[animal]["Type"] == "Dog":
            cat_list[animal] = animals_in[animal]
