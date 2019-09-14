
#Etablir une liste exaustive du moveset ainsi que des points faibles
#Pour les parties brisables, introduire une liste avec en complément les PV de la partie
from math import *


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
Attaque=0
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

HPlist=Hplist=("Punya",Punya[HP][0],"Tyrliel",Tyrliel[HP][0],"Shinza",shinza[HP][0],"Minyarr",Minyarr[HP][0],"Garuga",garuga[0][0])

##Données des persos

#NomJoueur=[Attaque, Sharpness, DégatsAffinité, [Element , dégats], Def Phy, [Res Feu, Eau, Foudre, Glace, Dragon, Res elementaire générale], Shield capacity, Blessing value, Armor Penetration, Critical Element, Sharpness bonus, (HP,Hpmax), recovery bonus en points sur 100]

Shinza=shinza=Thraror=thraror=[149, Bleue, 35, None, 65, [10,-5,-7,0,0,65],0,0,0,0,1,[95,95],0]

Punya=punya=pierre=Pierre=[171, Bleue, 25, [Feu, 5],70,[5,0,-5,5,0,70],20,0,0,0,0,[75,80],0]

Tyrliel=tyriel=tyrliel=Tyriel=Vic=vic=[174, Vert, -25, None, 80, [-5,5,0,0,10,80],50,50,0,0,0,[96,115],0]

Minyarr=minyarr=Aur=aur=[127, Jaune, 25, [Glace,10],51,[10,0,2,5,5,60],0,0,1,0,0,[80,80],0]

# le # permet de verrouiller les données de HP pour éviter qu'un crtl+e les réinitialise lors d'une modification du code

test=[171, Bleue, 25, [Explosion, 5],70,[5,0,-5,5,0,70],20,0,0,0,0,[75,80],0]

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

Garuga=garuga=[[3000,3000],[100,0,66,33,33],[300,300,0],[200,200,0],[120,120,0],[150,150,0],[70,70,0]]
Garugatest=garugatest=[[3000,3000],[95,0,66,33,33],[300,300,0],[200,200,0],[120,120,0],[150,150,0],[70,70,0]]
#mettre un hashtag lorsque le combat en commencé pour éviter de réinitialiser les valeurs en HP des monstres et joueurs par accident lors d'un crtl+e

##Algorithmes

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

def sharpcalc(j,p):
    #j pour joueur
    #p pour partie touchée
    #Principe de l'algo : donne un bonus en fonction de la sharp et un malus en fonction du blindage, puis compile tout pour donner la proba
    #rappel : j[10] correspond au bonus de sharpness du joueur, du à des bonus externes ou aux propriétés de son arme
    co=j[1]
    b=Sharpness[co+7]+j[10]
    c=Blindage[p+5]
    tot=b+c #chance totale sur 10 est les chances de base c plus le bonus b
    if b+c>10:
        return 10
    if b+c<0:
        return 0
    return b+c


def staminacost(j,dmg):
    #j pour joueur
    #dmg pour l'attaque du monstre
    s=round(3-(round((j[6]-dmg)/10)))
    #s pour stamina cost, égal à  3-( capacité-dégats totaux)/10 arrondi à l’entier le plus proche
    return(s)#retourne le stamina cost PUR, qui sera tronqué par la suite




