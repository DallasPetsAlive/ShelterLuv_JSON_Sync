# Cat functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import collections
from Local_Defines import CAT_LIST_FILE, PLACEHOLDER_IMAGE, LIST_THEME_PATH, PET_LINK_RELATIVE_PATH


# This function accepts the list of dogs and generates the formatted list for browser output
def generate_cat_list(cats):
    with open(CAT_LIST_FILE, 'w') as file:
        file.write("<script src=\"")
        file.write(LIST_THEME_PATH)
        file.write("lazy/jquery.min.js\"></script>")
        file.write("<script type=\"text/javascript\" src=\"")
        file.write(LIST_THEME_PATH)
        file.write("lazy/jquery.lazy.min.js\"></script>")

        file.write("<link href=\"")
        file.write(LIST_THEME_PATH)
        file.write("jplist/jplist.styles.css\" rel=\"stylesheet\" type=\"text/css\" />")

        file.write("<div class =\"sort-filter-options-parent\"><div class=\"sort-filter-options\">")
        file.write("<div data-jplist-control=\"dropdown-sort\" class=\"jplist-dd\"")
        file.write(" data-group=\"group1\"")
        file.write(" data-name=\"sorttitle\">")

        file.write("<div data-type=\"panel\" class=\"jplist-dd-panel\"> Sort by </div>")
        file.write("<div data-type=\"content\" class=\"jplist-dd-content\">")
        file.write("<div class=\"jplist-dd-item\" data-path=\"default\"> Sort by </div>")

        file.write("<div class=\"jplist-dd-item\"")
        file.write(" data-path=\".pet-list-name\"")
        file.write(" data-order=\"asc\"")
        file.write(" data-type=\"text\"> Name A - Z </div>")

        file.write("<div class=\"jplist-dd-item\"")
        file.write(" data-path=\".pet-list-name\"")
        file.write(" data-order=\"desc\"")
        file.write(" data-type=\"text\"> Name Z - A </div>")

        file.write("<div class=\"jplist-dd-item\"")
        file.write(" data-path=\".pet-list-intake-date\"")
        file.write(" data-order=\"asc\"")
        file.write(" data-type=\"number\" data-selected=\"true\"> Longest Stays First </div>")

        file.write("<div class=\"jplist-dd-item\"")
        file.write(" data-path=\".pet-list-intake-date\"")
        file.write(" data-order=\"desc\"")
        file.write(" data-type=\"number\"> Newest Arrivals First </div>")

        file.write("</div></div></div></div>")

        file.write("<div data-jplist-group=\"group1\" class=\"pet-list\">")

        pet_count = 0

        for cat in cats:
            pet_count += 1

            # for dev this is ../../
            # for local this is ../
            pet_name = cats[cat]['Name']
            pet_id = cats[cat]['ID']
            pet_photo = cats[cat]['CoverPhoto']
            output = '<div data-jplist-item class="pet-list-pet">' \
                     '<div class ="pet-list-image">' \
                     '<a href="'
            output += PET_LINK_RELATIVE_PATH
            output += 'pet/'
            output += pet_id
            output += '">'

            """if pet_count <= 20:
                output += '<img src = "'

                if "default_" not in pet_photo:
                    output += pet_photo
                else:
                    output += PLACEHOLDER_IMAGE

                output += '">'

                # for animals after the fist 20, lazy load the pictures
            else:"""
            output += '<img class="lazy" src="'
            output += PLACEHOLDER_IMAGE
            output += '" alt="Photo" data-src= "'
            if "default_" not in pet_photo:
                output += pet_photo
            else:
                output += PLACEHOLDER_IMAGE
            output += '">'

            output += '</a>' \
                      '</div>' \
                      '<div class="pet-list-name">' \
                      '<a href="'
            output += PET_LINK_RELATIVE_PATH
            output += 'pet/'
            output += pet_id
            output += '">'
            output += pet_name
            output += '</a></div>'
            output += '<div class="pet-list-intake-date hidden">'
            output += cats[cat]['LastIntakeUnixTime']
            output += '</div>'
            output += '</div>'
            output += '\n'
            file.write(output)
        file.write("</div>")
        file.write("<script>")
        file.write("    $(function() {")
        file.write("        $('.lazy').lazy();")
        file.write("    });")
        file.write("</script>")

        file.write("<script src=\"//cdnjs.cloudflare.com/ajax/libs/babel-polyfill/6.26.0/polyfill.min.js\"></script>")

        file.write("<script src=\"")
        file.write(LIST_THEME_PATH)
        file.write("jplist/jplist.min.js\"></script>")
        file.write("<script>jplist.init();</script>")


# This function accepts animal list from main and parses the dogs
def parse_cats(animals_in):
    cat_list = collections.OrderedDict()

    # get the cats
    for animal in animals_in:
        if animals_in[animal]["Type"] == "Cat":
            cat_list[animal] = animals_in[animal]

    generate_cat_list(cat_list)


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
        output += animal["Description"]

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
