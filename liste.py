temperatures = [10,15,36,7]
temperatures[3]=27 # change element
print(temperatures)
print(temperatures[1])
print(temperatures[3])
temperatures.pop(1)
print(temperatures)
temperatures.append(18)
print(temperatures)
temperatures.insert(0,45)
print(temperatures)
# tri sur liste 
temperatures.sort()
print(temperatures)
# maximum
print(max(temperatures))
# minimum
print(min(temperatures))
#len()
nombre_de_jours_releves = len(temperatures)
print(nombre_de_jours_releves)
#count()
print(temperatures.count(36))
