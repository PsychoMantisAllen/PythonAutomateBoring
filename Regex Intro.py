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

batRegex = re.compile(r'Bat(wo)?man')  # can take 0 or 1 time of wo in front of man, similar to batman or batwoman
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The adventures of Batwowowoman')
print(mo.group())

# this can apply to the phone case as well
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

# if we want the case to match 0 or more times
batRegex = re.compile(r'Bat(wo)*man')
# if we want the case to match 1 or more times
batRegex = re.compile(r'Bat(wo)+man')
# if we want to look for same cases in rows with certain times (say 3 times)
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
phoneRegex.search('My number are 415-555-1234,555-4242.212-555-0000')
# if we want to look for cases in rows with certain times that sits in a boundary (say min 3 and max 5)
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3,5}')
# we can set the max or min as unbounded
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3,}')
# here is another example
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))
# here we notice that Python matches 5 digits out of the 3 digit and 4 digit options
# this is because Python uses greedy match to match the longest possible string
# if we want to do a non-greedy match, we just need to put a question mark behind
digitRegex = re.compile(r'(\d){3,5}?')



