def mask_phone_number(phone):
    return "******" + phone[-4:]

phone = input("Enter 10-digit phone number: ")
print(mask_phone_number(phone))