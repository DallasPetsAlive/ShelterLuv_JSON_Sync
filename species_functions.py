# Species specific functions for ShelterLuv sync
# Developed for Dallas Pets Alive by Katie Patterson www.kirska.com


def profile_other_data(animal, doc, text, line):
    if animal["Type"] == "Dog":
        dog_profile_other_data(animal, doc, text, line)
    elif animal["Type"] == "Cat":
        cat_profile_other_data(animal, doc, text, line)
    else:
        other_profile_other_data(animal, doc, text, line)


def dog_profile_other_data(animal, doc, text, line):
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


def cat_profile_other_data(animal, doc, text, line):
    line("b", "ID: ")
    text(animal["ID"])
    doc.stag("br")

    line("b", "Age: ")
    if animal["Age"] < 3:
        text("Kitten")
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


def other_profile_other_data(animal, doc, text, line):
    line("b", "ID: ")
    text(animal["ID"])
    doc.stag("br")

    line("b", "Age: ")
    if animal["Age"] < 3:
        text("Baby")
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

    line("b", "Type: ")
    text(animal["Type"])
    doc.stag("br")

    if animal["Breed"] is not None:
        line("b", "Breed(s): ")
        text(animal["Breed"])
        doc.stag("br")
