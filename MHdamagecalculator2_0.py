
#Etablir une liste exaustive du moveset ainsi que des points faibles
#Pour les parties brisables, introduire une liste avec en complément les PV de la partie
from math import *


#Les données des monstres et persos sont conservées dans un fichier texte séparé qu sera podifié par les programmes.
#Faire dans le programme d'extraction uun if pour vérifier que les lignes commençant par # ne soient pas lues
#Faire un programme qui permet de modifier le fichier texte en prenant en argument des noms d'éléments et tout et traduit ça en chiffres pour modifier le fichier texte. Ex = le programme traduit "glace" en "3" pour permettre de ne pas avoir à traduire le fichier texte à chaque utilisation.


##Données générales

#Sharpness

Bleue=4
Vert=3
Jaune=2
Orange=1
Rouge=0
Blanc=5
Violet=6 #Disponible uniquement via Sharpness expert
Sharpness=[0.5,0.75,1,1.05,1.25,1.32,1.45,-2,-1,0,2,4,6,8]
#Les six premiers termes donnent le bonus multiplicatif de dégat et les six suivants le bonus en chances de ne pas deflect sur 10

#Elements

Feu=0
Eau=1
Foudre=2
Glace=3
Dragon=4
Poison=5
Paralysie=6
Sommeil=7
Explosion=8

#Permet de fouiller facilement les listes


#Blindages :

Faible=0
Normal=1
Moyen=2
Fort=3
Blindé=4
Blindage=Bl=[0,15,30,60,90,10,10,8,6,-1]
#Les cinq premier termes donnent le modificateur de dégat en résistance multiplicatif sur 100 et les six suivants les chances sur 0 de ne pas deflect du base pour les connus

#Références joueur
HP=11
Attaque=13
Défensephy=4
DéfenseElem=5
Tranchant=10
Défense=4
Shield=6
Recovery=12
HPmax=20

#Données pratiques

oui=Oui=yes=Yes=True
non=Non=no=No=False

#HPlist=Hplist=("Punya",Punya[HP][0],"Tyrliel",Tyrliel[HP][0],"Shinza",shinza[HP][0],"Minyarr",Minyarr[HP][0],"Garuga",garuga[0][0])

##Données des persos




#NomJoueur=[, Sharpness, DégatsAffinité, [Element , dégats], Def Phy, [Res Feu, Eau, Foudre, Glace, Dragon, Res elementaire générale], Shield capacity, Blessing value, Armor Penetration, Critical Element, Sharpness bonus, (HP,Hpmax), recovery bonus en points sur 100,Attaque]

test="garugatest"
##Données du monstre :

#NomMonstre=[(PV,PVmax), [Elem Res (feu, eau, foudre, glace, dragon], (PV KO,PVKO max,nombreKO), (PV Poison,PV Poison Max,nombrePoison), (PV Paralysie,PV paralysie Max,Nombre Para), (Pv sommeil,Pv sommeil max,Nombre sommeil),(pv explosion, pvmaxexplosion,nbexplosions]

#Garuga :

cou=Cou=Normal
Tête=tête=Faible
ventre=Ventre=Moyen
Dos=dos=Blindé
Queue=queue=Blindé
Ailes=ailes=Moyen
Pattes=pattes=Moyen


#mettre un hashtag lorsque le combat en commencé pour éviter de réinitialiser les valeurs en HP des monstres et joueurs par accident lors d'un crtl+e

##Comfort

def elementorailmentdisplay(element): #permet d'afficher les éléments lors d'évènements print en fonction de leur valeur.
    if element ==0 :
        return "Feu"
    if element ==1 :
        return "Eau"
    if element ==2 :
        return "Foudre"
    if element ==3 :
        return "Glace"
    if element== 4:
        return "Dragon"
    if element ==5 :
        return "Poison"
    if element ==6 :
        return "Paralysie"
    if element ==7 :
        return "Sommeil"
    if element==8 :
        return "Explosif"

#def elementmodifier(element):

def strtointbuff(type): #permet de convertir un string en la valeur qui lui est associée
    if type == "HP" or type=="Hp" or type== "hp":
        return 11
    if type == "Attaque" or type=="attaque" or "att" in type:
        return 13
    if type == "defense" or type == "Defense" or type == "def":
        return 4
    if type == "Shield" or type == "shield":
        return 6
    if "overy" in type:
        return 12
    if type == "fort" or type=="Fort":
        return 3
    if type == "faible" or type=="Faible" or "aible" in type:
        return 0
    if type == "Moyen" or type == "moyen":
        return 2
    if type == "Normal" or type == "normal":
        return 1
    if type == "Blindé" or type == "blindé":
        return 4
    if "arpness" in type or "anchant" in type :
        return 10

