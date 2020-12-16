# Cat functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
from Local_Defines import PLACEHOLDER_IMAGE


def parse_cat_profile(animal):
    output = ""

    output += "<div class=\"pet-profile\">\n"
    output += "<div class=\"pet-profile-images\">\n"
    output += "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js\"></script>\n"
    output += "<link href=\"https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.css\" rel=\"stylesheet\">\n"
    output += "<script src=\"https://cdnjs.cloudflare.com/ajax/libs/fotorama/4.6.4/fotorama.js\"></script>\n"

    output += "<div class =\"fotorama\" data-nav=\"thumbs\" data-allowfullscreen=\"true\">\n"

    if len(animal["Photos"]) > 0:
        for photo in animal["Photos"]:
            output += "<img src=\""
            output += photo
            output += "\">\n"
    else:
        output += "<img src=\""
        output += PLACEHOLDER_IMAGE
        output += "\">\n"

    output += "</div>\n"
    output += "</div>\n"

    output += "<div class=\"pet-profile-data\">\n"
    output += "<div class=\"pet-profile-name\">\n"
    output += animal["Name"]
    output += "<br/>\n"
    output += "</div>\n"

    output += "<div class=\"pet-profile-other-data\">\n"
    output += "<b>ID: </b>DPA-A-"
    output += animal["ID"]
    output += "<br/>\n"

    output += "<b>Age: </b>"
    if animal["Age"] < 3:
        output += "Kitten"
    elif animal["Age"] < 7:
        output += "Young"
    elif animal["Age"] > 98:
        output += "Senior"
    else:
        output += "Adult"
    output += "<br/>\n"

    output += "<b>Sex: </b>"
    output += animal["Sex"]
    output += "<br/>\n"

    if animal["Breed"] is not None:
        output += "<b>Breed(s): </b>"
        output += animal["Breed"]
        output += "<br/>\n"

    output += "</div>\n"

    output += "<a class=\"pet-profile-top-adopt-button\" href=\"https://www.shelterluv.com/matchme/adopt/DPA-A-"
    output += animal["ID"]
    output += "?species=Cat\" "
    output += "onclick=\"ga('send', 'event', 'Cat Adoption App Button', " \
              "'click', 'Cat Top Adoption Application Button');\""
    output += ">Apply to Adopt "
    output += animal["Name"]
    output += "</a>\n"

    output += "</div>\n"

    output += "<div class=\"pet-profile-description\">\n"
    output += "<div class=\"pet-profile-description-title\">\n"
    output += "Meet "
    output += animal["Name"]
    output += "! <br/>\n"
    output += "</div>"

    if len(animal["Description"]) < 3:
        output += "We don't have much information on this animal yet. " \
                  "If you'd like to find out more, please email adopt@dallaspetsalive.org."
    else:
        output += "<p>"
        description = animal["Description"].replace("\n\n", "</p><p>")
        output += description
        output += "</p>"

    output += "<div class=\"et_pb_promo et_pb_bg_layout_dark et_pb_text_align_center pet-profile-adopt-bottom\""
    output += " style=\"background-color: #006cb7;\">\n"
    output += "<div class=\"et_pb_promo_description\">"
    output += "<h2>Apply to Adopt "
    output += animal["Name"]
    output += " Today</h2>\n"
    output += "</div>"

    output += "<a class=\"et_pb_promo_button\" href=\"https://www.shelterluv.com/matchme/adopt/DPA-A-"
    output += animal["ID"]
    output += "?species=Cat\" "
    output += "onclick =\"ga('send', 'event', 'Cat Adoption App Button', " \
              "'click', 'Cat Bottom Adoption Application Button');\""
    output += ">Go To Adoption Application</a>\n"

    output += "</div></div></div>"

    return output
