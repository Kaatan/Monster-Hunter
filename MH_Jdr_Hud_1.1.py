#Etablir une liste exaustive du moveset ainsi que des points faibles
#Pour les parties brisables, introduire une liste avec en complément les PV de la partie
from math import *
import os

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

#Références mixtes

HP=1
Eleres=2


#References joueurs
Eledef=3
Def=4
Arme=5
DegatsEle=6 #Comprend l'élément ainsi que les dégats sous la forme d'une liste
Shield=7
AP=8
Critele=9
Sharpbonus=10
Sharp=11
Recovbonus=12
Attaque=13
Endurance=14 #Comprends l'endurance actuelle ainsi que l'endurance max
Crit=15 #comprend les chances de crit ainsi que les dégats crit soius forme d'une liste

#References Monstres
KO=3


#Données pratiques

oui=Oui=yes=Yes=True
non=Non=no=No=False
Nom=0
Donnee=1
#HPlist=Hplist=("Punya",Punya[HP][0],"Tyrliel",Tyrliel[HP][0],"Shinza",shinza[HP][0],"Minyarr",Minyarr[HP][0],"Garuga",garuga[0][0])

#Attaques
Pow=0
Multihit=1
KOdg=2
Endcost=3

#Nomjoueur : [PV,PV max], Elem Res, Elem Def, Def, Arme, [Elem, dégats elem], Shield, Blessing, Armor perf, Crit Ele, Sharp Bonus, Recovery bonus, Attaque

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


def weaptonumbconverter(arme):
    if arme== 'SnS':
        return 0
    if arme== 'DB':
        return 1
    if arme== 'LS':
        return 2
    if arme== 'GS':
        return 3
    if arme== 'Lance':
        return 4
    if arme== 'CB':
        return 5
    if arme== 'Bow':
        return 6
    if arme== 'Hammer':
        return 7
    if arme== 'SA':
        return 8
    if arme== 'GL':
        return 9
    if arme== 'Palico':
        return 10

def sharpnameconvertor(colour):
    if 'ert' in colour:
        return 3
    if 'leu' in colour:
        return 4
    if 'aune' in colour:
        return 2
    if 'ouge' in colour:
        return 0
    if 'lanc' in colour:
        return 5
    if 'iolet' in colour:
        return 6


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
        return HP
    if type == "Attaque" or type=="attaque" or "att" in type:
        return Attaque
    if type == "defense" or type == "Defense" or type == "def":
        return Def
    if type == "Shield" or type == "shield":
        return Shield
    if "overy" in type:
        return Recobonus
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
        return Sharp

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


##Programmes de préparation

def endloss(j,a):#prend en argument la liste du joueur et l'attaque pour modifer les stats d'endurance de la liste en fonction de l'attaque si elle consomme ou non de l'endurance
    if j[Endurance][0]>0:
        j[Endurance][0]-=a[4]
        datascripter(j,j0)

def esquive(j):
    if j[Endurance][0]>0:
        j[Endurance][0]-=1
        datascripter(j,j0,'Joueurs')
    else:
        print("Esquive impossible.")

def esquiveintra(j): #peut être utilisée dans les fonctions sans redemander le nom du joueur
    Esq=input("Esquive réussie ? ")
    if j[Endurance][0]>0:
        j[Endurance][0]-=1 #On n'écrit pas sur le fichier texte car ce sera fait après dans le programme de calcul
        if Esq=="Oui" or Esq == "oui":
            return True #Esquive réussie
    else:
        print("Esquive impossible.")
    return False #Si l'esquive est ratée ou impossible, return False


def endregen(j):
    if j[Endurance][0]<j[Endurance][1]:
        j[Endurance][0]+=1

def endregenextra():
    j0=input("Joueur : ")
    j=dataex(jo,1,'Joueurs')
    endregen(j)


def sharpcalc(j,p):
    #j pour joueur
    #p pour partie touchée
    #Principe de l'algo : donne un bonus en fonction de la sharp et un malus en fonction du blindage, puis compile tout pour donner la proba
    #rappel : j[10] correspond au bonus de sharpness du joueur, du à des bonus externes ou aux propriétés de son arme
    co=sharpnameconvertor(j[Sharp]) #couleur
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
    s=round(3-(round((j[Shield]-dmg)/10)))
    #s pour stamina cost, égal à  3-( capacité-dégats totaux)/10 arrondi à l’entier le plus proche
    return(s)#retourne le stamina cost PUR, qui sera tronqué par la suite



