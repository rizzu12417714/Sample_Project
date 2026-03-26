# Date 04-02-2026




import numpy as np

# z = np.full((3, 4), 0.11)
# print(z)

# ab = np.arange(10, 30, 5)       
# print(ab)

# w = np.arange(10, 30, 5)
# print(w)

# print(np.arange(0, 2, 0.3))

# print(np.linspace(0, 5/3, 6))    


# bb = np.random.rand(3,4)
# print(bb)
# print(bb.ndim)

# cc = np.random.randint(4, 9, size=(2,3))   
# print(cc)

# dd = np.random.uniform(4, 9, size=(2,3))
# print(dd)



# a=np.array([[1, 2, 3], [4, 5, 6]])
# print(a)
# print("type", type(a))
# print("dimension", a.ndim)

# print("shape", a.shape)

# print("size", a.size)
# print("datatype of elements", a.dtype)
# print("itemsize", a.itemsize)

#Insexing one dimensional numpy arrays
# a = np.array([10, 20, 30, 40, 50])
# print(a[3])     
# print(a[2:5])    
# print(a[::2])    
# print(a[::-1])
# print(a)

# Different with regular python  arrays

# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# a_slice = a[1:5].copy()  # Create a copy of the slice
# a_slice[1] = 1000
# print(a)  # Original array is modified
# print(a_slice)


# aa=np.array([1, 2, 3 , 4, 5, 6, ])
# print(aa)
# aa_slice = aa[2:5].copy()  # Create a copy of the slice
# print(aa_slice)
# aa_slice[2] = 100
# print("aa_slice is", aa_slice)
# print("aa is", aa)



# DATE 05-02-2026

# a = np.array([[1, 1], [0, 1]])
# b= np.array([[2, 0], [3, 4]])
# print(np.dot(a, b)) 



# m = np.array([20, -5, 30, 40])
# print (m < [15, 16,35,36])
# print(m < 25)

# print(m[m < 25])    


# b = np.arange(12).reshape(3, 4)
# print(b)
# print ("sum across columns:", b.sum(axis=0) )
# print("min across rows:", b.min(axis=1) )
# print("cumulative sum across rows:", b.cumsum(axis=1) )
# print(b.cumsum(axis=1) )

# print ("...............")   #transpose



# m=np.arange(6).reshape(2,3)
# print(m)
# print(m.T)




# c=np.arange(24).reshape(2,3,4)
# print(c)
# print(c.sum(axis=0))  #add to blocks
# print(c.sum(axis=1))  #sum  column
# print(c.sum(axis=2))  #row to row   







