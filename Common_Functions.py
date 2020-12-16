# Common/other animal functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
from yattag import Doc, indent
from Local_Defines import (
    PLACEHOLDER_IMAGE, LIST_THEME_PATH, PET_LINK_RELATIVE_PATH
)


# This function accepts the list of pets and
# generates the formatted list for browser output
def generate_pet_list(pets, filename):
    doc, tag, text = Doc().tagtext()

    if len(pets) == 0:
        with tag("div", klass="empty-pet-list"):
            text(
                "We currently have no pets of this type!" +
                " Please check out our other adoptable pets," +
                " or consider fostering."
            )
        with open(filename, 'w+') as file:
            file.write(indent(doc.getvalue()))
        return

    doc.asis(
        "<script src=\"" +
        LIST_THEME_PATH +
        "lazy/jquery.min.js\"></script>"
    )
    doc.asis(
        "<script type=\"text/javascript\" src=\"" +
        LIST_THEME_PATH +
        "lazy/jquery.lazy.min.js\"></script>"
    )
    doc.asis(
        "<link href=\"" +
        LIST_THEME_PATH +
        "jplist/jplist.styles.css\" rel=\"stylesheet\" type=\"text/css\" />"
    )

    with tag("div", klass="sort-filter-options-parent"):
        with tag("div", klass="sort-filter-options"):
            with tag(
                "div",
                ("data-jplist-control", "dropdown-sort"),
                ("data-group", "group1"),
                ("data-name", "sorttitle"),
                klass="jplist-dd",
            ):
                with tag(
                    "div",
                    ("data-type", "panel"),
                    klass="jplist-dd-panel",
                ):
                    text(" Sort by ")
                with tag(
                    "div",
                    ("data-type", "content"),
                    klass="jplist-dd-content",
                ):
                    # sort by options
                    with tag(
                        "div",
                        ("data-path", "default"),
                        klass="jplist-dd-item",
                    ):
                        text(" Sort by ")
                    with tag(
                        "div",
                        ("data-path", ".pet-list-name"),
                        ("data-order", "asc"),
                        ("data-type", "text"),
                        klass="jplist-dd-item",
                    ):
                        text(" Name A - Z ")
                    with tag(
                        "div",
                        ("data-path", ".pet-list-name"),
                        ("data-order", "desc"),
                        ("data-type", "text"),
                        klass="jplist-dd-item",
                    ):
                        text(" Name Z - A ")
                    with tag(
                        "div",
                        ("data-path", ".pet-list-intake-date"),
                        ("data-order", "asc"),
                        ("data-type", "number"),
                        ("data-selected", "true"),
                        klass="jplist-dd-item",
                    ):
                        text(" Featured Pets First ")
                    with tag(
                        "div",
                        ("data-path", ".pet-list-intake-date"),
                        ("data-order", "desc"),
                        ("data-type", "number"),
                        ("data-selected", "true"),
                        klass="jplist-dd-item",
                    ):
                        text(" Newest Arrivals First ")

    with tag("div", ("data-jplist-group", "group1"), klass="pet-list"):
        pet_count = 0
        for pet in pets:
            pet_count += 1

            pet_name = pets[pet]['Name']
            pet_id = pets[pet]['ID']
            pet_photo = pets[pet]['CoverPhoto']

            with tag(
                "div",
                ("data-jplist-item"),
                klass="pet-list-pet",
            ):
                pet_link = PET_LINK_RELATIVE_PATH + "pet/" + pet_id
                with tag("a", href=pet_link):
                    with tag("div", klass="pet-list-image"):
                        pet_photo_link = pet_photo
                        if "default_" in pet_photo:
                            pet_photo_link = PLACEHOLDER_IMAGE
                        doc.stag(
                            "img",
                            ("data-src", pet_photo_link),
                            src=PLACEHOLDER_IMAGE,
                            alt="Photo",
                            klass="lazy",
                        )
                    with tag("div", klass="pet-list-name"):
                        text(pet_name)
                    with tag("div", klass="pet-list-intake-date hidden"):
                        text(pets[pet]['LastIntakeUnixTime'])

    doc.asis(
        "<script>" +
        "    $(function() {" +
        "        $('.lazy').lazy();" +
        "    });" +
        "</script>"
    )
    doc.asis(
        "<script src=\"//cdnjs.cloudflare.com/ajax/libs/babel-polyfill" +
        "/6.26.0/polyfill.min.js\"></script>"
    )
    doc.asis(
        "<script src=\"" +
        LIST_THEME_PATH +
        "jplist/jplist.min.js\"></script>" +
        "<script>jplist.init();</script>"
    )

    with open(filename, 'w+') as file:
        file.write(indent(doc.getvalue()))


def parse_other_profile(animal):
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
        output += "Baby"
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

    output += "<b>Type: </b>"
    output += animal["Type"]
    output += "<br/>\n"

    if animal["Breed"] is not None:
        output += "<b>Breed(s): </b>"
        output += animal["Breed"]
        output += "<br/>\n"

    output += "</div>\n"

    output += "<a class=\"pet-profile-top-adopt-button\" href=\"https://www.shelterluv.com/matchme/adopt/DPA-A-"
    output += animal["ID"]
    output += "\" "
    output += "onclick=\"ga('send', 'event', 'Others Adoption App Button', " \
              "'click', 'Other Top Adoption Application Button');\""
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
    output += "\" "
    output += "onclick=\"ga('send', 'event', 'Others Adoption App Button', " \
              "'click', 'Other Bottom Adoption Application Button');\""
    output += ">Go To Adoption Application</a>\n"

    output += "</div></div></div>"

    return output
