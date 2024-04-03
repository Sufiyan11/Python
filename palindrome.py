def palindrome(s,i,j):
    if j>i:
        if s[i]!=s[j]:
            return 1
        i=i+1
        j=j-1
        return palindrome(s,i,j)

s=input('Enter the sentence :')
n=len(s)
if palindrome(s,0,n-1)==1:
    print(s,'is not palindrome')
else:
    print(s,'is a palindrome')
