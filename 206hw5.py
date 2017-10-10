import os

import pprint
import re

def readtxtNumber(file):
#https://codereview.stackexchange.com/questions/126363/shortest-regex-search-and-sum-for-integers
#http://www.pythonforbeginners.com/basics/list-comprehensions-in-python        
        
        
        with open(file, 'r') as f:
                result = sum(int(value) for value in re.findall('[0-9]+', f.read()))
        print(result)


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	
	
	total = readtxtNumber('regex_sum_32547.txt')
	
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

