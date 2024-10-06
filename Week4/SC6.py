P1 = str(input("Batu, Gunting, Kertas: "))
P2 = str(input("Batu, Gunting, Kertas: "))

p1=P1.lower()
p2=P2.lower()

if p1 == "gunting" and p2 == "batu" :
  print ("P2 Win")
elif p1 == "gunting" and p2 == "kertas" :
  print ("P1 Win")
elif p1 == "batu" and p2 == "gunting" :
  print ("P1 Win")
elif p1 == "batu" and p2 == "kertas" :
  print ("P2 Win")
elif p1 == "kertas" and p2 == "gunting" :
  print ("P2 Win")
elif p1 == "kertas" and p2 == "batu" :
  print ("P1 Win")
elif p1 == "gunting" and p2 == "gunting" :
  print ("Tie, Silahkan ulangi lagi")
elif p1 == "batu" and p2 == "batu" :
  print ("Tie, Silahkan ulangi lagi")
elif p1 == "kertas" and p2 == "kertas" :
  print ("Tie, Silahkan ulangi lagi")
else :
  print ("Salah kocak")
