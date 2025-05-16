import string 
alpha={}
print(string.ascii_lowercase)
for i in string.ascii_lowercase:
    alpha[i] = 0
print(alpha)
sentence = input("Please enter your panGRAm here").lower()
for i in sentence:
    if i in alpha:
        print(i)
        alpha[i]=alpha[i]+1

print(alpha)        
count = 0
for i in alpha:
    if alpha[i]>=1:
         count=count+1
if count==26:
    print("Its a pangram!")
else:
    print("Its not a pangram.")
   