import random, time, TrollScammer

if __name__ == "__main__":
    debug: bool = False
    instance = TrollScammer.TrollScammer()
    instance.get_variables_by_cli()
    instance.print_query_information()
    try:
        while True:
            username: str = instance.create_username()
            password: str = instance.create_password()
            instance.create_request(username, password)
            if debug:
                time.sleep(0.5)
            else:
                time.sleep(random.randint(1, 30) / 10)
    except KeyboardInterrupt as k:
        print("")
