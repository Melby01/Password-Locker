import unittest
from password import Password

class TestPassword(unittest.TestCase):
   
    def setUp(self):
        def test_init(self):
            
            self.assertEqual(self.new_password.username,"Melby01")
            self.assertEqual(self.new_password.email,"melbyokozi11@gmail.com")
            self.assertEqual(self.new_password,phone_number,"0718818642")
            
    def test_save_password(self): 
        self.new_password.save_password() 
        self.assertEqual(len(Password.password_list),1)
        
    def test_save_multiple_password(self):
        self.new_password.save_password()
        test_password = Password("Test","Melby01","melbyokozi11@gmail.com","0718818642")
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)
           
if __name__ == '__main__':
    unittest.main()