def Movesetprinter(Arme):
    Noms=dataex(Arme,0,'Armes')
    Moves=dataex(Arme,1,'Armes')
    print()
    print("Arme :",Noms[0])
    print()
    for i in range(1,len(Noms)):
        print(Noms[i], ":", Moves[i][0], "dégats")
    print()



def Elagueur(texte):
    return texte[:-4] #Retire le'.txt'



def elagueur1(stri):
    return stri[:-1]


def Reaction(str):
    if "lo" in str:
        return "Blocage"
    if "odge" in str or "qui" in str:
        return "Esquive"
    if str=='':
        return "Rien"


def valid(str):
    if "ui" in str or "es" in str:
        return True
    return False



##En combat





def dvm(j,m0): #dvm = Damage vs Monstre




    arme = elagueur1(j[Arme]) #Incorporer l'arme du joueur pour les données de recherche des dégats des attaques

    Movesetprinter(arme) #affichage du moveset pour aider aux résultats

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
        a=Attack(a0,arme)

    p0=input("Résistance aux dégats de la hitzone : ") #entrer un nombre (0 pour faible, 1 pour normal, etc...

    marq=a[Endcost]
    if marq!=0:
        if j[Endurance][0]>marq:
            j[Endurance][0]-=marq
    else:
        endregen(j)

    affinity=j[Crit][0]
    if affinity!=0:
        critique=int(input("Résultat du dé de critique : "))
        if affinity>0:
            if critique<=j[Crit][0]:
                c=True
                if critique<=int(affinity/10)+1:
                    print("Critique double !")
                    dbcc=True
                else:
                    print("Coup Critique !")
                    dbcc=False
        else:
            if critique<=j[Crit][0]:
                if critique<=int(affinity/10)+1:
                    print("Echec Critique double !")
                    dbcc=True
                else:
                    print("Echec Critique !")
                    dbcc=False
                    print("Le coup du joueur est annulé !")
                    return #le tour se termine

    p=strtointbuff(p0)
    Sh=Sharpness[sharpnameconvertor(j[Sharp])]

    m=dataex(m0,1,'Monstres')
    monstre=m
    atk=j[Attaque]

    ap=j[AP]
    CE=j[Critele]
    if c==True :
        if j[Crit][0]>0:
            sgn=1
        else:
            sgn=-1
        Cd=sgn*(100+j[Crit][1])/100 #cd for Crit Damage multiplier
    else :
        Cd=1
    if dbcc:
        if affinity>0:
            cdt=input("Conditions optimales respectées ?")
            cdt=valid(cdt)
            if cdt:
                Cd=2*Cd
            else:
                po=input("Nouveau point faible optimal : ")






    if j[DegatsEle]!= None:
        if j[DegatsEle][0]<5:#Disjonction entre les éléments et les ailments (?)
            Elem=j[DegatsEle][1]
            Eledmg=j[DegatsEle][0]
            Ailment="0"
            Ailmentdmg=0
        if j[DegatsEle][0]>=5:
            Ailment=j[DegatsEle][1]
            Ailmentdmg=j[DegatsEle][0]
            Elem="0"
            Eledmg=0
    else :
        Elem="0"
        Eledmg=0
        Ailment="0"
        Ailmentdmg=0
    if p-ap<0:
        p+=1 #pas de valeur négative d'indexation du blindage, 0 correspondant à un blindage nul.
    if CE==1:
        CE=Cd #attribution des dégats crit aux éléments si Critical element est actif
    else:
        CE=1
    Elem=elementreversedisplay(Elem)
    Ailment=elementreversedisplay(Ailment)
    #calcul de la réduction de dégats due au blindage.
    red=(100-Bl[int(p-ap)])/100
    if a[1]==0:
        red=1

    #calcul des dégats initiaux : dégats de base/100 * attaque * resistance du monstre * sharpness * crit
    raw=round(((a[0])/100)*atk*(red)*Sh*Cd)
    print(a[1],Eledmg,1-(m[Eleres][int(Elem)]/100),CE,Sh,red)


    ele=round((a[1]*Eledmg)*(1-(m[Eleres][int(Elem)]/100))*CE*Sh*red)
    #affichage des valeurs
    if a[1]!=0 and (Elem!=-1 or Ailment!=-1): #on n'affiche pas de dégats élémentaires si l'attaque est non élémentaire (type Glshot) ou si le personnage n'a pas d'élément.
        print("Raw = ",raw, "Elemental = ", ele, elementorailmentdisplay(Elem))
    else :
        print("Raw= ",raw, ", Attaque non élémentaire.")
    print(" ")
    print("Total = ", raw+ele)
    print(" ")

   #cas particulier du KO :
    if a[2]!=0:
        p=input("Coup à la tête ?")
        if p:
            DmgKO=a[2]
            print("Dégats KO = ",a[2])
            monstre[KO][0]-=DmgKO
            print("Il reste",monstre[KO][0],"PV en KO au monstre")

    #calcul des chances de perforation
    perfo=sharpcalc(j,int(p-ap))
    if (perfo==10 and a[1]!=0) or dbcc:
        print("Pas de rebond possible")
        rbd=1
    if perfo==0 and  a[0]<Bl[int(p-ap)]:
        print("Rebond obligatoire")
        rbd=0
    if perfo>0 and perfo<10 and a[0]<Bl[int(p-ap)]:
        print("Chances de perforer = ",perfo,"/10")
        perfchance=int(input("Résultat du dé de perfo"))
        if perfchance<perfo:
            rbd=1
        else:
            rbd=0



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
    monstre[HP][0]-=raw*rbd+ele #pas de raw en cas de rebond
    print("Il reste ",int(monstre[1][0])," PV au monstre")
    if m[HP][0]<=0:
        print("Victoire !")
    datascripter(monstre,m0,'Monstres')
    return marq



