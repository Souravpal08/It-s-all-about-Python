Name1= input("Write your full name:")
Name2= input("Write His/Her full name:")
combine_string= Name1+Name2
lowercase_string= combine_string.lower()

#here we will count the number of these letters in given name
t= lowercase_string.count('t')
r= lowercase_string.count('r')
u= lowercase_string.count('u')
e= lowercase_string.count('e')
true=t+r+u+e

l= lowercase_string.count('l')
o= lowercase_string.count('o')
v= lowercase_string.count('v')
e= lowercase_string.count('e')
love=l+o+v+e

#concatination of two strings

Love_score= int (str(true)+str(love))
if Love_score<10 or Love_score>90:
    print(f"Your score is {Love_score} and both of you made for each other..!! ")
elif Love_score>=50:
    print(f"Your score is {Love_score} and you are alright to go ahead")
else:
 print(f"Your score is {Love_score}.May go bless you")