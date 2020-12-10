"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string): # this is all O(n)
    answer_string = ""
    for char in string:
        ascii_char = ord(char) # ord() is used to convert to ascii
        # check if between 65 and 90
        if 65 <= ascii_char <= 90:
            # convert to lowercase
            lower_char_num = ascii_char + 32
            # convert the new ascii num back to character
            lower_char = chr(lower_char_num) # chr() changes back from ord into character
            # add lower_char to our answer_string
            answer_string += lower_char
        else:
            answer_string += char
            
    return answer_string

print(to_lower_case('LambdaSchool'))
# this is all O(n)
# to speed this up you would have to skip letters, making n smaller
# can you? no


# PLAN
    # use ascii #'s to find if lowercase or uppercase 
    # create empty answer_string
    # loop through each char of input_string
        # for each char convert to ascii
        # check if number is between 65 and 90  (uppercase)
            # lower case is 97-122 in ascii #'s for alphabetic letters
            # the letter is uppercase, so convert to lower
            # lower_char_num = converted_char + 32
            # convert the new ascii num back to character
            # lower_char = chr(lower_char_num)
            # add lower_char to our answer_string
        # else
            # add the character to answer_string (for the already lower-case letters)
            # even if there was a special character, it would fall into else
    # return answer_string