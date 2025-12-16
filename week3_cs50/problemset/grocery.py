"""
Fill a dictionary with the items asa keys and their number of instances as values. 
Sort the dictionary
output
"""


def main():
    items = {}

    while True:
        try:
            grocery = input().upper()
        except EOFError:
            break
        else:
            if grocery not in items:
                items.update({grocery: 1})
            else:
                items[grocery] += 1

    for item in sorted(items):
        print(f"{items[item]} {item}")    

main()