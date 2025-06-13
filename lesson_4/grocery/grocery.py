"""
implement a program that prompts the user for items, one per line,
until the usr inputs control-d

then output the uesr's grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted the item
    - no need to puralize the items

treat the uers's input case-insenstively
"""

def main():
    grocery = []
    while True:
        try:
            grocery.append(input().upper())
        except EOFError:
            break
        else:
            continue

    grocery_sorted = sorted(grocery)

    grocery_list = {item:grocery_sorted.count(item) for item in grocery_sorted}

    for item, count in grocery_list.items():
        print(count, item)

main()


