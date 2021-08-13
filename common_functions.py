# Common/other animal functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
from yattag import Doc, indent
from local_defines import (
    PLACEHOLDER_IMAGE, LIST_THEME_PATH, PET_LINK_RELATIVE_PATH
)
from species_functions import profile_other_data
from new_digs_species_functions import new_digs_profile_other_data


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


def generate_homepage_pet_list(pets, filename):
    doc, tag, text = Doc().tagtext()

    if len(pets) == 0:
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

    with tag("div", klass="pet-list pet-list-homepage"):
        for pet in pets:
            pet_name = pets[pet]['Name']
            pet_id = pets[pet]['ID']
            pet_photo = pets[pet]['CoverPhoto']

            with tag("div", klass="pet-list-pet pet-list-pet-homepage"):
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

    with open(filename, 'w+') as file:
        file.write(indent(doc.getvalue()))


def parse_animal_profile(animal):
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
                profile_other_data(animal, doc, text, line)

            adopt_link = (
                "https://www.shelterluv.com/matchme/adopt/DPA-A-" +
                animal["ID"]
            )
            if animal["Type"] == "Dog":
                adopt_link = adopt_link + "?species=Dog"
            elif animal["Type"] == "Cat":
                adopt_link = adopt_link + "?species=Cat"
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


def generate_new_digs_pet_list(pets, filename):
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
            pet_fields = pet.get("fields", {})

            pet_name = pet_fields.get("Pet Name")
            pet_id = str(pet_fields.get("Pet ID - do not edit"))
            pet_photo = None
            pet_photos = pet_fields.get("Pictures")
            if pet_photos:
                pet_photo = pet_photos[0]["url"]

            with tag(
                "div",
                ("data-jplist-item"),
                klass="pet-list-pet",
            ):
                pet_link = PET_LINK_RELATIVE_PATH + "pet/" + pet_id
                with tag("a", href=pet_link):
                    with tag("div", klass="pet-list-image"):
                        pet_photo_link = pet_photo
                        if not pet_photo:
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
                        text(pet_fields.get("Made Available for Adoption Date"))

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


def parse_new_digs_animal_profile(pet):
    pet_fields = pet["fields"]
    name = pet_fields.get("Pet Name")
    pet_id = str(pet_fields.get("Pet ID - do not edit"))
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
                pet_photos = pet_fields.get("Pictures")
                if len(pet_photos) > 0:
                    for photo in pet_photos:
                        doc.stag("img", src=photo["url"])
                else:
                    doc.stag("img", src=PLACEHOLDER_IMAGE)

        with tag("div", klass="pet-profile-data"):
            with tag("div", klass="pet-profile-name"):
                text(name)
                doc.stag("br")

            with tag("div", klass="pet-profile-other-data"):
                new_digs_profile_other_data(pet, doc, text, line)

            adopt_link = (
                "https://www.shelterluv.com/matchme/adopt/DPA-A-" +
                pet_id
            )
            if pet_fields.get("Pet Species") == "Dog":
                adopt_link = adopt_link + "?species=Dog"
            elif pet_fields.get("Pet Species") == "Cat":
                adopt_link = adopt_link + "?species=Cat"
            with tag(
                "a",
                href=adopt_link,
                klass="pet-profile-top-adopt-button"
            ):
                text("Apply to Adopt " + name)

        with tag("div", klass="pet-profile-description"):
            with tag("div", klass="pet-profile-description-title"):
                text("Meet " + name + "!")
                doc.stag("br")

            description = pet_fields.get("Public Description")

            if not description or len(description) < 3:
                text(
                    "We don't have much information on this animal yet. " +
                    "If you'd like to find out more, " +
                    "please email adopt@dallaspetsalive.org."
                )

            else:
                with tag("p"):
                    doc.asis(description.replace("\n\n", "</p><p>"))

            with tag(
                "div",
                klass=(
                    "et_pb_promo et_pb_bg_layout_dark" +
                    "et_pb_text_align_center pet-profile-adopt-bottom"
                ),
                style="background-color: #006cb7;"
            ):
                with tag("div", klass="et_pb_promo_description"):
                    line("h2", "Apply to Adopt " + name + " Today")
                with tag("a", klass="et_pb_promo_button", href=adopt_link):
                    text("Go To Adoption Application")

    return indent(doc.getvalue())
