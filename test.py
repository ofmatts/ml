dict = {"one":1,"two":2,"three":3}
print(dict)

dict_iterator= dict.keys()
print(dict_iterator) 

for i in dict_iterator:
    print(i)

    
some_var=5

if some_var>10:
    print("some_var is bigger than 10")
elif some_var<10:
    print("some_var is lower than 10")
else:
    print("some_var is 10")

print("\n\n")


for animal in ["dog", "cat", "mouse"]:
    print("{} - is a mammal".format(animal))

x=0

while x < 4:
    print(x)
    x+=1

A = [1,2,3]
    
    
try:
    print(A[1])
    print(A[3])
    #raise IndexError("Its index error") // raise выбрасывает ошибку
except IndexError as e:
    print("pizdec")
    pass
except (TypeError, NameError):
    print("pizdec 2")
    pass
else:
    print("Its okay!")

    
