def isPhoneNumber(text):
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # no area code
    if text[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # no first 3 digits
    if text[7] != '-':
        return False  # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # no last 4 digits
    return True


print(isPhoneNumber('415-555-1234'))

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office number'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')

# this would be a normal way to code and find the phone numbers. However, it would be an easier case if using regex
import re
message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office number'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

# if we want to find all phone numbers in the msg, add findall(), it will return a list of all the values
mo = phoneNumRegex.findall(message)
print(mo)

# if we want to put results into group, simply segregate them using parenthesis
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
mo.group()
print(mo.group(1))
print(mo.group(2))

# if the phone number format is like this (415) 555 - 4242
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is (415) 555-4242')
mo.group()

# if we are looking for words with the same prefix
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
print(mo.group(1))
# beware that when the search could not find the corresponding item, it will store a boolean False value
# in this case we cannot use group() to check the item, instead we will
mo = batRegex.search('Batadmin lost a wheel')
print(mo == None)


