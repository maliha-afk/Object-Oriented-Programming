#class coffee:
    #Milk=50
    #coffee=50
    #def greet():
        #print("Good morning Mr.coffee!")

#cappuccino= coffee()
#print(cappuccino.Milk)
#print(cappuccino.greet)
#print(cappuccino.coffee)



#class car:
    #wheel=4
    #AC=True
    #seats=6
    #def speed():
    #    print("Too Fast!")


#audi=car()
#bmw=car()
#tayota=car()
#lamborghini=car()
#Nissan=car()

#print(Nissan.speed)


class car:
    def __init__(self,name,model,seat,price,AC):
      self.name=name
      self.model=model
      self.seat=seat
      self.price=price
      self.AC=AC

bmw=car("BMW","V8",6,"90000$",True)

print(bmw.price)
    
  