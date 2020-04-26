# correct way

def print_personal_data(first_name: str, last_name: str, year_of_birth: int, city: str, email: str, phone: str):
    """
    The function prints in one row personal data
    :param first_name: first name
    :param last_name: last name
    :param year_of_birth: year of birth
    :param city: home city
    :param email: e-mail
    :param phone: phone number
    :return: None
    """

    print(f"First name: {first_name}", end="; ")
    print(f"Last name: {last_name}", end="; ")
    print(f"Year of birth: {year_of_birth}", end="; ")
    print(f"Home city: {city}", end="; ")
    print(f"E-mail: {email}", end="; ")
    print(f"Phone number: {phone}")

    print("Thank you for your assistance!")


# another way, wrong one

def print_personal_data_2(**kwargs):
    """
    The function prints in one row personal data
    :param kwargs: named parameters
    :return: None
    """

    for k, v in kwargs.items():
        print(f"{k}: {v}", end="; ")

    print("")
    print("Thank you for your patience!")