#faire un programme qui extrit du fichier les points faibles des onstres en fonction de l'endroit visé


def elementreversedisplay(str):
    if "ire" in str or "eu" in str:
        return 0
    if "au" in str:
        return 1
    if "oudre" in str :
        return 2
    if "lace" in str :
        return 3
    if "ragon" in str :
        return 4
    if "oison" in str :
        return 5
    if "alysie" in str:
        return 6
    if "ommeil" in str:
        return 7
    if "xplosi" in str:
        return 8
    else:
        return -1 #si aucun n'est validé, on considère qu'il n'y en a pas

def sharpcalc(j,p):
    #j pour joueur
    #p pour partie touchée
    #Principe de l'algo : donne un bonus en fonction de la sharp et un malus en fonction du blindage, puis compile tout pour donner la proba
    #rappel : j[10] correspond au bonus de sharpness du joueur, du à des bonus externes ou aux propriétés de son arme
    co=int(j[1])
    b=Sharpness[co+7]+j[10]
    c=Blindage[p+5]
    tot=b+c #chance totale sur 10 est les chances de base c plus le bonus b
    if b+c>10:
        return 10
    if b+c<0:
        return 0
    return b+c #proba sur 10 de perforer


def staminacost(j,dmg): #stamina cost du blocage. les valeurs du bouclier sont contenues dans j.
    #j pour joueur
    #dmg pour l'attaque du monstre
    s=round(3-(round((j[6]-dmg)/10)))
    #s pour stamina cost, égal à  3-( capacité-dégats totaux)/10 arrondi à l’entier le plus proche
    return(s)#retourne le stamina cost PUR, qui sera tronqué par la suite


##En combat

