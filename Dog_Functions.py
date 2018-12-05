# Dog functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import collections
from Local_Defines import DOG_LIST_FILE, PLACEHOLDER_IMAGE, LIST_THEME_PATH, PET_LINK_RELATIVE_PATH


# This function accepts the list of dogs and generates the formatted list for browser output
def generate_dog_list(dogs):
    with open(DOG_LIST_FILE, 'w') as file:
        file.write("<script src=\"")
        file.write(LIST_THEME_PATH)
        file.write("lazy/jquery.min.js\"></script>")
        file.write("<script type=\"text/javascript\" src=\"")
        file.write(LIST_THEME_PATH)
        file.write("lazy/jquery.lazy.min.js\"></script>")
        file.write("<div class=\"pet-list\">")

        pet_count = 0

        for dog in dogs:
            pet_count += 1

            # for dev this is ../../
            # for local this is ../
            pet_name = dogs[dog]['Name']
            pet_id = dogs[dog]['ID']
            pet_photo = dogs[dog]['CoverPhoto']
            output = '<div class="pet-list-pet">' \
                     '<div class ="pet-list-image">' \
                     '<a href="'
            output += PET_LINK_RELATIVE_PATH
            output += 'pet/'
            output += pet_id.encode('utf-8')
            output += '">'

            if pet_count <= 20:
                output += '<img src = "'

                if "default_" not in pet_photo:
                    output += pet_photo.encode('utf-8')
                else:
                    output += PLACEHOLDER_IMAGE

                output += '">'

                # for animals after the fist 20, lazy load the pictures
            else:
                output += '<img class="lazy" src="'
                output += PLACEHOLDER_IMAGE
                output += '" alt="Photo" data-src= "'
                if "default_" not in pet_photo:
                    output += pet_photo.encode('utf-8')
                else:
                    output += PLACEHOLDER_IMAGE
                output += '">'

            output += '</a>' \
                      '</div>' \
                      '<div class="pet-list-name">' \
                      '<a href="'
            output += PET_LINK_RELATIVE_PATH
            output += 'pet/'
            output += pet_id.encode('utf-8')
            output += '">'
            output += pet_name.encode('utf-8')
            output += '</a></div></div>'
            output += '\n'
            file.write(output)
        file.write("</div>")
        file.write("<script>")
        file.write("    $(function() {")
        file.write("        $('.lazy').lazy();")
        file.write("    });")
        file.write("</script>")


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
    output += "<script src=\"../../wp-content/themes/Divi-child/fotorama/jquery.min.js\"></script>\n"
    output += "<link href=\"../../wp-content/themes/Divi-child/fotorama/fotorama.css\" rel=\"stylesheet\">\n"
    output += "<script src=\"../../wp-content/themes/Divi-child/fotorama/fotorama.js\"></script>\n"

    output += "<div class =\"fotorama\" data-nav=\"thumbs\" data-allowfullscreen=\"true\">\n"

    if len(animal["Photos"]) > 0:
        for photo in animal["Photos"]:
            output += "<img src=\""
            output += photo.encode('utf-8')
            output += "\">\n"
    else:
        output += "<img src=\""
        output += PLACEHOLDER_IMAGE
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

    if "Small" in animal["Size"]:
        output += "<b>Size: </b>Small<br/>\n"
    elif "Medium" in animal["Size"]:
        output += "<b>Size: </b>Medium<br/>\n"
    elif "Large" in animal["Size"]:
        output += "<b>Size: </b>Large<br/>\n"
    elif "Extra" in animal["Size"]:
        output += "<b>Size: </b>Extra-Large<br/>\n"

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

    if len(animal["Description"]) < 3:
        output += "We don't have much information on this animal yet. " \
                  "If you'd like to find out more, please email adopt@dallaspetsalive.org."
    else:
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
