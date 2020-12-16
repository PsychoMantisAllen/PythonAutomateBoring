import pyperclip
import re

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# sample 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|\sx)         # extension word-part (optional)
(\d{2,5}))?                 # extension number-part (optional)

''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# sample some.+_thing@some.+_thing.com/edu etc

[a-zA-Z0-9_.+]+             # name part
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain name part 

''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)

# if we run the result here we will see phone is in tuple since it is constructed by groups
# while email is only one group
# to solve this, simply just add parenthesis to make it as one group
phoneRegex = re.compile(r'''
# sample 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|\sx)         # extension word-part (optional)
(\d{2,5}))?                 # extension number-part (optional)
)

''', re.VERBOSE)

# and since the phone number we actually want is the first item in the tuple
# we need to only extract a group of it
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)

# Copy the extracted email/phone to the clipboard
# since the results are in a list format and there is quote mark
# we want to have pure phone number and email followed line-by-line
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

