#Can be solved using .isalnum() but that seems to defeat the purpose of the excercise

def alphanumeric(password):
    alphaNum = "abcdefghijklmnopqrstuvwxyz0123456789"
    passw = password.lower()
    inPass = 0
    for a in passw:
        for b in alphaNum:
            if a == b:
                inPass += 1
                break
    if inPass == len(password) and len(password) != 0:
        return True
    else:
        return False

print(alphanumeric("PassW0rd"))