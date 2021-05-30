import unittest
from password import Password

class TestPassword(unittest.TestCase):
    
    #Test 1
    def setUp(self):
        def test_init(self):
            
            self.assertEqual(self.new_password.username,"Melby01")
            self.assertEqual(self.new_password.email,"melbyokozi11@gmail.com")
            self.assertEqual(self.new_password,phone_number,"0718818642")
            self.assertEqual(self.new_password,password,"Orinah8644")
            
    #Test 2
    def test_save_password(self): 
        self.new_password.save_password() 
        self.assertEqual(len(Password.password_list),1)
        
    #Test 3
    def test_save_multiple_password(self):
        self.new_password.save_password()
        test_password = Password("Test","Okozi01","okozimelby11@gmail.com","0798118444","Orinah8644")
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)
        
    def tearDown(self):
        Password.password_list = []
    def test_save_multiple_password(self):
        self.new_password.save_password()
        test_contact = Password("Test","Okozi01","okozimelby11@gmail.com","0798118444","Orina8644")
        
    #Test 4
    def test_delete_password(self):
        self.new_password.save_password()
        test_password = Password("Test","Okozi01","okozimelby11@gmail.com","0798118444","Orina8644")
        test_password.save_password()
        
        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1)
        
    def delete_password(self):
        Password.password_list.remove(self)
        
    #Test 5  
    def test_find_password_by_email(self):
    self.new_password.save_password()
    test_password = Password("Test","Okozi01","okozimelby11@gmail.com","0798118444","Orina8644")
    test_password.save_password()
    
    found_password =  Password.find_by_email(melbyokozi11@gmail.com)
    
    self.assertEqual(found_password.username,test_password.phone_number)
    
    @classmethod
    def find_by_email(cls,email):
        
        for email in cls.password_list:
            if password.email == email:
                return password
            
if __name__ == '__main__':
    unittest.main()
    
def test_password_exists(self):
        
        self.new_password.save_password()
        test_password = Password("Melby01", "melbyokozi11@gmail.com", "0718818642", "Orinah8644")  
        test_password.save_password()

        password_exists = Password.password_exist("Orinah8644")

        self.assertTrue(password_exists)
        
        @classmethod 
        def password_exist(cls,email):
            for password in cls.password_list:
                if password.email == email:
                    return True
            
            return False
        