import  random

lower_case=("abcdefghijklmnopqrstuvwxyz")
upper_case=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Num = ("0123456789")
sp_char=("!@#$%^&*_=)(")
sym = ("+-*/")
string = lower_case+upper_case+Num+sp_char+sym
length = 16
print("Welcome to password generator:")
password = "".join(random.sample(string,length))
print("Your 16 digit password is:"+password)