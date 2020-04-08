class pokemon:
    def __init__(self, name, level, health, max_health, p_t, is_knocked_out):
        self.name=name
        self.level=level
        self.health=health
        self.max_health=health
        self.p_t=p_t
        self.is_knocked_out=is_knocked_out
    def lose_health(self, points):
        self.health -= points
        if self.health <= 0:
            self.knock_out()
        print("Your {} has lost health your new health is {} it was {}!".format(self.name, self.health, self.health+points  ))  
            
        pass
    
    def gain_health(self, points):
        self.health += points
        if self.health >= self.max_health:
            self.health=self.max_health  
        print("{} gained health".format(self.name))
    def knock_out(self):
        self.knock_out=True
        print("Oh no {} you have been knocked out".format(self.name))
        pass
    def revive(self):
        pass
        
    def attack(self, opponent):
        if self.p_t.lower()=="grass" and opponent.p_t.lower()=="water":
            opponent.lose_health(2*self.level)
            print("grass beats water {} lose {} points".format(opponent.name, 2*self.level))
        if self.p_t.lower()=="water" and opponent.p_t.lower()=="fire":
            opponent.lose_health(2*self.level)
            print("water beats fire {} lose {} points".format(opponent.name, 2*self.level))        
        if self.p_t.lower()=="fire" and opponent.p_t.lower()=="grass":
            opponent.lose_health(2*self.level)
            print("fire beats grass {} lose {} points".format(opponent.name, 2*self.level))
        if self.p_t.lower()=="water" and opponent.p_t.lower()=="grass":
            opponent.lose_health(0.5*self.level)
            print("grass beats water {} lose {} points".format(opponent.name, 0.5*self.level))
        if self.p_t.lower()=="fire" and opponent.p_t.lower()=="water":
            opponent.lose_health(0.5*self.level)
            print("water beats fire {} lose {} points".format(opponent.name, 0.5*self.level))        
        if self.p_t.lower()=="grass" and opponent.p_t.lower()=="fire":
            opponent.lose_health(0.5*self.level)
            print("fire beats grass {} lose {} points".format(opponent.name, 0.5*self.level))
   
   
charazard=pokemon("charazard",700,700,700,"fire",False)

lapras=pokemon("lapras",500,500,500,"water",False)

snorlax=pokemon("snorlax",400,400,400,"normal",False)

zapdos=pokemon("zapdos",1000,1000,1000,"water",False)
    
zapdos.lose_health(40)
    
venasaur=pokemon("venasaur",500,500,500,"grass",False)
    

    
blastois=pokemon("blastois",600,600,600,"water",False)
  
venasaur.attack(blastois)  

 
class trainer:
    def __init__(self, name, potions, poke_list, cap):
        self.name=name
        self.potions=potions
        self.poke_list=poke_list
        self.cap=cap
    def use_potion(self, pokemon):
        potion=self.potions.pop()
        if potion=="normal":
            print("{} used normal potion on {}".format(self.name, pokemon.name))
            pokemon.gain_health(60)
        if potion=="super":
            print("{} used super potion on {}".format(self.name, pokemon.name))
            pokemon.gain_health(100)
        if potion=="ultra":
            print("{} used ultra potion on {}".format(self.name, pokemon.name))
            pokemon.gain_health(200)
    def attack(self, opponent):
        A=self.cap
        D=opponent.cap
        print("{}'s {} attacked {}'s {} because Jeffrey deserves to win".format(self.name, self.cap.name, opponent.name, opponent.cap.name))
        A.attack(D)
    def ap(self, pokemon):
        self.cap=pokemon
        print("{} just switched his pokemon to {}".format(self.name, pokemon.name))
        
    




Jeffrey=trainer("Jeffrey", ["ultra"], [zapdos, blastois, venasaur], zapdos)
Red=trainer("Red", ["ultra"], [charazard, lapras, snorlax], charazard)
Jeffrey.use_potion(zapdos)
Jeffrey.attack(Red)
Jeffrey.ap(blastois)

    
print("Jeffrey beats Red, Jeffrey is the new pokemon champion with his Zapdos")
    
