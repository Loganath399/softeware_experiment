def login(username, password):
    return username == "admin" and password == "1234"


GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

print(BLUE + "============================" + RESET)
print(BLUE + "       LOGIN SYSTEM         " + RESET)
print(BLUE + "============================" + RESET)

username = input("Username: ")
password = input("Password: ")

if login(username, password):
    print(GREEN + "✔ Login successful" + RESET)
else:
    print(RED + "✘ Invalid credentials" + RESET)