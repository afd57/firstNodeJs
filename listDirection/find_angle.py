import math 

AB = int(input())
BC = int(input())

'''
aˆ2 = bˆ2 + cˆ2 
'''
hipotenus = math.sqrt(AB**2 + BC**2)
print('Hipotenus', hipotenus)
c_degree = math.asin(AB/hipotenus)
print(math.degrees(c_degree))

result = 0
if math.degrees(c_degree) - int(math.degrees(c_degree)) >= 0.5:
    result = int(math.degrees(c_degree)) + 1
else:
    result = int(math.degrees(c_degree))
print(result)