def dvj(j0,j,dodge): #dégats v joueurs, modifier les indices d'appellation des donées (Shield, etc)
    dmg0=input("Dégats non élémentaire : ")
    Ele0=input("Element utilisé : ")
    Eledmg0=input("Dégats élémentaires : ")
    Reac=input("Réaction du joueur : ")
    Reac = Reaction(Reac)
    Ele=elementreversedisplay(Ele0)
    if dmg0!= "":
        dmg=int(dmg0)
    else:
        dmg=0
    if Eledmg0!= "":
        Eledmg=int(Eledmg0)
    else:
        Eledmg=0

    defphy=j[Def]
    defele=j[Eledef]
    red=1

    if Reac=="Blocage":
        Sh=j[Shield]
    else:
        Sh=0
        #Attribution à Sh de la valeur du bouclier s'il est utilisé. Sh vaut 0 par défaut (pas de bouclier ou non utilisé)
    redphy=defphy/(30+defphy) #Reduction de dégats physique
    if not (Ele==None or Ele==-1):
        modele=(100-3*(j[Eleres][int(Ele)]))/100 #modification elementaire = (100-3 fois la res élémentaire correspondante)/100


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

    if Reac=="Esquive": #Cas d'esquive
        esq=esquiveintra(j)
        if dodge!=0:
            j[Endurance][0]-=1 #annulation de la regen du tour d'attaque
        if esq:
            print("Esquive réussie !")
            datascripter(j,j0,'Joueurs')
            return #Pas besoin de poursuivre le programme



    #calcul des marqueurs d'endurance en blocage
    if Reac=="Blocage":
        stamcost=staminacost(j,raw+elem)
        if stamcost<0:
            stamcost=0
        if stamcost>4:
            stamcost=4 #capage des marquers à 4 pour éviter de descendre toute l'endurance du joueur.
        print("Stamina cost ",stamcost,"points")
        bool=False
        if stamcost>0:
            if j[Endurance][0]>=stamcost:
                j[Endurance][0]-=stamcost
                bool=True
            else:
                bool=False #Si le joueur n'a pas assez de Stamina, False
        else:
            bool=True

        if bool:#Si le joueur a assez de stam
            j[HP][0]-=Bc #modification de la jauge de vie du joueur
            if Bc>0:
                print("Le joueur bloque",svg-Bc, "et perd ",Bc,"PV")
            else :
                print("Le bouclier absorbe tous les dégats.")
        else : #Si le joueur n'a pas assez de stamina
            mar=j[Endurance][0]
            if mar>stamcost:
                return "Erreur dans le calcul d'endurance, le joueur dispose d'assez de marqueurs"
            hploss1=round(svg-(mar/stamcost)*Sh) #le joueur ne bloque que marqueur restant sur cout fois bouclier dégats et encaisse tout le reste.
            j[HP][0]-=hploss1
            j[Endurance][0] #le joueur perd toute l'endurance qu'il lui reste
            print("Le joueur bloque",svg-hploss1, "et perd ",hploss1,"PV")

    print()
    print("Dégats subis =",Bc)
    j[HP][0]-=Bc

    #affichage des données restantes

    if j[HP][0]<0:
        j[HP][0]=0
    print(j[HP][0], "PV restants")
    if j[HP][0]==0:
        print("Joueur Ko.")
    datascripter(j,j0,'Joueurs')


