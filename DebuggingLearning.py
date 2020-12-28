def boxPrint(symbol, width, height):
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


boxPrint('*', 15, 5)
boxPrint('***', 15, 5)


# to debug like when the symbol input is not 1 character
def boxPrintDe1(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


boxPrintDe1('***', 15, 5)


# debug version 2
def boxPrintDe2(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater than 1.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


# to store the traceback information separately
import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written in error_log.txt')

# sometimes we will use assert to monitor bug
# if condition returns True then nothing happens; if not then AssertionError is raised
market_2nd = {'ns': 'green', 'ew': 'red'}


def swithlights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


print(market_2nd)
swithlights(market_2nd)
print(market_2nd)

# sometimes we can use logging to record the debugging information
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total


print(factorial(5))

logging.debug('End of program')

# we found that the range should not start from 0 but from 1, otherwise it will multiply by 0
# change range from (n + 1) to (1, n + 1)

# in the old way of debugging, we need to comment and uncomment the line to have a trial
# in the logging mode, a simply line will do the work
logging.disable(logging.CRITICAL)   # can change the level in the brackets
# there are 5 levels in logging (lowest to highest)
logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
# if we want to save the logging in an external file, change to current line
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

