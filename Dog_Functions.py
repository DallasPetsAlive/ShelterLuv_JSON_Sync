# Dog functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import collections
import Common_Functions


def generate_dog_pages(dogs):
    Common_Functions.manage_pages(dogs, 0)


def generate_dog_page_php(dog):
    # TODO generate HTML/PHP for dogs
    return "stuff for dogs"


# This function accepts the list of dogs and generates the formatted list for browser output
def generate_dog_list(dogs):
    # TODO take the dog list and generate HTML/PHP for list output
    pass


# This function accepts animal list from main and parses the dogs
def parse_dogs(animals_in):
    dog_list = collections.OrderedDict()

    # get the dogs
    for animal in animals_in:
        if animals_in[animal]["Type"] == "Dog":
            dog_list[animal] = animals_in[animal]

    generate_dog_list(dog_list)

    generate_dog_pages(dog_list)
