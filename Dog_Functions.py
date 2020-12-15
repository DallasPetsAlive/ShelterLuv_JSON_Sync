# Dog functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
import collections
from yattag import Doc, indent
from Local_Defines import (
    DOG_LIST_FILE,
    PLACEHOLDER_IMAGE,
    LIST_THEME_PATH,
    PET_LINK_RELATIVE_PATH,
)


# This function accepts the list of dogs and
# generates the formatted list for browser output
def generate_dog_list(dogs):
    with open(DOG_LIST_FILE, 'w+') as file:
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
        file.write("<div data-jplist-control=\"dropdown-sort\" class=\"jplist-dd\"" )
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
        file.write(" data-type=\"number\" data-selected=\"true\"> Featured Pets First </div>")

        file.write("<div class=\"jplist-dd-item\"")
        file.write(" data-path=\".pet-list-intake-date\"")
        file.write(" data-order=\"desc\"")
        file.write(" data-type=\"number\"> Newest Arrivals First </div>")

        file.write("</div></div></div></div>")

        file.write("<div data-jplist-group=\"group1\" class=\"pet-list\">")

        pet_count = 0

        for dog in dogs:
            pet_count += 1

            # for dev this is ../../
            # for local this is ../
            pet_name = dogs[dog]['Name']
            pet_id = dogs[dog]['ID']
            pet_photo = dogs[dog]['CoverPhoto']
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

                output += '">'"""

                # for animals after the fist 20, lazy load the pictures
            #else:

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
            output += dogs[dog]['LastIntakeUnixTime']
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
def parse_dogs(animals_in):
    dog_list = collections.OrderedDict()

    # get the dogs
    for animal in animals_in:
        if animals_in[animal]["Type"] == "Dog":
            dog_list[animal] = animals_in[animal]

    generate_dog_list(dog_list)


def parse_dog_profile(animal):
    doc, tag, text, line = Doc().ttl()

    with tag("div", klass="pet-profile"):
        with tag("div", klass="pet-profile-images"):
            doc.asis(
                "<script src=\"https://ajax.googleapis.com/ajax/" +
                "libs/jquery/1.11.1/jquery.min.js\"></script>"
            )
            doc.asis(
                "<link href=\"https://cdnjs.cloudflare.com/ajax/" +
                "libs/fotorama/4.6.4/fotorama.css\" rel=\"stylesheet\">"
            )
            doc.asis(
                "<script src=\"https://cdnjs.cloudflare.com/ajax/" +
                "libs/fotorama/4.6.4/fotorama.js\"></script>"
            )
            with tag(
                "div",
                ("data-nav", "thumbs"),
                ("data-allowfullscreen", "true"),
                klass="fotorama"
            ):
                if len(animal["Photos"]) > 0:
                    for photo in animal["Photos"]:
                        doc.stag("img", src=photo)
                else:
                    doc.stag("img", src=PLACEHOLDER_IMAGE)

        with tag("div", klass="pet-profile-data"):
            with tag("div", klass="pet-profile-name"):
                text(animal["Name"])
                doc.stag("br")

            with tag("div", klass="pet-profile-other-data"):
                line("b", "ID: ")
                text(animal["ID"])
                doc.stag("br")

                line("b", "Age: ")
                if animal["Age"] < 3:
                    text("Puppy")
                elif animal["Age"] < 7:
                    text("Young")
                elif animal["Age"] > 98:
                    text("Senior")
                else:
                    text("Adult")
                doc.stag("br")

                line("b", "Sex: ")
                text(animal["Sex"])
                doc.stag("br")

                if animal["Breed"] is not None:
                    line("b", "Breed(s): ")
                    text(animal["Breed"])
                    doc.stag("br")

                line("b", "Size: ")
                if "Small" in animal["Size"]:
                    text("Small")
                elif "Medium" in animal["Size"]:
                    text("Medium")
                elif "Large" in animal["Size"]:
                    text("Large")
                elif "Extra" in animal["Size"]:
                    text("Extra-Large")
                doc.stag("br")

            adopt_link = (
                "https://www.shelterluv.com/matchme/adopt/DPA-A-" +
                animal["ID"] +
                "?species=Dog"
            )
            with tag(
                "a",
                href=adopt_link,
                klass="pet-profile-top-adopt-button"
            ):
                text("Apply to Adopt " + animal["Name"])

        with tag("div", klass="pet-profile-description"):
            with tag("div", klass="pet-profile-description-title"):
                text("Meet " + animal["Name"] + "!")
                doc.stag("br")

            if len(animal["Description"]) < 3:
                text(
                    "We don't have much information on this animal yet. " +
                    "If you'd like to find out more, " +
                    "please email adopt@dallaspetsalive.org."
                )

            else:
                with tag("p"):
                    doc.asis(animal["Description"].replace("\n\n", "</p><p>"))

            with tag(
                "div",
                klass=(
                    "et_pb_promo et_pb_bg_layout_dark" +
                    "et_pb_text_align_center pet-profile-adopt-bottom"
                ),
                style="background-color: #006cb7;"
            ):
                with tag("div", klass="et_pb_promo_description"):
                    line("h2", "Apply to Adopt " + animal["Name"] + " Today")
                with tag("a", klass="et_pb_promo_button", href=adopt_link):
                    text("Go To Adoption Application")

    return indent(doc.getvalue())
