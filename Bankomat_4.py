# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Uppdrag 1, Bankomat

# %%
from termcolor import colored
from datetime import datetime
import pickle




## ------- Functions -----

## skriv ut huvudmeny (meny A)
def huvudmeny():
       print(colored('*** HUVUDMENY ***','yellow'))
       print('1. Skapa konto')
       print('2. Logga in på konto')
       print('3. Avslua')

## skriv ut kontomeny (meny B)
def kontomeny():
        print(colored('*** KONTOMENY ***','blue'))
        print('1. Ta ut pengar')
        print('2. Sätt in pengar')
        print('3. Visa saldo')
        print('4. Visa transaktion')
        print('5. Avsluta')

## skriv ut felmedelande
def printfel(meddelande, color):
    print(colored(f'!!! Felmeddelande: {meddelande} !!!',color))

## läs menyvalet
def valet(nval):
    while True:
        sel = int(input("Ange val:"))
        if sel >= 1 and sel <= nval:
            return sel
        else:
            print(f'Val måste vara mellan 1 och {nval}')

## läs kontonummer
def laskonto():
    Knummer = int( input('Ange kontonummer:') )
    return Knummer

## om kontonummer finns eller inte
def kontofinns(knummer,kontoList):
    finns = False
    for konto in kontoList:
        if konto.nummer == knummer:
            finns = True
            break
    return finns

## ---- End of Functions -----

## ------- Classess -----

class Kontoclass:
    def __init__(self):
        self.nummer = ""
        self.saldo = 0

        self.date =[]
        self.belop = []
        self.type = []

    def Transaktion(self, belop, typ):
        datum = datetime.now()
        date = datum.strftime('%Y-%m-%d %H:%M')
        self.date.append(date) 
        self.belop.append(belop)
        self.type.append(typ)

## ------- End of Classess -----

#------------------------------------------------------------------#
#----------------------------- MAIN CODE --------------------------#
#------------------------------------------------------------------#

#kontoList = []

## Open log file for reading
with open ('konto.log', 'rb') as f:
    kontoList = pickle.load(f)


while True:
# Meny A
    huvudmeny()
    valA = valet(3)

 # Avslut
    if valA == 3:
        print(colored('Avslut', 'red'))
        break
 
 # konot register   
    elif valA == 1:
       num = laskonto()
       finns = kontofinns(num,kontoList)

       if finns == True:
           printfel('redan tagit', 'red')
       else:
           nykonto = Kontoclass()
           nykonto.nummer = num
           kontoList.append(nykonto)
           continue

 # Login
    elif valA == 2:
        num = laskonto()
        finns = kontofinns(num,kontoList)
        if finns == False :
           printfel('Konton finns ej','red')
        else:
# Meny B
          while True:
           kontomeny()
           valB = valet(5)

           for konto in kontoList:
              if konto.nummer == num:
                 kontoObj = konto
                 break

   # Uttag
           if valB == 1:
               belopp = int( input('Ange belopp:') )
               if belopp > kontoObj.saldo:
                   printfel('Ingen tillräckling med pengar', 'red')
               else:
                   kontoObj.saldo = kontoObj.saldo - belopp
                   print(colored (f'ny saldo: {kontoObj.saldo}', 'green') )
                   kontoObj.Transaktion(belopp,"uttag")

               continue

   # Insätt            
           elif valB == 2:
                belopp = int( input('Ange belopp:') ) 
                kontoObj.saldo = kontoObj.saldo + belopp
                print(colored (f'ny saldo: {kontoObj.saldo}', 'green') )
                kontoObj.Transaktion(belopp,"insätt")
                continue

   # Saldo            
           elif valB == 3:
                print(colored (f'Saldo: {kontoObj.saldo}', 'green') )

   # Transaktion            
           elif valB == 4:
                print(colored ('Last 3 transaktions:' , 'green') )
                n = len(konto.date)
                if n > 3:
                   n = 3
                for i in range(n):
                   print(f'#{i} date: {konto.date[i]} , belop: {konto.belop[i]}, typ: {konto.type[i]}')

   # Avslut
           elif valB == 5:
                print(colored('logga ut', 'red'))
                break


# %%
## Rewrite the logfile

with open ('konto.log', 'wb') as logfile:
    pickle.dump(kontoList, logfile)


# %%
