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
        
     
    def test_delete_password(self):
        self.new_password.save_password()
        test_password = Password("Test","Okozi01","okozimelby11@gmail.com","0798118444","Orina8644")
        test_password.save_password()
        
        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1)
        
           
if __name__ == '__main__':
    unittest.main()