from string import ascii_letters, digits, punctuation
from random import choice, sample

def isEven(integer):
    """Return True if the input integer is even, False otherwise."""
    return integer % 2 == 0

def RandPass(size=8):
    """
    Generate a password with the specified size and categorize its strength.
    
    Parameters:
    - size (int): Length of the generated password. Default is 8.
    
    Returns:
    - new_password (str): The generated password.
    - strength (str): Strength category of the password.
    - colorVal (str): Color code representing the strength category.
    """
    special_chars = "!@#$%^&*- _~+-="  # Special characters
    letters = ascii_letters  # Upper and lower case letters
    digits_set = digits  # Digits 0-9
    
    # Combine character sets
    all_chars = special_chars + letters
    full_chars = all_chars + digits_set

    # Determine the length of each section of the password
    passlen = size
    if isEven(passlen):
        front_size = passlen // 5
    else:
        front_size = passlen // 2
    mid_size = 2
    remaining_size = passlen - (front_size + mid_size) - 1

    # Generate password sections
    pass0 = choice(special_chars)  # Ensure a special character is included
    pass1 = ''.join(sample(full_chars, front_size))
    pass2 = ''.join(sample(digits_set, mid_size))
    pass3 = ''.join(sample(all_chars, remaining_size))

    # Adjust if the password ends with a space
    if pass3.endswith(' '):
        pass3 = pass3[:-1] + choice(all_chars)
    
    # Combine all sections to form the final password
    new_password = pass0 + pass1 + pass2 + pass3
    
    # Determine password strength and corresponding color
    if passlen <= 8:
        strength = 'VERY WEAK'
        colorVal = "#6d0001"
    elif passlen <= 10:
        strength = 'WEAK'
        colorVal = "#cc0000"
    elif passlen <= 12:
        strength = 'DECENT'
        colorVal = "#fc8600"
    elif passlen <= 14:
        strength = 'GOOD'
        colorVal = "#eae200"
    elif passlen <= 16:
        strength = 'STRONG'
        colorVal = "#9ff400"
    elif passlen <= 18:
        strength = 'VERY STRONG'
        colorVal = "#007715"
    else:
        strength = 'EXCELLENT'
        colorVal = "#001fef"

    return new_password, strength, colorVal
