'''s = input("Enter a string you want to reverse: ")
print(s[::-1]) '''

''' s = "hello"
rev = ""
for i in s:
     rev=i+rev
print(rev) '''

s = input("Enter a string to reverse: ")
rev = ""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print(rev)