from random import *

print("""
************    ***           ****             ****************
************    ***          **  **            ****************
***             ***         **    **           **            **
***             ***        **      **          **            **
***             ***       ************         **            **
***             ***      **************        **            **
***             ***     **            **       **            **
***             ***    **              **      **            **
************    ***   **                **     ****************
************    ***  **                  **    ****************

""")


stringa = ("""La password è stata sbagliata--""")

dom = (input("""Che programma vuoi usare?
             ricorda_psw
             numeri random
             """))

if(dom=="ricorda_psw"):
   
  passwd = (input("Scrivi la password: "))
  if(passwd=="password"):
   print("Password di accesso giusta")
   sito = (input("Quale password vuoi? "))
   
   if(sito=="tiktok"):
      print("password tiktok")
      
   elif(sito=="youtube"):
      print("password youtube")
   elif(sito=="instagram"):
      print("password instagram")
   elif(sito=="tv"):
      print("2580, password tv camera tom/leo")
   else:
      print('Mi dispiace ma non riesco a trovare una password')
  else:
    print("password di accesso sbagliata")
    
    file1 = open("registro.txt","a")
    file1.write(stringa)
    file1.close()
    
elif(dom=="numeri random"):
   print("""
Questo programma serve a generare dei numeri casuali, scegli qui sotto il numero massimo

         """)
   print("""Quale vuoi:
         1 da 1 a 100
         2 da 1 a 999
         3 da 111 111 a 999 999
         4 da 1111 a 4444""")



   domanda = (input("1,2,3,4? "))



   if (domanda=="1"):
      print("Numero casuale generato")
      print(randint(1,100))

   elif(domanda=="2"):
      print("Numero casuale generato")
      print(randint(1,999))

   elif(domanda=="3"):
      print("Numero casuale generato")
      print(randint(111111,999999))

   elif(domanda=="4"):
      print("Numero casuale generato")
      print(randint(1111,4444))
      
   else:
      print("Puoi farcela non è difficile")

   
else:
   print("Mi dispiace ma il programma",dom, "non esiste")
