import re
def normalize_phone(phone_number):
    cleaned_numbers = []
    for search in phone_number:
        clean_number = re.sub(r"\D", "", search)
        if len(clean_number) == 9:
            clean_number = "380" + clean_number
        elif len(clean_number) == 10:
            clean_number = "38" + clean_number
        elif len(clean_number) == 11:
            clean_number = "3" + clean_number

        cleaned_numbers.append(clean_number)
    return cleaned_numbers


all_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]
result=normalize_phone(all_numbers)
for number in result:
    print(number)