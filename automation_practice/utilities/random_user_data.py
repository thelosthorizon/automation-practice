
from utilities import common

USERDATA_DYNAMIC = {
    "First name": "{random_string}FirstName",
    "Last name": "{random_string}LastName",
    "Email": "{random_string}@test.automation.practice.com", 
    "Password": "{random_string}Test123.",
    "Address": "{random_string}Address",
    "City": "{random_string}City",
}

USERDATA_STATIC = {
    "State": "Alabama",
    "Postal Code": 12345,
    "Country": "United States",
    "Mobile Phone": 123456789,
    "Address Alias": "My Address"
}

def generate(prefix=""):
    """generate random user data

    Args:
        prefix (str, optional): prefix to use when generating user data. Defaults to "".

    Returns:
        dict: a dict containing user data
    """
    user_data = dict(USERDATA_DYNAMIC)
    for key, value in user_data.items():
        user_data[key] = value.format(random_string=common.generate_random_string(prefix=prefix, size=3))
    user_data.update(dict(USERDATA_STATIC))
    return user_data

if __name__=="__main__":
    print(generate("SG"))