def dvm(critique=False,rawpur=0,elempur=0): #dvm = Damage vs Monstre
    #elempur=dégats élémentaires purs spécifiques (décharges élémentaires)
    #rawpur=dégats raw purs spécifiques (fioles de choc)
    j0=input("Joueur : ")
    a0=input("Attaque utilisée : ")
    if "spe" in a0 or "Spe" in a0: #si jamais nécessité de mettre un coup spécial type DragonPiercer
        dg=int(input("Dégats du coup spécial : "))
        em=float(input("Multiplicité élémentaire du coup spécial : "))
        gk=input("Dégats de KO du coup spécial : ")
        if gk=="" or gk=="0" or gk==0:
            a=[dg,em]
        else:
            a=[dg,em,gk]
    else:
        a=datao(a0)
    m0=input("Monstre cible : ")
    p0=input("Résistance aux dégats de la hitzone : ") #entrer un nombre (0 pour faible, 1 pour normal, etc...
    p=strtointbuff(p0)
    c=critique
    data=datable('D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')
    j=dataj(j0) #récupération des données du joueur et du monstre via la fonction d'extraction
    m=dataj(m0)
    monstre=m
    atk=j[Attaque]

    AP=j[8]
    CE=j[9]
    if c==True :
        Cd=(100+j[2])/100 #cd for crit damage multiplier
    else :
        Cd=1
    Sh=Sharpness[int(j[1])]
    if j[3]!= None:
        if j[3][0]<5:#Disjonction entre les éléments et les ailments (?)
            Elem=j[3][0]
            Eledmg=j[3][1]
            Ailment=-1
            Ailmentdmg=0
        if j[3][0]>=5:
            Ailment=j[3][0]
            Ailmentdmg=j[3][1]
            Elem=-1
            Eledmg=0
    else :
        Elem=-1
        Eledmg=0
        Ailment=-1
        Ailmentdmg=0
    if p-AP<0:
        p+=1 #pas de valeur négative d'indexation du blindage, 0 correspondant à un blindage nul.
    if CE==1:
        CE=Cd #attribution des dégats crit aux éléments si Critical element est actif
    else:
        CE=1
    Elem=int(Elem)
    Ailment=int(Ailment)
    #calcul de la réduction de dégats due au blindage.
    red=(100-Bl[int(p-AP)])/100
    if a[1]==0:
        red=1

    #calcul des dégats initiaux : dégats de base/100 * attaque * resistance du monstre * sharpness * crit
    raw=round(((a[0]+rawpur)/100)*atk*(red)*Sh*Cd)
    ele=round((a[1]*Eledmg+elempur)*(1-(m[2][int(Elem)]/100))*CE*Sh*red)
    #affichage des valeurs
    if a[1]!=0 and (Elem!=-1 or Ailment!=-1): #on n'affiche pas de dégats élémentaires si l'attaque est non élémentaire (type Glshot) ou si le personnage n'a pas d'élément.
        print("Raw = ",raw, "Elemental = ", ele, elementorailmentdisplay(Elem))
    else :
        print("Raw= ",raw, ", Attaque non élémentaire.")
    print(" ")
    print("Total = ", raw+ele)
    print(" ")

   #cas particulier du KO :
    if len(a)==3 and p==tête:
        DmgKO=a[2]
        print("Dégats KO = ",a[2])
        monstre[3][0]-=DmgKO
        print("Il reste",monstre[3][0],"PV en KO au monstre")

    #calcul des chances de perforation
    perfo=sharpcalc(j,int(p-AP))
    if (perfo==10 and a[1]!=0):
        print("Pas de rebond possible")
        #if a[0]>=Bl[p-AP]:
            #print("(Armor Override)") #Si la puissance de base d'une attaque dépasse la résistance de la partie de la cible , le coup traverse peu importe le blindage
    if perfo==0 and  a[0]<Bl[int(p-AP)]:
        print("Rebond obligatoire")
    if perfo>0 and perfo<10 and a[0]<Bl[int(p-AP)]:
        print("Chances de perforer = ",perfo,"/10")



    #disjonctions de cas en fonction des ailments
    if Ailment!=-1 and a[1]!=0 : #a[1]=0 implique que l'attaque est non élémentale
        monstre[int(Ailment-1)][0]-=round(Ailmentdmg*a[1])
        print("Le monstre accumule ",round(Ailmentdmg*a[1])," PV en ", elementorailmentdisplay(Ailment))
        print("Chances de statut = ",round((Ailmentdmg/(2*monstre[int(Ailment-1)][1]))*100),"/100")
        print("PV restants dans le statut considéré",monstre[int(Ailment-1)][0],"/",monstre[int(Ailment-1)][1])
    if monstre[3][0]<=0 :
        m[3][2]+=1 #incrémentation du compteur de KO
        monstre[3][0]=monstre[3][1]*0.5*(1+monstre[3][2]) #Réinitialisation avec augmentation du palier de KO en fonction du nombre de KO
        print("KO !")
    if monstre[4][0]<=0:
        m[4][2]+=1
        monstre[4][0]=round(monstre[4][1]*(1+m[4][2]*0.4))
        monstre[4][1]=monstre[4][0]
        print("Empoisonné ! Dégats de poison = ",round(m[1][1]/100))
    if monstre[5][0]<=0:
        m[5][2]+=1
        monstre[5][0]=round(monstre[5][1]*(1+m[5][2]*0.4))
        monstre[5][1]=monstre[5][0]
        print("Paralysé !")
    if monstre[5][0]<=0:
        m[5][2]+=1
        monstre[6][0]=round(monstre[6][1]*(1+m[6][2]*0.4))
        monstre[6][1]=monstre[6][0]
        print("Dodo !")
    if monstre[7][0]<=0:
        m[7][2]+=1
        monstre[7][0]=round(monstre[7][1]*(1+m[7][2]*0.1))
        monstre[7][1]=monstre[7][0]
        print("BOOM ! 120 PV !")
        monstre[1][0]-=120
        m[1][0]-=120
    #application des dégats infligés au monstre
    monstre[1][0]-=raw+ele
    print("Il reste ",int(monstre[1][0])," PV au monstre")
    if m[1][0]<=0:
        print("Victoire !")
    tablemod2(data,m) #modification de la ligne de code correspondant au monstre
    datascripter(data,'D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')



