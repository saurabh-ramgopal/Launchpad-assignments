list =[] 
s = input() 

words = s.split(' ') 

for i in words: 
    list.insert(0, i) 
  
print(" ".join(list))