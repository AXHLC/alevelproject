def lengthscheck(string, nums, option):

    # option 1 is to check the nums of string is equal to the nums necessary
    if option == 1:
        if len(string) == nums:
            return True
        else:
            return False
    # option 2 is to check the nums of string is greater than or equal to the nums
    elif option == 2:
        if len(string) >= nums:
            return True
        else:
            return False
    # option 3 is to check the nums of string is less than or equal to the nums
    elif option == 3:
        if len(string) <= nums:
            return True
        else:
            return False

def emailcheck(email):
    import re
    # This variable is the format in which the email will be checked against
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    # if the email matches the format given then returns true otherwise returns false
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def passcheck(password):
    import re
    # this validates a string eneteres to include numbers, capital letters, and special characters
    if re.search('\d', password) and re.search(r'[A-Z]', password) and re.search('[+,?,#,£,$,%,&]', password):
        return True
    else:
        return False

def rangecheck(number, thresh):
    if number == thresh:
        return True
    else:
        return False

def prescheck(inp):
    while inp == "":
        return False
    else:
        return True

# testing
if __name__ == "__main__":
    #print(lengthscheck("b3338", 10, 3))
    #print(emailcheck("dirguhdfklj"))
    #print(passcheck("t8hareeAnonums"))
    #print(rangecheck(23, 53))
    print(prescheck("b"))



    # this is to check using terminal
#this is to check using terminalthis is to check using terminalthis is to check using terminalthis is to check using terminal
