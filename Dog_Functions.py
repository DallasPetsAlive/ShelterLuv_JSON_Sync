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
            # for dev this is ../../
            # for local this is ../
            petName = dogs[dog]['Name']
            petId = dogs[dog]['ID']
            petPhoto = dogs[dog]['CoverPhoto']
            output = '<div class="pet-list-pet">' \
                     '<div class ="pet-list-image">' \
                     '<a href="../pet/'
            output += petId.encode('utf-8')
            output += '">'
            output += '<img src = "'
            output += petPhoto.encode('utf-8')
            output += '">' \
                     '</a>' \
                     '</div>' \
                     '<div class="pet-list-name">' \
                     '<a href="../pet/'
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
    output = ""

    output += "<div class=\"pet-profile\">\n"
    output += "<div class=\"pet-profile-images\">\n"
    output += "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js\"></script>\n"
    output += "<link href=\"https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.css\" rel=\"stylesheet\">\n"
    output += "<script src=\"https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.js\"></script>\n"

    output += "<div class =\"fotorama\" data-nav=\"thumbs\" data-allowfullscreen=\"true\">\n"

    for photo in animal["Photos"]:
        output += "<img src=\""
        output += photo.encode('utf-8')
        output += "\">\n"

    output += "</div>\n"
    output += "</div>\n"

    output += "<div class=\"pet-profile-data\">\n"
    output += "<div class=\"pet-profile-name\">\n"
    output += animal["Name"].encode('utf-8')
    output += "<br/>\n"
    output += "</div>\n"

    output += "<div class=\"pet-profile-other-data\">\n"
    output += "<b>ID: </b>DPA-A-"
    output += animal["ID"].encode('utf-8')
    output += "<br/>\n"

    output += "<b>Age: </b>"
    if animal["Age"] < 3:
        output += "Puppy"
    elif animal["Age"] < 7:
        output += "Young"
    elif animal["Age"] > 98:
        output += "Senior"
    else:
        output += "Adult"
    output += "<br/>\n"

    output += "<b>Sex: </b>"
    output += animal["Sex"].encode('utf-8')
    output += "<br/>\n"

    output += "<b>Breed(s): </b>"
    output += animal["Breed"].encode('utf-8')
    output += "<br/>\n"

    output += "<b>Size: </b>Unknown <br/>\n"

    output += "</div>\n"

    output += "<a class=\"pet-profile-top-adopt-button\" href=\"https://www.shelterluv.com/matchme/adopt/DPA-A-"
    output += animal["ID"].encode('utf-8')
    output += "?species=Dog\">Apply to Adopt "
    output += animal["Name"].encode('utf-8')
    output += "</a>\n"

    output += "</div>\n"

    output += "<div class=\"pet-profile-description\">\n"
    output += "<div class=\"pet-profile-description-title\">\n"
    output += "Meet "
    output += animal["Name"].encode('utf-8')
    output += "! <br/>\n"
    output += "</div>"

    output += animal["Description"].encode('utf-8')

    output += "<div class=\"et_pb_promo et_pb_bg_layout_dark et_pb_text_align_center pet-profile-adopt-bottom\""
    output += " style=\"background-color: #006cb7;\">\n"
    output += "<div class=\"et_pb_promo_description\">"
    output += "<h2>Apply to Adopt "
    output += animal["Name"].encode('utf-8')
    output += " Today</h2>\n"
    output += "</div>"

    output += "<a class=\"et_pb_promo_button\" href=\"https://www.shelterluv.com/matchme/adopt/DPA-A-"
    output += animal["ID"].encode('utf-8')
    output += "?species=Dog\">Go To Adoption Application</a>\n"

    output += "</div></div></div>"

    return output