def dvj(Blocage=False, blessing=False): #dégats v joueurs
    data=datable('D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')
    j0=input("Joueur ciblé : ")
    dmg0=input("Dégats non élémentaire : ")
    Ele0=input("Element utilisé : ")
    Eledmg0=input("Dégats élémentaires : ")
    Ele=elementreversedisplay(Ele0)
    if dmg0!= "":
        dmg=int(dmg0)
    else:
        dmg=0
    if Eledmg0!= "":
        Eledmg=int(Eledmg0)
    else:
        Eledmg=0
    j=dataj(j0)
    defphy=j[4]
    defele=j[5][5]
    if blessing:
        red=1-j[7]/100
    else:
        red=1
    if Blocage:
        Sh=j[6]
    else:
        Sh=0
        #Attribution à Sh de la valeur du bouclier s'il est utilisé. Sh vaut 0 par défaut (pas de bouclier ou non utilisé)
    redphy=defphy/(30+defphy) #Reduction de dégats physique
    if not (Ele==None or Ele==-1):
        modele=(100-3*(j[5][int(Ele)]))/100 #modification elementaire = (100-3 fois la res élémentaire correspondante)/100


    else:
        modele=1
    if modele<0:
        modele=0 #une résistance si forte qu'elle rend le modificateur négatif modifie la valeur de modification à 0
    redele=defele/(30+defele) #Reduction de dégats élémentaire
    raw=round(dmg*(1-redphy))*red #Dégats de base non élémentaires
    elem=round(Eledmg*(1-redele))*red*modele #Dégats de base élémentaires
    svg=round(raw+elem)
    if raw+elem-Sh<0:
        Sh=raw+elem
    Bc=round((raw+elem-Sh)*(round(1-Sh/(raw+elem),1)))#Dégats réellement subis après absorption par le potentiel bouclier
    #La valeur obtenue est ensuite multipliée par un modifiacteur empêchant la valeur de PV perdue d'être escessive si le bouclier est très faible devant la puissance de l'attaque. Ce modificateur est arrondi à la première décimale, entre autres pour les cas où l'attaque est endessous de deux fois plus forte que le bouclier.
    if Bc<0:
        Bc=0
        #Si le bouclier est plus fort que l'attaque, les dégats subis sont ramenés à 0

    #affichage des données
    print("Raw basic = ",raw, "Ele basic = ", round(elem),". Total brut =",svg)


    #calcul des marqueurs d'endurance
    if Blocage:
        stamcost=staminacost(j,raw+elem)
        if stamcost<0:
            stamcost=0
        if stamcost>4:
            stamcost=4 #capage des marquers à 4 pour éviter de descendre toute l'endurance du joueur.
        print("Stamina cost ",stamcost,"points")
        bool=non
        if stamcost>0:
            bool=input("Assez d'endurance ? ")
        else:
            bool="oui"

        if bool=="True" or bool=="oui" or bool == "true" or bool == "Oui":
            j[HP][0]-=Bc #modification de la jauge de vie du joueur
            if Bc>0:
                print("Le joueur bloque",svg-Bc, "et perd ",Bc,"PV")
            else :
                print("Le bouclier absorbe tous les dégats.")
        else :
            mar=input("Marqueurs restants : ")
            mar=int(mar)
            if mar>stamcost:
                return "Erreur dans le calcul d'endurance, le joueur dispose d'assez de marqueurs"
            hploss1=round(svg-(mar/stamcost)*Sh) #le joueur ne bloque que marqueur restant sur cout fois bouclier dégats et encaisse tout le reste.
            j[HP][0]-=hploss1
            print("Le joueur bloque",svg-hploss1, "et perd ",hploss1,"PV")

    print()
    print("Dégats subis =",Bc)
    j[HP][0]-=Bc
    if j[HP][0]>0:
        if Blocage :
            if bool=="True" or bool=="oui" or bool == "true" :
                print("HP récupérables :",round((Bc/2)*(1+j[12]/100)))
            else:("HP récupérables :",round((hploss1/2)*(1+j[12]/100))) #changement de PV récupérables si le joueur rate son blocage ou pas.
        else :
            print("HP récupérables :",round((Bc/2)*(1+j[12]/100))) #Pas de regen si le joueur est mort lol

    #affichage des données restantes

    if j[HP][0]<0:
        j[HP][0]=0
    print(j[HP][0], "PV restants")
    if j[HP][0]==0:
        print("Joueur Ko.")
    tablemod2(data,j)
    datascripter(data,'D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')

def heal(): #permet de soigner les joueurs #attention, à adapter avec le fichier texte
    data=datable('D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')
    j0=input("Joueur à soigner : ")
    pv=int(input("Nombre de PV à soigner : "))
    j=dataj(j0)#j[HP][0]+=pv à modifier avec la nouvelle méthode
    j[HP][0]+=pv
    if j[HP][0]>j[HP][1]:
        j[HP][0]=j[HP][1]
    if pv>=0:
        print(pv,"HP récupérés. Total",j[HP][0])
    if pv<0:
        print(-pv, "HP perdus. Restants",j[HP][0])
    if j[HP][0]<=0:
        print("Joueur Ko.")
    tablemod2(data,j)
    datascripter(data,'D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')