##Fonctions hors tour de combat


def heal(): #permet de soigner les joueurs #attention, à adapter avec le fichier texte
    j0=input("Joueur à soigner : ")
    pv=int(input("Nombre de PV à soigner : "))
    j=dataex(j0,1,'Joueurs')
    j[HP][0]+=pv
    if j[HP][0]>j[HP][1]:
        j[HP][0]=j[HP][1]
    if pv>=0:
        print(pv,"HP récupérés. Total",j[HP][0])
    if pv<0:
        print(-pv, "HP perdus. Restants",j[HP][0])
    if j[HP][0]<=0:
        print("Joueur Ko.")
    datascripter(j,j0,'Joueurs')

def buff(): #permet d'appliquer des buffs aux joueurs, à adapter au fichier texte
    j0=input("Joueur à Buff : ")
    b0=input("Catégorie du buff : ")
    n0=input("Valeur du buff :")
    n=int(n0)
    j=dataex(j0,1,'Joueurs')
    b=strtointbuff(b0)
    if b==Eleres:
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
    datascripter(j,j0,'Joueurs')



##Fonction globale

nbjoueurs=1



def action(str):
    if "aque" in str:
        return "Attaque"
    if "qui" in str:
        return "Esquive"
    else:
        return "Rien"

def tour0():
    for i in range(nbjoueurs):
        dodge=0
        j0=input("Joueur ")
        j=dataex(j0,1,'Joueurs')
        act=input("Action du joueur : ")
        act=action(act)
        if act=="Attaque":
            dodge=dvm(j)
        matk=valid(input("Le Joueur est-il attaqué ? "))
        if matk:
            dvj(j,dodge)
        else:
            if act=="Esquive":
                esquive(j)
            if act=="Rien":
                endregen(j)

def tour(joueurs,monstre):
    m0=monstre
    for i in range(nbjoueurs):
        print("Tour de", joueurs[i])
        dodge=0
        j0=joueurs[i]
        j=dataex(j0,1,'Joueurs')
        act=input("Action du joueur : ")
        act=action(act)
        if act=="Attaque":
            dodge=dvm(j,m0)
        matk=valid(input("Le Joueur est-il attaqué ? "))
        if matk:
            dvj(joueurs[i],j,dodge)
        else:
            if act=="Esquive":
                esquive(j)
            if act=="Rien":
                endregen(j)

def jeu():
    joueurs=[0]*nbjoueurs
    m0=input("Monstre : ")
    for i in range(nbjoueurs):
        print("Joueur n°",i+1,":")
        joueurs[i]=input()

    Tours=0
    Stop=False
    while Stop==False:
        tour(joueurs,m0)
        Tours+=1
        suiv=valid(input("Le jeu s'arrête ? "))
        Stop=suiv
        print("Tours écoulés : ",Tours)

#Choses à faire à l'avenir :
#Faire dans le fichier "non modifiable" une base de donnée des stats des persos dans leur état au repos.
#Faire un programme qui permet de modifier les stats de base des eprsos hors combat (programme upgrade())
#Compléter le programme réinitialiser() pour remettre les persos dans leur état hors combat à partir du fichier non modifiable.

##Hors combat

#A propos des fichiers globaux : Les fichiers globaux contiennent les stats DE BASE des joueurs. Les stats d'attaque ne sont ainsi pas notées, mais il y a l'arme du joueur, ainsi que les dégats de cette dernière, les buffs d'attaque via les stats, les passifs, etc.


#def change() fonction ayant pour but de modifier le fichier des données initiales pour réaliser des modifications d'upgrade
    #data=datable('D:/Users/Nicolas/Documents/MHjdr/MHdatadini.txt')
    #j0=input("Joueur à changer : ")
    #j=dataini(j0)

def Reiniunique(fichier):
    fichierini=fichier+'ini'
    Dataini=dataex(fichierini,1,"JoueursIni")
    datascripter(DataIni,fichier,'Joueurs')

