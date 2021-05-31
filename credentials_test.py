import unittest
import pyperclip
from password import Password

class TestPassword(unittest.TestCase):
    
    #Test 1
    def setUp(self):
        def test_init(self):
             
            self.assertEqual(self.new_password,number,"0718818642")
            self.assertEqual(self.new_password,password,"Orinah8644")
            
    #Test 2
    def test_save_password(self): 
        self.new_password.save_password() 
        self.assertEqual(len(Password.password_list),1)
        
    #Test 3
    def test_save_multiple_password(self):
        self.new_password.save_password()
        test_password = Password("Test","0798118444","Orinah8644")
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)
        
    def tearDown(self):
        Password.password_list = []
    def test_save_multiple_password(self):
        self.new_password.save_password()
        test_contact = Password("Test","0798118444","Orina8644")
        
    #Test 4
    def test_delete_password(self):
        self.new_password.save_password()
        test_password = Password("Test","0798118444","Orina8644")
        test_password.save_password()
        
        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1)
        
    def delete_password(self):
        Password.password_list.remove(self)
        
    #Test 5  
    def test_find_password_by_number(self):
     self.new_password.save_password()
    test_password = Password("Test","0798118444","Orina8644")
    test_password.save_password()
    
    found_password =  Password.find_by_number(0718818642)
    
    self.assertEqual(found_password.username,test_password.number)
    
    @classmethod
    def find_by_number(cls,number):
        
        for number in cls.password_list:
            if password.number == number:
                return password
            
 
    
def test_password_exists(self):
        
        self.new_password.save_password()
        test_password = Password("0718818642", "Orinah8644")  
        test_password.save_password()

        password_exists = Password.password_exist("Orinah8644")

        self.assertTrue(password_exists)
        
        @classmethod 
        def password_exist(cls,email):
            for password in cls.password_list:
                if password.email == email:
                    return True
            
            return False
        
def test_display_passwords(self):
    self.assertEqual(Password.display_passwords(),Password.password_list)
        