def buff(): #permet d'appliquer des buffs aux joueurs, à adapter au fichier texte
    data=datable('D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')
    j0=input("Joueur à Buff : ")
    b0=input("Catégorie du buff : ")
    n0=input("Valeur du buff :")
    n=int(n0)
    j=dataj(j0)
    b=strtointbuff(b0)
    if b==5:
        for i in range(5):
            j[6][i]+=n
            return()
    elif b==HP:
        j[HP][1]+=n
        if n>0:
            j[HP][0]+=n
            print("HP augmentés de",n)
        if n<0:
            if j[HP][0]>j[HP][1]:
                j[HP][0]=j[HP][1]
            print("HP diminués de",-n)
        print("Nouvelles valeurs de HP :",j[HP][0],"/",j[HP][1])
    elif b==Défense:
        j[b]+=n
        j[5][5]+=n
        print("Nouvelle valeur : ",j[b])

    else:
        j[b]+=n
        print("Nouvelle valeur : ",j[b])
    tablemod2(data,j)
    datascripter(data,'D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')




def reinitialiser(): #à tester
    datamod=datable('D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')
    dataini=datable('D:/Users/Nicolas/Documents/MHjdr/MHdatadini.txt')
    for i in range(len(datamod)):
        for j in range(len(dataini)):
            if datamod[i][0]==dataini[j][0]:
                datamod[i]=datamod[j] #on remplace les valeurs de combats par les valeurs hors combat.
    datascripter(datamod,'D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')



def HPlist():
    data=datable('D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt')
    for i in range(4):
        print(data[i][0]," : ",data[i][HP][0],"/",data[i][HP][1])

#Choses à faire à l'avenir :
#Faire dans le fichier "non modifiable" une base de donnée des stats des persos dans leur état au repos.
#Faire un programme qui permet de modifier les stats de base des eprsos hors combat (programme upgrade())
#Compléter le programme réinitialiser() pour remettre les persos dans leur état hors combat à partir du fichier non modifiable.

##Hors combat


#def change() fonction ayant pour but de modifier le fichier des données initiales pour réaliser des modifications d'upgrade
    #data=datable('D:/Users/Nicolas/Documents/MHjdr/MHdatadini.txt')
    #j0=input("Joueur à changer : ")
    #j=dataini(j0)






##Data analyser

#Les algorithmes suivant interagissent avec un tableau de valeurs qui donne les infos des joueurs et un fichier tete qui sert à les sauvegarder. Le tableau sera de la forme [Joueur1,joueur2,joueur3,joueur4,monstre]. (a priori)





def datao(objet): #S'utilise sur un fichier qui contient des informations fixes (typiquement les attaques)
    f=open('D:/Users/Nicolas/Documents/MHjdr/MHdatafixe.txt', 'r')
    donnees=f.readlines()
    parsedData = []
    for line in donnees:
        if objet in line and "#" not in line :
            parsedData.append(line.split(" "))
    parsedData[0].pop(0) #supression du premier terme qui correspond au nom et qui est inutile dans la suite
    fdata=parsedData[0] #parseddata apparait comme une liste d'une liste à cause du .appen. on ne garde que la liste interne qui est supposée unique.
    for i in range(len(fdata)) :
        if "," not in fdata[i]:
            fdata[i]=float(fdata[i]) #la "," sert à indiquer puis indexer les listes de liste dans le string global.
        else :
            fdata[i]=fdata[i].split(",")
            fdata[i].pop(0) #le premier terme est une ",", on s'en débarasse
            for j in range(len(fdata[i])):
                fdata[i][j]=float(fdata[i][j]) #maintenant qu'on a identifié ce qui doit être une liste, on transforme en entiers ses membres.
    nah=fdata.pop()
    return nah