def Reini():
    joueurs=os.listdir('D:/Users/Nicolas/Documents/MHjdr/Data/Joueurs')
    joueursini=os.listdir('D:/Users/Nicolas/Documents/MHjdr/Data/JoueursIni')
    for i in range(len(listejoueurs)):
        joueurs[i]=Elagueur(joueurs[i])
        joueursini[i]=Elagueur(joueursini[i]) #on retire les .txt
    for i in range(len(listejoueurs)):
        if joueurs[i] in joueursini: #si les noms correspondent
            data=dataex(joueurini[i],1,"JoueursIni") #On extrait les données initiales
            datascripter(data,joueurs[i],"Joueurs") #Et on remplace les données actuelles par ces dernières.

def majini(): #permet de passer des données globales aux données de combat
    a=0


def modif(joueur): #permet de modifier le fichier du joueur. la fonction imprimera les différentes stats du joueur pour que le MJ puisse les regarder et choisir celle qu'il veut modifier. Les fichiers joueurs modifiés sont les fichiers globaux, contenant les données de combat ainsi que les stats et autres (force, etc)
    a=0




##Data analyser

#Les algorithmes suivants interagissent avec un tableau de valeurs qui donne les infos des joueurs et un fichier tete qui sert à les sauvegarder. Le tableau sera de la forme [Joueur1,joueur2,joueur3,joueur4,monstre]. (a priori)





#extracteur de données dans un fichier qui sera modifiable. obj pour objectif (nom ou donnée)
def dataex(fichier,obj,dossier):
    nomfichier='D:/Users/Nicolas/Documents/MHjdr/Data/'+dossier+'/'+fichier+'.txt'
    f=open(nomfichier, 'r')
    donnees=f.readlines()
    data = []
    if obj==1:
        for line in donnees:
            if line !='\n':
                line=line.split()
                data.append(line[obj]) #on récupère la donnée correspondant à l'objectif

        for i in range(1,len(data)) :
            if "*" in data[i]:
                    data[i]=data[i]
            elif "," not in data[i]:

                data[i]=float(data[i]) #la "," sert à indiquer puis indexer les listes de liste dans le string global.
            else :
                data[i]=data[i].split(",")

                for j in range(len(data[i])):
                    if 'Ele' not in data[i][j]:
                            data[i][j]=float(data[i][j]) #maintenant qu'on a identifié ce qui doit être une liste, on transforme en entiers ses membres.
    if obj==0:
        for line in donnees:
            line=line.split(' ')
            data.append(line[0]) #cas où on veut les noms des données

    return data



def datascripter(liste,fichier,dossier): #permet d'éditer le fichier texte en prenant en argument la liste qui servira à le compléter. A tester.
    t=liste
    nomfichier='D:/Users/Nicolas/Documents/MHjdr/Data/'+dossier+'/'+fichier+'.txt'
    noms=dataex(fichier,0,dossier)
    f=open(nomfichier, 'w')#fichier caractéristique
    for i in range (len(liste)):

        t[i]=str(t[i]) #conversion en string
        t[i]=t[i].replace("[","",100) #On remplace les crochets par rien pour l'écriture des listes de listes
        t[i]=t[i].replace("]","",100) #Obtient la structure d'extraction du fichier texte où les listes commencent par "," et dont les membres de la liste sont séparées par des ","
        t[i]=t[i].replace("'","",100) #Lors de l'écriture, des ' se greffent dans les lignes, ce qui fait buguer le programme de lecture. en attendant une meilleure solution, on les retire.
        t[i]=t[i].replace(", ",",",100) #on remplace les espaces qui peuvent suivre des virgules par des virgules seules

        t[i]=noms[i]+' '+t[i] #On réécrit le nom puis la valeur de la donnée séparée par un espace pour chaque donnée

    t='\n'.join(t) #permet de transformer une liste en chaine de caractère en utilisant '\n' comme séparateur, indiquand qu'il faut changer de ligne
    f.writelines(t) #Réécriture du fichier


def Attack(atk,fichier):
    moves=dataex(fichier,0,'Armes') #récupère les noms
    dmg=dataex(fichier,1,'Armes') #récupère les données
    No=0
    i=1
    for x in moves:
        if atk in x:
            No=i #si le nom correspond, on retient l'indice
        else:
            i+=1

    return dmg[No]

#D:/WINDOWS_SEVEN/Users/Nicolas_Admin/Documents/MHjdr/MHdata.txt