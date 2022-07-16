# pop () sans position specifiee renvoie au dernier argument de la liste

mot_de_passe = ["Tracteur","charrue", "Semoir", "Moissonneuse-batteuse", "Herse"]
code = mot_de_passe.pop()
print(code)
mot_de_passe.append(9)
print(mot_de_passe)
print(code)
code = mot_de_passe.pop()
print(code)
