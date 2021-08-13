# Species specific functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com


def new_digs_profile_other_data(animal, doc, text, line):
    pet_fields = animal["fields"]
    species = pet_fields.get("Pet Species")

    if species == "Dog":
        dog_profile_other_data(animal, doc, text, line)
    elif species == "Cat":
        cat_profile_other_data(animal, doc, text, line)
    else:
        other_profile_other_data(animal, doc, text, line)


def dog_profile_other_data(animal, doc, text, line):
    pet_fields = animal["fields"]

    line("b", "ID: ")
    text(str(pet_fields.get("Pet ID - do not edit")))
    doc.stag("br")

    line("b", "Age: ")
    text(pet_fields.get("Pet Age"))
    doc.stag("br")

    line("b", "Sex: ")
    text(pet_fields.get("Sex"))
    doc.stag("br")

    if pet_fields.get("Breed - Dog") is not None:
        line("b", "Breed(s): ")
        text(pet_fields.get("Breed - Dog"))
        doc.stag("br")

    line("b", "Size: ")
    text(pet_fields.get("Pet Size"))
    doc.stag("br")


def cat_profile_other_data(animal, doc, text, line):
    pet_fields = animal["fields"]

    line("b", "ID: ")
    text(str(pet_fields.get("Pet ID - do not edit")))
    doc.stag("br")

    line("b", "Age: ")
    text(pet_fields.get("Pet Age"))
    doc.stag("br")

    line("b", "Sex: ")
    text(pet_fields.get("Sex"))
    doc.stag("br")

    if pet_fields.get("Breed - Cat") is not None:
        line("b", "Breed(s): ")
        text(pet_fields.get("Breed - Cat"))
        doc.stag("br")


def other_profile_other_data(animal, doc, text, line):
    pet_fields = animal["fields"]

    line("b", "ID: ")
    text(str(pet_fields.get("Pet ID - do not edit")))
    doc.stag("br")

    line("b", "Age: ")
    text(pet_fields.get("Pet Age"))
    doc.stag("br")

    line("b", "Sex: ")
    text(pet_fields.get("Sex"))
    doc.stag("br")

    line("b", "Species: ")
    text(pet_fields.get("Pet Species"))
    doc.stag("br")

    if pet_fields.get("Breed - Other") is not None:
        line("b", "Breed(s): ")
        text(pet_fields.get("Breed - Other"))
        doc.stag("br")
