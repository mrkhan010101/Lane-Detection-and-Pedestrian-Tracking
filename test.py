import numpy as np                 
  
# creating the first array
arr1 = np.array([2, 6, 9, 4])
 
# displaying the identity of arr1
# print(id(arr1))
 
# shallow copy arr1 in arr2 using view()
arr2 = arr1.copy()
 
# displaying the identity of arr2
# print(id(arr2))
  
# making a change in arr1
arr1[1] = 7                       
  
# displayin the arrays
print(arr1)
print(arr2)