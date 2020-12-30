def question1():
    x= input("how are you today? \n good / bad \n ->")
    if x == "good":
        print("Awesome!")
        question2()

    elif x == "bad":
        print("sorry to hear that. But....")
        question2()
    else:
        print("uhh.... i dont understand")
        return question1()

def question2():
    y = input("would you like to have some ice-cream? \n yes / no \n ->")

    if y == "yes":
        ice_cream_station()
    elif y == "no":
        print("okay, have a good day")
        print("ice-cream station simulation success!")

    else:
        print("uhh.... i dont understand")
        return question2()

def ice_cream_station():
    a=["chocolate", "vanilla", "strawberry","mint"]
    print("This is our menu=")
    while a!= 0:
        for ax in a:
            print(ax)
        ax= input("what ice-cream do you want? \n ->")
        if ax in a:
            print(f"okay {ax}")
            a.remove(ax)
            ay=True
            if a == []:
                a=0
                topping_station()
                break
            while ay == True:
                az= input("do you want to add more ice-cream? \n ->yes / no \n->")
                if az == "yes":
                    ay=False
                elif az == "no":
                    while az == "no":
                        aa=input("are you sure?\n yes / no \n ->")
                        if aa =="yes":
                            ay=False
                            a=0
                            topping_station()
                            break
                        elif aa == "no":
                            az = "typo"
                            ay= False
                        else:
                            print("i dont understand")
                            az= "no"
                else:
                    print("uhhh.... we dont have that")
                    ay=True
        else:
            print("uhhh.... we dont have that")

def topping_station():
    print("ice-cream station simulation success!")

question1()