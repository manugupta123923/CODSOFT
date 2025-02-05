import random
import string

length = int(input("Enter password length: "))
password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase+ string.digits + string.punctuation, k=length))
print("Generated Password:",password)