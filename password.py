class Password: 
    pass 
  #Class that generates new instances of passwords.
  
password_list = []
def save_password(self):
      Password.password_list.append(self)
  
def __init__(self, username, email, phone_number):
          
         # username: New password username.
         # email: New password email.
         # number: New password number.
           
          self.username = username
          self.email = email
          self.phone_number = phone_number
 
         
new_password = Password("Melby01", "melbyokozi11@gmail.com", "0718818642")
print(new_password)