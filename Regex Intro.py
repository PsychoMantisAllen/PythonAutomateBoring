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
    chunk = message[i:i + 12]
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

# remember that we use findall() method to return a list of strings that meets the criteria
# if we structure a bit more about the compile function, we will get tuples
resume = '123-321-1234 and what is another one again? 392-123-9484'
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneRegex.findall(resume)

# now try this one!
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
phoneRegex.findall(resume)

# \d - any numeric digit from 0 to 9
# \D - any character that is not a numeric digit from 0 to 9
# \w - any letter, numeric digit, or the underscore character (think of this as matching 'word' characters)
# \W - any character that is not a letter, numeric digit, or the underscore character
# \s - any space, tab, or newline character (think of this as matching 'space' characters)
# \S - any character that is not a space, tab or newline character

vowelRegex = re.compile(r'[aeiouAEIOU]')  # same as r'(a|e|i|o|u|A|E|I|O|U)'
print(vowelRegex.findall('Robocop eats baby food'))
# if we want two vowels in a row
vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall('Robocop eats baby food'))
# if we want all non-vowel letters, simply just put a carrot sign
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food'))

# starting with something or end with something in Regex
beginsWithHelloRegex = re.compile(r'^Hello')
endsWithWorldRegex = re.compile(r'world!$')
# if the text does not start with Hello or end with world! then it will return a None
# using both we can find the exact pattern in a string
allDigitsRegex = re.compile(r'^/d+$')

# adding a dot can represent any characters except for the new line
# it only looks for a single character
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat. At haha'))
# see here flat and at are not included, only lat for flat
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat. At haha'))
# this one can help with the flat, but we can see for others a space is included, not ideal

# (.*) finds anything after that, except for new line
nameRegex = re.compile(r'First Name: (.*) Last Name:(.*)')
print(nameRegex.findall('First Name: Allen Last Name: Yan'))
# returning a tuple of strings, see here if we change Last Name to without upper case, we will get a NONE

# to keep in mind, (.*) is greedy and (.*?) is non-greedy
serve = '<To serve humans> for dinner.>'
nonGreedy = re.compile(r'<(.*?)>')
print(nonGreedy.findall(serve))
isGreedy = re.compile(r'<(.*)>')
print(isGreedy.findall(serve))

# now let's see what except for new line means
prime = 'I take over the next arcade.\nWhat could the world have done to compromise me\nThat would be the abysmal.'
dotStar = re.compile(r'.*')
print(dotStar.search(prime))
# if we want everything including new lines
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))
# similarly we can have case insensitive while searching
vowelRegex = re.compile(r'[aeiou]', re.I)

# in Regex we can find and replace content
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub('REDATCTED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub(r'Agent \1xxxx', 'Agent Alice gave the secret documents to Agent Bob.'))

# to make Regex in python more readable, we can make it verbose
# this means allowing comments in Regex, using phone number as the example
# if we want to pass multiple arguments (re.DOTALL, re.IGNORECASE, re.VERBOSE)
# combine them with the | bitwise operator
phoneRegex = re.compile(r'''
(\d\d\d-)|             # area code (without parens, with dash)
(\(\d\d\d\))           # or area code with parens and no dash
\d\d\d                 # first 3 digits
-                      # second dash
\d\d\d\d               # last 4 digits
\sx\d{2,4}             # extension, like x1234''', re.VERBOSE | re.IGNORECASE | re.DOTALL)


