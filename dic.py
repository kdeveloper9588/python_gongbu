bloom = {'1월':'수선화',
         '3월':'프리지아',
         '4월':'라일락',
         '5월':'장미',
         '6월':'장미',
         '7월':'무궁화',
         '11월':'국화',}

bloom
print(bloom)        

for key, value in bloom.items():
  if value == '라일락' :
    print(key)

for key, value in bloom.items():
    
  if key == '4월' :
    print(value)  

bloom.keys()   

bloom.values()

list(bloom.keys())

[key for key, value in bloom.items() if value == '장미']#키와 벨류로 블럼에서 장미인 놈의 키를 찾는다.

[value for key, value in bloom.items() if key == '4월']