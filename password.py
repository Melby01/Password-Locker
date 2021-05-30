class Password:
    """
    Class that generates new instances of passwords.
    """
    def __init__(self, username, email, phone_number):
         
          """
          username: New password username.
          email: New password email.
          number: New password number.
          """
          self.username = username
          self.email = email
          self.phone_number = number
 
         
new_password = Password( )
print(new_password)