def dvm(joueur,partiedumonstre,monstre,attaqueutilisée,critique=False,rawpur=0,elempur=0,): #dvm = Damage vs Monstre
    #j=Nom Joueur
    #p=Partie touchée : Donne le blindage
    #m=Monstre
    #a=Attaque utilisée, liste contenant la valeur totale de dégats ainsi que le nombre de coups
    #c=Crit ?
    #elempur=dégats élémentaires purs spécifiques (décharges élémentaires)
    #rawpur=dégats raw purs spécifiques (fioles de choc)
    j=joueur
    p=partiedumonstre
    m=monstre
    a=attaqueutilisée
    c=critique
    atk=j[0]
    AP=j[8]
    CE=j[9]
    if c==True :
        Cd=(100+j[2])/100 #cd for crit damage multiplier
    else :
        Cd=1
    Sh=Sharpness[j[1]]
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

    #calcul de la réduction de dégats due au blindage.
    red=(100-Bl[p-AP])/100
    if a[1]==0:
        red=1

    #calcul des dégats initiaux : dégats de base/100 * attaque * resistance du monstre * sharpness * crit
    raw=round(((a[0]+rawpur)/100)*atk*(red)*Sh*Cd)
    ele=round((a[1]*Eledmg+elempur)*(1-(m[1][Elem]/100))*CE*Sh*red)
    #affichage des valeurs
    print("Raw = ",raw, "Elemental = ", ele, elementorailmentdisplay(Elem))
    print("Total = ", raw+ele)
    if len(a)==3 and p==tête:
        DmgKO=a[2]
        print("Dégats KO = ",a[2])
        monstre[2][0]-=DmgKO
        print("Il reste",monstre[2][0],"PV en KO au monstre")

    #calcul des chances de perforation
    perfo=sharpcalc(j,p-AP)
    if perfo==10 :#or  a[0]>=Bl[p-AP]:
        print("Pas de rebond possible")
        #if a[0]>=Bl[p-AP]:
            #print("(Armor Override)") #Si la puissance de base d'une attaque dépasse la résistance de la partie de la cible , le coup traverse peu importe le blindage
    if perfo==0 and  a[0]<Bl[p-AP]:
        print("Rebond obligatoire")
    if perfo>0 and perfo<10 and a[0]<Bl[p-AP]:
        print("Chances de perforer = ",perfo,"/10")



    #disjonctions de cas en fonction des ailments
    if Ailment!=-1:
        monstre[Ailment-2][0]-=round(Ailmentdmg*a[1])
        print("Le monstre accumule ",round(Ailmentdmg*a[1])," PV en ", elementorailmentdisplay(Ailment))
        print("Chances de statut = ",round((Ailmentdmg/(2*monstre[Ailment-2][1]))*100),"/100")
        print(monstre[Ailment-2][0],"/",monstre[Ailment-2][1])
    if monstre[2][0]<=0 :
        m[2][2]+=1 #incrémentation du compteur de KO
        monstre[2][0]=monstre[2][1]*0.5*(1+monstre[2][2]) #Réinitialisation avec augmentation du palier de KO en fonction du nombre de KO
        print("KO !")
    if monstre[3][0]<=0:
        m[3][2]+=1
        monstre[3][0]=round(monstre[3][1]*(1+m[3][2]*0.4))
        monstre[3][1]=monstre[3][0]
        print("Empoisonné ! Dégats de poison = ",round(m[0][1]/100))
    if monstre[4][0]<=0:
        m[4][2]+=1
        monstre[4][0]=round(monstre[4][1]*(1+m[4][2]*0.4))
        monstre[4][1]=monstre[4][0]
        print("Paralysé !")
    if monstre[5][0]<=0:
        m[5][2]+=1
        monstre[5][0]=round(monstre[5][1]*(1+m[5][2]*0.4))
        monstre[5][1]=monstre[5][0]
        print("Dodo !")
    if monstre[6][0]<=0:
        m[6][2]+=1
        monstre[6][0]=round(monstre[6][1]*(1+m[6][2]*0.1))
        monstre[6][1]=monstre[6][0]
        print("BOOM ! 120 PV !")
        monstre[0][0]-=120
        m[0][0]-=120


    #application des dégats infligés au monstre
    monstre[0][0]-=raw+ele
    print("Il reste ",monstre[0][0]," PV au monstre")
    if m[0][0]<=0:
        print("Victoire !")

def dvj(j,dmg,Ele=-1, Eledmg=0, Blocage=False, blessing=False): #dégats v joueurs
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
    if not Ele==None:
        modele=(100-3*(j[5][Ele]))/100 #modification elementaire = (100-3 fois la res élémentaire correspondante)/100
    else:
        modele=1
    if modele<0:
        modele=0 #une résistance si forte qu'elle rend le modificateur négatif modifie la valeur de modification à 0
    redele=defele/(30+defele)*modele #Reduction de dégats élémentaire
    raw=round(dmg*(1-redphy))*red #Dégats de base non élémentaires
    elem=round(Eledmg*(1-redele))*red #Dégats de base élémentaires
    svg=round(raw+elem)
    if raw+elem-Sh<0:
        Sh=raw+elem
    Bc=round((raw+elem-Sh)*(round(1-Sh/(raw+elem),1)))#Dégats réellement subis après absorption par le potentiel bouclier
    #La valeur obtenue est ensuite multipliée par un modifiacteur empêchant la valeur de PV perdue d'être escessive si le bouclier est très faible devant la puissance de l'attaque. Ce modificateur est arrondi à la première décimale, entre autres pour les cas où l'attaque est endessous de deux fois plus forte que le bouclier.
    if Bc<0:
        Bc=0
        #Si le bouclier est plus fort que l'attaque, les dégats subis sont ramenés à 0

    #affichage des données
    print("Raw basic = ",raw, "Ele basic = ", elem,". Total brut =",svg)


    #calcul des marquers d'endurance
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

        if bool=="True" or bool=="oui" or bool == "true" :
            j[HP][0]-=Bc #modification de la jauge de vie du joueur
            print(Bc)
            print(svg)
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

