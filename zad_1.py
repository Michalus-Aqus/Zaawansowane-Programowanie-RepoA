def gen_greatings_text(name:str,surname:str):
    return "Cześć %(name)s %(surname)s!" % {"name": name, "surname" : surname}


print(gen_greatings_text("James","Bond"))
