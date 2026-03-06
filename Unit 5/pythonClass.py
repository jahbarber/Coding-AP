# import random


grocery= ['apple','water']
grocery.append('cookies')

# A Class is a special construct for creating objects - it is the 
# blueprint/ machine for making objects

class Insta_Profile:
    def __init__(self, username, email, location, skills):
        self.username = username
        self.email = email
        self.locaion = location
        self.skills = skills
        





    # Insta_Profile(usernmae, email)
    #  Objects are the blueprint for data

    #  Ex. a job application has the same questions but everyones data
    #  is going to be different
# x = random.randint(0,1)
Profile_1= Insta_Profile("EmilTheBoss", 'etbe@gmail.com',0,[])
Profile_2= Insta_Profile("CoolGuy","cg@apple.com")

print(Profile_1)
print(Profile_1.username)
