import string
import random

def generate_random_string(size=6, chars=string.ascii_lowercase, prefix="", suffix=""):
    """generates a random string of 

    Args:
        size (int, optional): size of the generated string. Defaults to 6.
        chars (_type_, optional): sequence to choose from, fed to random.choice. Defaults to string.ascii_lowercase.
        prefix (str, optional): this will be tacked in front if present. Defaults to "".
        suffix (str, optional): this will be tacked at the end if present. Defaults to "".

    Returns:
        str: prefix + randomly generated string of length size chosen from chars 
    """
    random_string = "".join(random.choice(chars) for _ in range(size))
    return "".join((prefix, random_string, suffix))