class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = [] # Empty credentials list

    def __init__(self,handle,user_name1,password1):

      # docstring removed for simplicity

        self.handle = handle
        self.user_name1 = user_name1
        self.password1 = password1
        
    def save_credentials(self):

        '''
        save_contact method saves contact objects into credentials_list
        '''

        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        
        '''
        delete_credentials method deletes a saved user from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_by_user_name1(cls,user_name1):
        
        for credentials in cls.credentials_list:
            if credentials.user_name1 == user_name1:
                return credentials
            
    @classmethod
    def credentials_exist(cls,user_name1):
        '''
        Method that checks if a user exists from the user list.
        Args:
            user_name: Username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for credentials in cls.credentials_list:
            if credentials.user_name1 == user_name1:
                    return True

        return False     
              
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list         
              
