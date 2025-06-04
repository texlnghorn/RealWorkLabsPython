import string


#
# Finds all lowercase English letters that are not present in the input string.
#
# @param input_string The string to check for used letters.
# @returns A string containing all lowercase English letters that were not found in the input string,
# in alphabetical order.
#
def find_unused_letters(input_string):
    # Create a dictionary to store the presence of each lowercase English letter.
    # Initialize all letters to false, indicating they have not yet been observed.
    lowercase_alphanumeric_dict = {char: False for char in string.ascii_lowercase}

    # Check if the input string exists and has content.
    if input_string and len(input_string) > 0:
        # Iterate over every character in the input string.
        for letter in input_string.lower():
            # Check if the character is a lowercase English letter.
            if letter.isalpha():
                # If the letter is seen, update its value in the dictionary to true.
                lowercase_alphanumeric_dict[letter] = True

    # Build the output string with letters that were not used.
    output = ""
    # Iterate through the map entries. Keys are already in alphabetical order due to initialization.
    for key, value in lowercase_alphanumeric_dict.items():
        # If the value is false, it means the letter was not found in the input string.
        if not value:
            output += key
    return output
