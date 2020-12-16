# Dog functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com
from yattag import Doc, indent
from Local_Defines import PLACEHOLDER_IMAGE


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
