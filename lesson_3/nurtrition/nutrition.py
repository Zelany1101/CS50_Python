# implement a program that prompts users to input a fruit and then output the number of calories
# in one portion of that fruit per the FDA's poster for furits
# capitalization aside, assume the users will input fruits exactly as written in the poster
# ignore any input that isn't a fruit

fruits_calories = {
    'apple' : 130,
    'avocado' : 50,
    'banana' : 110,
    'cantaloupe' : 50,
    'grapefruit' : 60,
    'grapes' : 90,
    'honeydew melon' : 50,
    'kiwifruit' : 90,
    'lemon' : 15,
    'lime' : 20,
    'nectarine' : 60,
    'orange' : 80,
    'peach' : 60,
    'pear' : 100,
    'pineapple' : 50,
    'plums' : 70,
    'strawberries' : 50,
    'sweet cherries' : 100,
    'tangerine' : 50,
    'watermelon' : 80
}

def main():
    item = input('Item: ').lower()
    fruit(item)


def fruit(item):
    for i in fruits_calories:
        if i == item:
            print(f'Calories: {fruits_calories[item]}')
        else:
            continue
main()
