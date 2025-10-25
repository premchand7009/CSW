def validatepassword(password):
    errors = []

    if len(password) < 8:
        errors.append("At least 8 characters needed.")
    if not any(ch.isupper() for ch in password):
        errors.append("Need one uppercase letter.")
    if not any(ch.islower() for ch in password):
        errors.append("Need one lowercase letter.")
    if not any(ch.isdigit() for ch in password):
        errors.append("Need one digit.")
    if not any(ch in "!@#$%" for ch in password):
        errors.append("Need one special character (!@#$%).")
    if any(ch.isspace() for ch in password):
        errors.append("No spaces allowed.")

    if len(errors) == 0:
        return True
    else:
        return False, errors

pwd = input("Enter password: ")
result = validatepassword(pwd)

if result == True:
    print("Password is valid.")
else:
    print("Password is invalid:")
    for e in result[1]:
        print("-", e)
