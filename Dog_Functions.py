# Dog functions for ShelterLuv sync
import collections


DOG_LIST_FILE = "dog_list.html"


def parse_dogs(animals_in):
    dog_list = collections.OrderedDict()

    # get the dogs
    for animal in animals_in:
        if animals_in[animal]["Type"] == "Dog":
            dog_list[animal] = animals_in[animal]


