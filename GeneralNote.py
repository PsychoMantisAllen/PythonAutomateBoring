# difference between append() and insert() is that append() will add the value as the last item in the list
# while insert() we can just specify the index position
spam = ['cat', 'dog', 'pig', 'mouse']
print(spam)
spam.append('Cow')
print(spam)
spam.insert(2, 'ant')
print(spam)

# similar to addition, if we want to remove any index in the list, remove() can do that work
spam.remove('cat')
print(spam)
# or another way is to use del
del spam[0]
print(spam)

# for sort(), you can't sort a list with both integers and strings
# for strings only, uppercase comes first and following the lowercase
# to ignore this, we can use the following method
spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)

# mutable and immutable are something that we need to pay attention to
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)
# here we can see that cheese will not change even though spam has changed after assigning cheese equaling spam
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam)


# however, when a list is assigned, spam has followed the changes that have been assigned to cheese Python created
# this list and it's in the computer's memory but it was assigned a reference to this list so when we are assigning
# spam to cheese, we are creating another separate reference but they are referencing the same list
# Immutable values such as string and tuple don't have this problem because they cannot be modified "inplace".
# They can only be replaced by new values.
# While mutable values such as list are actually creating a reference when assigning to a variable
# so the list or the information is not actually stored in the variable

# this factor will usually cause some weird bugs
# a typical example is the global and local variable
def eggs(cheese):
    cheese.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)
# even though cheese is a local variable and thus append() should not have effect over the global variable
# however, since here spam is assigned only to a reference of the list
# the append() is actually making effect upon the actual list that is stored in the computer not in the variable
# it directly skips the difference between global and local variable

# why Python would love this reference feature?
# if we consider that a list contains millions items, in this case
# it would be a huge problem to copy that entire list every time you call the function
# so rather than copying the whole function, it would make more sense to copy the reference only

# if we really want to copy the whole list to a new variable (a new reference to a new set of list)
import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
# in this case, we are not going to make any changes to spam as there is a new list referencing to cheese


# if we want to have a list of the dictionary key or value or item, can use the following
eggs = {'name': 'Zophine', 'species': 'cat', 'age': 8}
list(eggs.keys())
list(eggs.values())
list(eggs.items())

# or we can use a for loop
for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

# if we want to get certain value from the dictionary, can use the following
eggs.get('age', 0)
eggs.get('color', '')  # the second option is to return value if not finding the key
# if we want to set value for a non-existed key in a dictionary
eggs.setdefault('color', 'black')
# setdefault() will not work if the key already exist, even if the value assigned before is empty
trial1 = {'hand': ''}
print(trial1)
trial1.setdefault('hand', 'yes')
print(trial1)

# try the following section
message = 'It was a bright hot day in December, and the clock is not moving anymore.'
count = {}
for character in message:  # if we want the count regardless of upper or lower case, add upper() after message
    count.setdefault(character, 0)  # if we don't include this we will receive a KeyError
    count[character] += 1

print(count)  # to get a better print result, can use pprint (need to import first) -- displaying dictionary value
# pformat() function returns a string value of this output

# here is an advanced string syntax -- raw string
r'Hello'
r'That is Carol\'s cat.'
print(r'That is Carol\'s cat.')
# multi-line string
print("""Dear Alice,
Eve's cat
and extortion
sincerely,
Bob.""")

# some extra string methods
# startswith() and endswith()
''.join(['cats', 'rats', 'bats'])
'\n\n'.join(['cats', 'rats', 'bats'])
print('\n\n'.join(['cats', 'rats', 'bats']))
# rjust() and ljust() and center() will add extra spaces on the left or right hand side of the string
# to make the len of the whole string equals to the assigned length
rtHello = 'Hello'.rjust(10)
print(rtHello)
print(len(rtHello))
# alternatively, we can change the spaces to some other contents
# but the fill character must be exactly one character long
rtHello = 'Hello'.rjust(20, '1')
print(rtHello)
# if we want to remove empty spaces on either side, can use strip(), lstrip() or rstrip()
"     12123       ".strip()
'    1212121'.lstrip()
'1231231         '.rstrip()
# reminder: only remove spaces from the left or right but not the middle
'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')

# concatenation in string would be time consuming if there are many strings that we want to add
# we can use conversion specifiers to help us ease the process
name = 'Alice'
place = 'Main street'
time = '6 pm'
food = 'turnips'
'Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)
