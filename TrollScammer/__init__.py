import requests, json, names, random, time, string, datetime
from colorama import Fore, Back, Style

class TrollScammer:

    bad_url: str = ""
    bad_url_method: int = 0
    bad_url_username_name: str = ""
    bad_url_password_name: str = ""
    username_char_between = []
    email_provider = []
    count_request = 0

################################################################################

#                       GET DATA FROM USER

################################################################################

    def __init__(self):
        with open('email_provider.json','r') as file:
            self.email_provider = json.loads(file.read())
        self.username_char_between = ["", ".", "-"]

    def get_variables_by_cli(self):
        self.bad_url = self.get_string_cli("Enter the server address:")
        self.bad_url_username_name = self.get_string_cli("What is the transfer parameter for the username?")
        self.bad_url_password_name = self.get_string_cli("What is the transfer parameter for the password?")
        self.bad_url_method = self.get_numselect_cli("Should the data be transmitted via 1) GET or 2) POST", 2)

    def get_string_cli(self,input_message: str) -> str:
        while True:
            print(Fore.YELLOW+input_message+Style.RESET_ALL)
            input_val = input("> ")
            if isinstance(input_val, str) and len(input_val) >= 1:
                return input_val
            else:
                print(Fore.RED+"invalid value -> try again"+Style.RESET_ALL)

    def get_numselect_cli(self, input_message: str, max_value: int) -> int:
        while True:
            print(Fore.YELLOW+input_message+Style.RESET_ALL)
            input_val = input("> ")
            if input_val.isnumeric() and int(input_val) >= 1 and int(input_val) <= max_value:
                return int(input_val)
            else:
                print(Fore.RED+"invalid value -> try again"+Style.RESET_ALL)

################################################################################

#                       START HEADER

################################################################################

    def print_query_information(self):
        print(Fore.GREEN+"""
              _   _              _     _     _     _                         _   _             _
             | | (_)            | |   (_)   | |   (_)                       | | | |           | |
   __ _ _ __ | |_ _ ______ _ __ | |__  _ ___| |__  _ _ __   __ _ ______ __ _| |_| |_ __ _  ___| | __
  / _` | '_ \| __| |______| '_ \| '_ \| / __| '_ \| | '_ \ / _` |______/ _` | __| __/ _` |/ __| |/ /
 | (_| | | | | |_| |      | |_) | | | | \__ \ | | | | | | | (_| |     | (_| | |_| || (_| | (__|   <
  \__,_|_| |_|\__|_|      | .__/|_| |_|_|___/_| |_|_|_| |_|\__, |      \__,_|\__|\__\__,_|\___|_|\_\\
                          | |                               __/ |
                          |_|                              |___/
        """+Style.RESET_ALL)
        print("github sourcecode: https://github.com/uvulpos/anti-phishing-attack")
        print("-----------------------------------------------")
        print(Fore.GREEN+"target-addr: " + Style.RESET_ALL + self.bad_url)
        if self.bad_url_method == 1:
            print(Fore.GREEN+"target-method:" + Style.RESET_ALL + " GET")
        else:
            print(Fore.GREEN+"target-method:" + Style.RESET_ALL + " POST")
        print(Fore.GREEN+"target-username-name: " + Style.RESET_ALL + self.bad_url_username_name)
        print(Fore.GREEN+"target-password-name: " + Style.RESET_ALL + self.bad_url_password_name)
        print("-----------------------------------------------")

################################################################################

#                       CREATE RANDOM STRINGS

################################################################################

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

################################################################################

#                       CREATE REQUEST

################################################################################

    def create_request(self, username: str, password: str) -> bool:
        # request
        if self.bad_url_method == 1:
            payload = {self.bad_url_username_name:username,self.bad_url_password_name:password}
            result = requests.get(self.bad_url, allow_redirects=False, params=payload)
        else:
            payload = {self.bad_url_username_name:username,self.bad_url_password_name:password}
            result = requests.post(self.bad_url, allow_redirects=False, data=payload)
        self.count_request += 1

        # output
        format_status = Fore.RED+"[ "+str(result.status_code)+" ]"+Style.RESET_ALL
        if result.status_code == 200:
            format_status = Fore.GREEN+"[ "+str(result.status_code)+" ]"+Style.RESET_ALL

        format_number: str = Style.DIM+self.create_numstring_min_length(str(self.count_request))+Style.RESET_ALL
        format_datetime: str = Fore.BLUE+"["+datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")+"]"+Style.RESET_ALL
        format_username: str = self.create_string_min_length(username, 35)

        format_key_username: str = Fore.YELLOW+"username:"+Style.RESET_ALL
        format_key_password: str = Fore.YELLOW+"password:"+Style.RESET_ALL

        print(f"{format_datetime} {format_status} {format_number} {format_key_username} {format_username} - {format_key_password} {password}")

################################################################################

#                   BEAUTIFY OUTPUT FUNCTIONS

################################################################################

    def create_numstring_min_length(self, value: str, min_length: int = 5):
        return self.create_string_min_length(value, min_length, "0", True)

    def create_string_min_length(self, value: str, min_lenth: int, fill_with: str = " ", leading: bool = False) -> str:
        extra_whitespace_len: str = "".join(fill_with for i in range(min_lenth - len(value)))
        if leading:
            return_value: str = extra_whitespace_len + value
        else:
            return_value: str = value + extra_whitespace_len
        return return_value
