class Password: 
    pass 
  #Class that generates new instances of passwords.
  
    password_list = []
  
def __init__(self, username, email, phone_number):
          
         # username: New password username.
         # email: New password email.
         # number: New password number.
           
          self.username = username
          self.email = email
          self.phone_number = phone_number
 
         
new_password = Password("Melby01","melby11@gmail.com","0718818642")
print(new_password)