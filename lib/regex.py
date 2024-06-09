import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r""
name_regex =  re.compile(r"^[A-Za-z]+(?:['’][A-Za-z]+)?(?:-[A-Za-z]+(?:['’][A-Za-z]+)?)?\s[A-Za-z]+(?:['’][A-Za-z]+)?(?:-[A-Za-z]+(?:['’][A-Za-z]+)?)?$")

phone_number = r""
phone_regex =  re.compile(r'^\d{3}-\d{3}-\d{4}$')

email_address = r""
email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
