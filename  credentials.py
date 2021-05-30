class Password:
    pass
    # Class that generates new instances of passwords.
    password_list = []


def save_password(self):
    Password.password_list.append(self)


def __init__(self, username, email, phone_number, password):

    # username: New password username.
    # email: New password email.
    # number: New password number.
    #password: New password.

    self.username = username
    self.email = email
    self.phone_number = phone_number
    self.password = password


new_password = Password("Melby01", "melbyokozi11@gmail.com", "0718818642", "Orinah8644")
print(new_password)

 