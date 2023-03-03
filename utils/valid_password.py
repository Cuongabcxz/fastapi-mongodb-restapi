import re


def password_check(passwd):
    SpecialSym = ['!', '@', '#', '$', '%', '&', '_', '=']
    val = True
    if passwd == "":
        print('Not pass variable')
        val = False
    if len(passwd) < 8:
        print('length should be at least 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    return val
