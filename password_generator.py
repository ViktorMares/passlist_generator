#!/usr/bin/env python3

from datetime import date
import argparse

parser = argparse.ArgumentParser(description='A simple script to generate passswords for account brute-forcing')

# Add command-line arguments
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument('-k','--keyword', help='Specify a keyword to generate passwords from',type=str, required=True)
requiredNamed.add_argument('-w','--word', help='Specify an optional second word to generate more complex passwords',type=str, required=False)
args = parser.parse_args()

# Define all variables that will be used in the creation of the passwords
characters = ['!', '@', '#', '$', '&', '*', '=', '+', '~']
delimiters = ['.', '_', '-']

keyword_lower = args.keyword.lower()
keyword_upper = args.keyword.capitalize()

current_year = str(date.today().year)
last_year = str(date.today().year - 1)
current_year_short = str(date.today().year).replace('20', '')
last_year_short = str(date.today().year - 1).replace('20', '')

# Check if second argument is passed
if args.word is not None:
    word_lower = args.word.lower()
    word_upper = args.word.capitalize()

# Create an empty list to store generated passwords
pass_list = []

# Start generating passwords from given arguments
if args.word is None:
    pass_list.append(keyword_lower + current_year_short)
    pass_list.append(keyword_lower + last_year_short)
    pass_list.append(keyword_upper + current_year_short)
    pass_list.append(keyword_upper + last_year_short)
    pass_list.append(keyword_lower + current_year)
    pass_list.append(keyword_lower + last_year)
    pass_list.append(keyword_upper + current_year)
    pass_list.append(keyword_upper + last_year)
    for c in characters:
        pass_list.append(keyword_lower + current_year_short + c)
        pass_list.append(keyword_lower + last_year_short + c)
        pass_list.append(keyword_upper + current_year_short + c)
        pass_list.append(keyword_upper + last_year_short + c)
        pass_list.append(keyword_lower + current_year + c)
        pass_list.append(keyword_lower + last_year + c)
        pass_list.append(keyword_upper + current_year + c)
        pass_list.append(keyword_upper + last_year + c)
else:
    for d in delimiters:
        pass_list.append(keyword_upper + d + word_upper)
        pass_list.append(keyword_upper + d + word_lower)
        pass_list.append(keyword_lower + d + word_upper)
        pass_list.append(keyword_lower + d + word_lower)
        pass_list.append(keyword_upper + d + word_upper + current_year)
        pass_list.append(keyword_upper + d + word_lower + current_year_short)
        pass_list.append(keyword_lower + d + word_upper + last_year)
        pass_list.append(keyword_lower + d + word_lower + last_year_short)

        for c in characters:
            pass_list.append(keyword_upper + d + word_upper + c)
            pass_list.append(keyword_upper + d + word_lower + c)
            pass_list.append(keyword_lower + d + word_upper + c)
            pass_list.append(keyword_lower + d + word_lower + c)
            pass_list.append(keyword_upper + d + word_upper + current_year + c)
            pass_list.append(keyword_upper + d + word_lower + current_year_short + c)
            pass_list.append(keyword_lower + d + word_upper + last_year + c)
            pass_list.append(keyword_lower + d + word_lower + last_year_short + c)


# Remove non unique passwords, sort them & print them out
unique_pass_list = sorted(list(dict.fromkeys(pass_list)))
for pw in unique_pass_list:
    print(pw)
