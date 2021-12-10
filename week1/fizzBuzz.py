class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        my_list = []
        for i in range(1, n+1):
            if(i%3 == 0 and i%5 == 0):
                my_list.append("FizzBuzz")
            elif(i%3 == 0):
                my_list.append("Fizz")
            elif(i%5 == 0):
                my_list.append("Buzz")
            else:
                my_list.append(f"{i}")
                
        return my_list