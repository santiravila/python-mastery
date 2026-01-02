def f(*args, **kwargs):
    print("Positional:", kwargs)
    #print("Keyword:", kwargs)
    

f(galleons=100, sickles=50, knuts=25)

#def total(galleons, sickles, knuts):
#    return (galleons * 17 + sickles) * 29 + knuts

#coins = {"galleons": 100, "sickles": 50, "knuts": 25}

#print(total(**coins), "Knuts")

#coins = [100, 50, 25]

#print(total(*coins), "Knuts")

#first, _ = input("What's your name? ").split(" ")
#print(f"hello, {first}")