# object are a construct for story data and functions together
# when creating an object we start with the class keyword.
# This acts like our object maker/ our blueprint

#(class CarMaker:
       def __init__(self, name, color, seating, year, model, miles): # initializes the blueprint
               self.name = name
                self.color = color
                self.seating = seating
                self.year = year
                self.model = model
                self.miles= miles

       def printInfo(self):
                       #print('heres your car faqs')
                       #print('name: '+ self.name)
                       #print('year: '+ str( self.year))
                       #print('miles '+ str( self.miles))
       def windshieldwippers(self):
                       #print('when raining turn on')
                
       def airbag(self):
                       #print('when driving a certain speed anc a collision happens; open')
                
                
       def turnsignals(self,up,down):
                       #if up:
                        #        print("turn left")
                       #elif down:
                        #      print("turn right")
                       #else:
                        #      print("dont turn signals on")
               
       #def bluetooth(year):
        #               if year > 2020:
         #                     print('you have bluetooth')
          #             else:
           #                   print("no bluetooth on this model")

#carOption1 = CarMaker('carolla','black','2','2024','carolla',20000)
#print(carOption1)

#carOption1.printInfo()



class phone:
        def __init__(self, model, brand,storage,time,number ):
                self.model = model
                self.brand = brand
                self.storage = storage
                self.time = time
                self.number = number
        def phoneinfo(self):
                print('model:',self.model)
                print('brand',self.brand)
                print('storage',self.storage)
                print('time',self.time)
                print('ring ring ring hello?' 'number:'+ self.number)




phone1 = phone('Iphone15','Apple','1 TB','12:20','215 768 9153')
print(phone1)
                




















#class instaProfile:
    #def __init__(self, username, email, profileImg, pw, bio):
        #self.username = username
        #self.email = email
        #self.profileImg = profileImg
        #self.pw = pw
        #self.bio = bio

    #def printInfo(self):
            #print(self.username,)
            #print('email')
    #def resetPw(self):
            #print('2-step auth...')
        
    #def uploadPicture(self):
            #print('instructions')

    #def viewFollowers(self):
            #print(['list of other followers'])

#profile1 = instaProfile('Ian','ik@aoil.com','pic.png','123','lorem ipsum')
#profil2 = instaProfile('Rob','')


#profile.printInfo()