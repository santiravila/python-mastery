def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


# pythonic way for strings using print function
#print("meow " * 3)


# typical cycle
#i = 3
#while i > 0:
#    print("meow ", end='')
#    i -= 1 

#print('')


# for (no pun-intended) iterating over a list of items
#for i in [0, 1, 2]:
#    print("meow ", end='')
    # i can also work with i
#    print("current iteration: ", i)


# with range (returns a range of values default starting at 0)
#for _ in range(3):
#    print("meow ", end='')


    
# infinite loop for validation
#while True:
#    n = int(input("What's n? "))
#    if n > 0: 
#        break

#for _ in range(n):
#    print("meow ", end='')