def heal(joueur,pv):
    j=joueur
    j[HP][0]+=pv
    if j[HP][0]>j[HP][1]:
        j[HP][0]=j[HP][1]
    if pv>=0:
        print(pv,"HP récupérés. Total",j[HP][0])
    if pv<0:
        print(pv, "HP perdus. Restants",j[HP][0])
    if j[HP][0]<=0:
        print("Joueur Ko.")

def buff(joueur, buffcategory,buffnumber):
    j=joueur
    b=buffcategory
    n=buffnumber
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



##Base de données des attaques

#Les attaques sont des tuples qui comprennent la puissance, le multiplicateur de coups (important pour les dégats élémentaires), et si nécessaire les dégats KO.

#Sns
Weak=(24,4)
Strong=(26,2.5)
Roundslash=Rslash=(30,1.5)
Gapcloser=(20,1)
Shbash=(20,1,20)
Backstrike1=(25+30,2)
BsH=(50,1,40)
BsL=(25,1)


#DualBlades
DbGapclo=(15,1)
Dbbase=(5+5+7+7,3)
Fourfold=(8+8+9+9,3)
Eightfold=(8+8+10+10,3)
Slingshot=(60,3)
Demondance=(20+40+60,8)
Dbrslash=(30,2)

AdFourfold=(7+7+8+8,3)
AdEightfold=(8+8+9+9,3)
Adrslash=(28,2)
AdDemondance=(30+50,6)


#longsword
Vslash=(28,1)
Thrust=(12,1)
Tcombo=(12+15,1.5)
Fadingslash=(25,1)
Sslash1=(28,1)
Sslash2=(20,1)
Sslash3=(10+15+25,2)
Srslash=(65,1)
Sthrust=(20)
Shelmbreaker=(65,2)
Shelmbreakerred=(130,5)
Scounter=(25,1)


#Greatsword
Vslash0=(50,1)
Vslash1=(50*1.3,1)
Vslash2=(50*1.6,1.5)
Vslash3=(50*2.2,2)
Scharge0=(70,1)
Scharge1=(70*1.3,1)
Scharge2=(70*1.6,1,5)
Scharge3=(70*2.2,2)
Ssweep0=(60,1)
Ssweep1=(60*1.3,1)
Ssweep2=(60*1.6,1.5)
Ssweep3=(60*2.2,2)
Sbash0=(30,1,20)
Sbash1=(30*1.3,1,20*1.3)
Sbash2=(30*1.6,1.5,20*1.6)
Sbash3=(30*2.2,2,20*2.2)


#Lance
Poke=(12,1)
Pokecombo=(12+13,2)
Pokefinisher=(40,1)
Gcounter1=(40,1)
Gcounter2=(60,2)
Assault=Assaut=(24,3)
#Assaultfinisher àentrer par le MJ


#Chargeblade
Bslash=(13,1)
Cslash=(12+13,2)
Cbgapclo=(20,1)
Cdbslash=(25+30,2)
CbRslash=(27,1)
CbFslash=(20,1)
PD=(4,0,8)
CbSlam=(30,1)
Dcharge1=(20,1)
Dcharge2=(10+20,2)
AED=Aed=aed=(70,1) #+6PD
SAED=Saed=(20+80) #+X PD
#Pour la charge blade, faire deux fiches de perso (une avec Cb chargée et l'autre sans


#Bow
Shot1=(10,1)
Shot2=(26,2.5)
Shot3=(45,3.7)
Shot4=(17*4,5)
Spread0=(20,2)
Spread1=(30,3.5)
Spread2=(40,4.8)
Spread3=(50,6)
Spread4=(60,7)
#Dragonpiercer à vois avec le MJ


#Hammer
#Bien penser à donner un bonus de 2 en sharpness
Smash=(30,1,20)
Homerun=(50,1,50)
Charge1=Smash
Uppercut=(40,1,70)
Rollthunder=(20*2,2,20)
Bigbang=(10+25+100,3,90)

#Swithcaxe
Aslam=(30,1)
HnS=Wildswing=(40,2)
SaFslash=(20,1)
Amorph=(40,1)
Saslash=(30,1)
SaDslash=(30+40,2)
Smorph=(30,1)
Spmorph=(20+30+70,3)
Eldcharge=(20,1)
Eldchargetick=(20,2)
#Explosion à entrer par le MJ, de la forme (20+X*20,2+X)
Zsumdcharge=(28,1)
Zsdchargetick=(12*2,2)
#Zsexplosion à entrer par le MJ, de la forme (30*x+30, x+2)

#Gunlance
GlPoke=(20,1)
GdPoke=(17,1)
Shot=(10,0)
Chargedshot=Cshot=(25,0)
Slam=(35,1)
#Boom=burstshot à entrer par le MJ (10*X,0)
Wyvernfire=(150,0)











