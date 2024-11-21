import re
import json


class User:
    users_file = "users.json"

    def __init__(self, firstname, email):
        self.firstname = firstname
        self.email = email

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname):
        if isinstance(firstname, str) and len(firstname) > 0 and firstname[0] != '@':
            self.__firstname = firstname
        else:
            raise ValueError('First name must be an alphanumeric string')

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        valid_email = re.fullmatch(regex, email)
        if valid_email:
            self.__email = email
        else:
            raise ValueError('Email is not valid')

    def save_user(self):
        # get all users first , append current user then save user again
        users = self.__class__.get_all_users()
        users.append(self.__dict__)
        try:
            with open(self.users_file, mode='w') as users_file:
                users_file.write(json.dumps(users, indent=4))

            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def get_all_users(cls):
        try:
            fileobject = open(cls.users_file)
            users = json.load(fileobject)
            fileobject.close()
        except FileNotFoundError:
            users = []

        return users





aya_account = User("Aya", "aya@gmail.com")
aya_account.save_user()

