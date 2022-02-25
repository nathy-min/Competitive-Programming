class Solution(object):
    def fizzBuzz(self, n):
        answer=[]
        for i in range(1,n+1):
            h=str(i)*(i%3!=0 and i%5!=0)+ "Fizz"*(i%3==0 and i%5!=0)+"Buzz"*(i%5==0 and i%3!=0)+"FizzBuzz"*(i%5==0 and i%3==0)
            answer.append(h)
        return(answer)