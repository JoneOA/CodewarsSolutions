def expanded_form(n):
    i = -1
    output = ""
    for b in str(n):
        if str(n)[i] != "0":
            if output == "":
                output = str(n)[i] + "" + "0"*(-i-1) + output
            else:
                output = str(n)[i] + "" + "0"*(-i-1) + " + " + output
        i -= 1
    return output

print(expanded_form(707070))