def dataj(objet):#extracteur de données dans un fichier qui sera modifiable
    f=open('D:/Users/Nicolas/Documents/MHjdr/MHdatamod.txt', 'r')
    donnees=f.readlines()
    parsedData = []
    for line in donnees:
        if objet in line and "#" not in line :
            parsedData.append((line.split(" ")))
    fdata=parsedData[0] #parseddata apparait comme une liste d'une liste à cause du .appen. on ne garde que la liste interne qui est supposée unique.
    for i in range(1,len(fdata)) :
        if "," not in fdata[i]:
            fdata[i]=float(fdata[i]) #la "," sert à indiquer puis indexer les listes de liste dans le string global.
        else :
            fdata[i]=fdata[i].split(",")
            fdata[i].pop(0) #le premier terme est une ",", on s'en débarasse
            for j in range(len(fdata[i])):
                fdata[i][j]=float(fdata[i][j]) #maintenant qu'on a identifié ce qui doit être une liste, on transforme en entiers ses membres.
    return fdata

def dataini(objet):#extracteur de données dans un fichier qui sera modifiable
    f=open('D:/Users/Nicolas/Documents/MHjdr/MHdataini.txt', 'r')
    donnees=f.readlines()
    parsedData = []
    for line in donnees:
        if objet in line and "#" not in line :
            parsedData.append((line.split(" ")))
    fdata=parsedData[0] #parseddata apparait comme une liste d'une liste à cause du .appen. on ne garde que la liste interne qui est supposée unique.
    for i in range(1,len(fdata)) :
        if "," not in fdata[i]:
            fdata[i]=float(fdata[i]) #la "," sert à indiquer puis indexer les listes de liste dans le string global.
        else :
            fdata[i]=fdata[i].split(",")
            fdata[i].pop(0) #le premier terme est une ",", on s'en débarasse
            for j in range(len(fdata[i])):
                fdata[i][j]=float(fdata[i][j]) #maintenant qu'on a identifié ce qui doit être une liste, on transforme en nombres ses membres.
    return fdata


def datascripter(tableau,file): #peremt d'éditer le fichier texte en prenant en argument le tableau qui servira à le compléter.
    t=tableau
    f=open(file, 'w')#fichier joueur
    for i in range (len(tableau)):
        for j in range(len(tableau[i])):
            t[i][j]=str(t[i][j])
            t[i][j]=t[i][j].replace("[",",",100)
            t[i][j]=t[i][j].replace("]","",100) #Obtient la structure d'extraction du fichier texte où les listes commencent par "," et dont les membres de la liste sont séparées par des ","

        t[i]=' '.join(t[i])#permet de transformer une liste en chaine de caractère en utilisant ' ' comme séparateur
        t[i]=t[i]+chr(10)#truc de Etienne pour les sauts de lignes. à voir comment on peut changer ça
    for i in range(len(t)):
        t[i]=t[i].replace(", ",",",100)
    j=0
    while j in range(len(t)):
        if t[j]=='\n\n':
            t.pop(j)#permet de supprimer les sauts de ligne intempestifs
        else:
            j+=1
    f.writelines(t)


def datable(f): #renvoie un tableau composé des lignes du fichier texte. C'est ce tableau qui sera ensuite réécrit dans le même fichier texte pour actualisation.
    f=open(f, 'r')
    donnees=f.readlines()
    t = [] #tableau initial. On introduit à l'intérieur les strings
    tf=[] #tableau final. on append les lignes à ce dernier
    for line in donnees :
        if "#" not in line :
            t.append((line.split(" ")))
    for j in range(len(t)):
        l=t[j]#l est une liste de caractères

        for i in range(1,len(l)) :
            if "," not in l[i]:
                l[i]=float(l[i]) #la "," sert à indiquer puis indexer les listes de liste dans le string global.
            else :
                l[i]=l[i].split(",")
                l[i].pop(0) #le premier terme est une ",", on s'en débarasse
                for j in range(len(l[i])):
                    l[i][j]=float(l[i][j]) #maintenant qu'on a identifié ce qui doit être une liste, on transforme en entiers ses membres.
        tf.append(l)
    return tf
#pour le gros tableau, on réinsère les lignes qu'on a modifié en effaçant celle d'avavtn. système pour reconnaître la bonne ligne : if nomjoueur in ligne tableau

def tablemod(t,objet,idmod,mod): #permet de modifier une valeur en particulier du tableau (non utilisé pour le moment)
    for i in range(len(t)):
        if objet in t[i][0]:
            t[i][idmod]+=mod


def tablemod2(t,ligne): #permet d'incorporer les lignes modifiées directement dans le tableau
    for i in range(len(t)):
        if t[i][0]==ligne[0]:
            t[i]=ligne










#D:/WINDOWS_SEVEN/Users/Nicolas_Admin/Documents/MHjdr/MHdata.txt












