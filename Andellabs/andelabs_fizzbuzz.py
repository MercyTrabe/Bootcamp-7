

# Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.

# When the number is not divisible by 3 or 5, the number itself should be returned.




def fizz_buzz(a):


    if  a % 3 == 0 and a % 5==0 :
    	return "fizzbuzz"
    if a % 3 == 0:
    	return "fizz"
    if a % 5 == 0:
    	return "buzz"
    else:
      return a


