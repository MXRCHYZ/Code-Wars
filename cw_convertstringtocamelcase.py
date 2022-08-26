def to_camel_case(text):
    camel_case = ""
    old_string = text
    while True:
        if "" == text:
            return ""
        if "-" in old_string:
            old_string = text.split("-")
            old_string = "_".join(old_string)
        if "_" in old_string:
            old_string = old_string.split("_")
            old_string = " ".join(old_string)
            
        if " " in old_string:
            old_string = old_string.split(" ")
        break
    for i, s in enumerate(old_string):
        if i == 0:
            camel_case += s
        else:
            camel_case += s.title()
    return camel_case
print(to_camel_case("the-stealth_warrior"))