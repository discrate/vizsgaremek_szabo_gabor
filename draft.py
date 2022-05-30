import random
import string


# def email_gen():
#     userx = {
#         "counter": 992,
#         "name": "szgtest",
#         "domain": "gmail.com",
#         "password": "Tesztelek1"
#     }
#     email = f'{userx["name"]}{userx["counter"]}@{userx["domain"]}'
#     userx['counter'] += 1
#     print(userx["counter"])
#     return email


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


random_char(1)
email_gen = random_char(10) + "@gmail.com"

