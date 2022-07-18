# moyenne de 2 nombres
"""
a = float(input("entrez a : "))
b = float(input("entrez b : "))
moyenne = (a + b )/2
print("La moyenne de a et b est :", moyenne)
"""
# calcul moyenne de n nombres

n = int(input("entrez la valeur de n : "))
moyenneN = 0

for a in range(1, n+1) :
   x = float(input("entrez x : "))
   moyenneN = moyenneN + x
   print (moyenneN/n)


