# Dog functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import collections
import os
from Local_Defines import DOG_PROFILES_DIRECTORY, CAT_PROFILES_DIRECTORY
import Dog_Functions
import Cat_Functions


# This function accepts the list of dogs or cats and generates dog or cat profile pages for browser output
def manage_pages(dogs, cats):
    # determine if we're working with dogs or cats
    if dogs == 0:
        directory = CAT_PROFILES_DIRECTORY
        dog_list = False
        animals = cats
    else:
        directory = DOG_PROFILES_DIRECTORY
        dog_list = True
        animals = dogs

    # get current list of animal pages
    profiles_current = os.listdir(directory)
    output_file_list = []

    for animal in animals:
        filename = animal + ".php"
        output_file_list.append(filename)

        with open(directory + filename, 'w') as file:
            # TODO generate the HTML/PHP
            if dog_list:
                php = Dog_Functions.generate_dog_page_php(animals[animal])
                file.write(php)
            else:
                php = Cat_Functions.generate_cat_page_php(animals[animal])
                file.write(php)

    # delete stagnant pages
    for profile in profiles_current:
        if profile not in output_file_list:
            print "deleting " + directory + profile
            if os.path.isfile(directory + profile):
                os.remove(directory + profile)
