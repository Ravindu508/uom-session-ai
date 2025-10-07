

#project euler problems
#problem2  
def even_fib(limit):
    first,second=1,2
    total=2
    new=first+second
    while new<limit:
        first,second=second,new
        if new%2==0:
            total+=new
        new=first+second
    print (total)
even_fib(4000000)


#problem3
def largest_prime_factor(n):
    i=2
    
       
    while i*i<=n:
        if n%i!=0:
            i+=1
        else:
            value=2
            while value * value <= i:
                  if i % value != 0:
                         value += 1
                  else:
                     break
            else:
              final_val = i

            i=i+1      
    print(final_val)  

largest_prime_factor(600851475143)        
            
 #problem4     
def largest_palindrome_product():
    max_palindrome=0
    for i in range(100,1000):
        for j in range(i,1000):
            answer=i*j
            if str(answer)==str(answer)[::-1] and max_palindrome<=answer:
                  max_palindrome=answer
    return max_palindrome
print(largest_palindrome_product())       

#promblem5
def smallest_multiple():
    activity=True;
    n=2520
    while activity:
        n=n+1
        for i in range(11,20):
            if n%i!=0:
                break
        else:
            activity=False
            print(n)
smallest_multiple() 

#problem6
def sum_square_difference(n):
     sum1=0
     sum2=0
     for i in range(1,n+1):
         sum1+=i**2
         sum2+=i
     else:
         print(sum2**2-sum1) 
sum_square_difference(100)
