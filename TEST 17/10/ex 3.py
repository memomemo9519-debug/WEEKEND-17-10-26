print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

email = input("What is your email?")
print(f"Thank you for your email,(name)")

phone_number = input("What is your phone number?")
print(f"Thank you for your phone number,(name)")

DOB = input("Enter your DOB (DD/MM/YYYY:)")
print(f"Thank you for your DOB,(name)")

with open("userdata.txt","w") as file:
    file.write(f"Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nDOB: {DOB}")