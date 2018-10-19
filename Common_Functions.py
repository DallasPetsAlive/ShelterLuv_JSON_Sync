# Dog functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import collections
import os
from Local_Defines import PROFILES_DIRECTORY


# This function accepts the list of animals and generates profile pages for browser output
def parse_profiles(animals):
    output_file_list = []

    # get current list of animal pages
    profiles_current = os.listdir(PROFILES_DIRECTORY)

    for animal in animals:
        filename = animal + ".php"
        output_file_list.append(filename)

        with open(PROFILES_DIRECTORY + filename, 'w') as file:
            # TODO generate the HTML/PHP
            pass

    # delete stagnant pages
    for profile in profiles_current:
        if profile not in output_file_list:
            print "deleting " + PROFILES_DIRECTORY + profile
            if os.path.isfile(PROFILES_DIRECTORY + profile):
                os.remove(PROFILES_DIRECTORY + profile)
