class User:
    """
    Class that generates new instances of contacts
    """
    user_list = [] # Empty user list

    def __init__(self,user_name,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.password = password

        
    def save_user(self):
    
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self) 
        
    def delete_user(self):
    
        '''
        delete_contact method deletes a saved user from the user_list
        '''

        User.user_list.remove(self) 
           
    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in user_name and returns a contact that matches that number.
        Args:
            user_name: User_name to search for
        Returns :
            User that matches the user_name.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user
              
    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            user_name: Username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                    return True

        return False  
      
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list