def is_palindrome(n):
    temp=n 
    rev=0
    ans = True 
    while(n>0): 
        dig=n%10 
        rev=rev*10+dig 
        n=n//10 
    if(temp==rev): 
        ans = True
    else: 
        ans = False 
    return ans


def check_palindrome():
    for i in range(100000,999999,1):

        four_last_digits = i % 10000
        five_last_digits_after_plus1 = (i+1) % 100000
        five_last_digits_after_plus2= (i+2) % 100000
        four_middle_digits_after_plus2= int(five_last_digits_after_plus2/10)
        num_plus3 = i+3

        if is_palindrome(four_last_digits) and is_palindrome (five_last_digits_after_plus1) and is_palindrome (four_middle_digits_after_plus2) and is_palindrome(num_plus3) and (four_last_digits/1000 > 1):
            print(i)
    

if __name__ == "__main__":
    # Question 2
    check_palindrome()