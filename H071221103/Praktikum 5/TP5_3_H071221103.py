array1 = input("input array ke 1: ")
my_array1 = set(int(item) for item in array1.split())
array2 = input ("input array ke 2: ")
my_array2 = set(int(item) for item in array2.split())

print (f"terdapat {len(my_array1 & my_array2)} buah duplikat yaitu  {tuple(my_array1 & my_array2)}")