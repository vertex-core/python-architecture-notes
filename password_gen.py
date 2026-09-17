import secrets
import string

power_of_password = input("How much hard will be your password(1,2,3,4): ")

my_list = []

secure_gen = secrets.SystemRandom()

secure_gen.shuffle(my_list) 
