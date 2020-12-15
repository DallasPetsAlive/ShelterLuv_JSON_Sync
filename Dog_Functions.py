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
    doc, tag, text = Doc().tagtext()

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
        for dog in dogs:
            pet_count += 1

            pet_name = dogs[dog]['Name']
            pet_id = dogs[dog]['ID']
            pet_photo = dogs[dog]['CoverPhoto']

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
                        text(dogs[dog]['LastIntakeUnixTime'])

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

    with open(DOG_LIST_FILE, 'w+') as file:
        file.write(indent(doc.getvalue()))


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
