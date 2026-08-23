points=[(7,5),(2,4),(3,6),(10,7)]
distances=[]
d=0
def euclideanDistance():

  for i in range(len(points)-1):
     x1,y1=points[i]
     x2,y2=points[i+1]

     d=((x2-x1)**2+(y2-y1)**2)**(1/2)

     d=round(d,2)
     distances.append(d)
     print("Distance",i+1,":",d)
  
  print("All distances:" ,distances)

euclideanDistance()

print("Min distance:",min(distances))
 
 


    
