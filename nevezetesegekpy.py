import nevezetesegekclass
lista=[]
def f1(label):
    print(label)
    x=input("Kérek egy kontinenst: ")
    inputFile("nevezetesegek.txt")
    for i in range(len(lista)):
        if(x == lista[i].kontinens):
            print("\t",lista[i].nev," ",lista[i].varos," ",lista[i].orszag," ",lista[i].kontinens)
       
def f2(label):
    print(label)
    x=input("Kérek egy országot: ")
    for i in range(len(lista)):
        if(x == lista[i].orszag):
            print("\t",lista[i].nev," ",lista[i].varos," ",lista[i].orszag," ",lista[i].kontinens)
        if(x !=lista[i].orszag):
            txt = "\tIlyen nincs a listában"
    print(txt)
    

def f3(label):
    print(label)
    x=input("Kérek egy nevezetességet: ")
    for i in range(len(lista)):
        if(x == lista[i].nev):
            print("\t",lista[i].nev," ",lista[i].varos," ",lista[i].orszag," ",lista[i].kontinens)
        if(x !=lista[i].nev):
            txt = "\tIlyen nincs a listában"
    print(txt)
    
def f4(label):
    print(label)
    x =(input("\tMelyik városba van a Eiffel-torony?: "))
    if(x == "Párizs"):
        print("\tEltaláltad!")
    if(x != "Párizs"):
        print("\tNem találtad el!")

def f5(label):
    print(label)
    x =(input("\tMelyik városba van a Arany Pavilon?: "))
    if(x == "Kyoto"):
        print("\tEltaláltad!")
    if(x != "Kyoto"):
        print("\tNem találtad el!")

def f6(label):
    print(label)
    x =(input("\tMelyik városba van a Brandenburgi kapu?: "))
    if(x == "Berlin"):
        print("\tEltaláltad!")
    if(x != "Berlin"):
        print("\tNem találtad el!")
     
def f7(label):
    print(label)
    x =(input("\tMelyik városba van a Jézus-szobor?: "))
    if(x == "Rio de Janeiro"):
        print("\tEltaláltad!")
    if(x != "Rio de Janeiro"):
        print("\tNem találtad el!")

def f7(label):
    print(label)
    x =(input("\tMelyik városba van a Magyar Parlament?: "))
    if(x == "Budapest"):
        print("\tEltaláltad!")
    if(x != "Budapest"):
        print("\tNem találtad el!")
        
def inputFile(file):
    f=open(file,"r", encoding="utf-8")
    for sor in f:
        sor=sor[0:-1].split(",")
        példány=nevezetesegekclass.Nevezetesegek(sor[0],sor[1],sor[2], sor[3])
        lista.append(példány)
    f.close()


#f1("Kiirom")
#f2("Kiirom")
#f3("Kiirom")
f4("Kiirom")
f5("Kiirom")
f6("Kiirom")
f7("Kiirom")

