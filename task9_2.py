list1 = list (input("Enter the list : "))
result = all (map(lambda x: isinstance(x, (int, str)),list1))

if result:
    print ("Every element is an integer or a string")
else:
    print ("Not all element is an integer or a string")