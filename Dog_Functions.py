# Dog functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import collections
import Common_Functions
import json
from Local_Defines import DOG_LIST_FILE


# This function accepts the list of dogs and generates the formatted list for browser output
def generate_dog_list(dogs):
    with open(DOG_LIST_FILE, 'w') as file:
        file.write("<div class=\"pet-list\">")
        for dog in dogs:
            petName = dogs[dog]['Name']
            petId = dogs[dog]['ID']
            petPhoto = dogs[dog]['CoverPhoto']
            output = '<div class="pet-list-pet">' \
                     '<div class ="pet-list-image">' \
                     '<a href="//localhost/wordpress/pet/'
            output += petId.encode('utf-8')
            output += '">'
            output += '<img src = "'
            output += petPhoto.encode('utf-8')
            output += '">' \
                     '</a>' \
                     '</div>' \
                     '<div class="pet-list-name">' \
                     '<a href="//localhost/wordpress/pet/'
            output += petId.encode('utf-8')
            output += '">'
            output += petName.encode('utf-8')
            output += '</a></div></div>'
            output += '\n'
            file.write(output)
        file.write("</div>")


# This function accepts animal list from main and parses the dogs
def parse_dogs(animals_in):
    dog_list = collections.OrderedDict()

    # get the dogs
    for animal in animals_in:
        if animals_in[animal]["Type"] == "Dog":
            dog_list[animal] = animals_in[animal]

    generate_dog_list(dog_list)


def parse_dog_profile(animal):
    return animal["Name"]
