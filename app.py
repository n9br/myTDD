
class invalidValue(Exception):
    pass

def getUserData():
    # firstName = input ("Enter first name: ")
    firstName = "Karsten"
    return firstName

def verifyUserFirstName(user):
    try:
        user = str(user)
    except(ValueError):
        raise invalidValue
    
def verifyAge(age):
    try:
        age = int(age)
    except(ValueError):
        raise invalidValue

user = getUserData()
# user = 
verifyUserFirstName(user)
print(user)



