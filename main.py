import requests
import json
import names
import random
import time
import string

class TrollScammer:

    bad_url: str = ""
    username_char_between = []
    email_provider = []

    def __init__(self):
        with open('email_provider.json','r') as file:
            self.email_provider = json.loads(file.read())
        self.username_char_between.append("")
        self.username_char_between.append(".")
        self.username_char_between.append("-")
        self.username_char_between.append("_")

    def create_username(self) -> str:
        try:
            username: str = ""
            username: str = names.get_full_name()
            username: str = username.replace(" ", random.choice(self.username_char_between))

            if random.randint(0,1) >= 1:
                username = username.lower()
            if random.randint(0,1):
                username = username + "@" + str(random.choice(self.email_provider))
        except Exception as e:
            username = self.create_username()

        return str(username)

    def create_password(self) -> str:
        password = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(random.randint(4, 30)))
        return password

    def create_request(self, username: str, password: str) -> bool:
        print("username: "+self.create_string_min_length(username, 35)+" - password: "+password)
        pass

    def create_string_min_length(self, value: str, min_lenth: int) -> str:
        return_value: str = ""
        length_value: int = len(value)
        extra_whitespace_len: str = "".join(" " for i in range(min_lenth - length_value))
        return_value: str = value + extra_whitespace_len
        return return_value

if __name__ == "__main__":
    instance = TrollScammer()
    while True:
        username: str = instance.create_username()
        password: str = instance.create_password()
        instance.create_request(username, password)
        time.sleep(0.5)
        # time.sleep(random.randint(1, 100)   / 10)
