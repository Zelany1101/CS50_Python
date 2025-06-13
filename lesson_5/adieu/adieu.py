"""
implement a program that prompts the user for names, one per line, until the user inputs control-d
assume user will input at least one name
then bid adieu to those names, separating two with one an, three names with two commas and one and, and n names with n-1 commas and one and

ex:
Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

inflect library -- generate plurals, singular nouns, ordinals, indefinite articles, and word-based representations of numbers
    import inflect
    p = inflect.engine()

inflect library methods:
    - plural, plural_noun, plural_verb, plural_adj, singular_noun, no, num
    - compare, compare_nouns, compare_verbs, compare_adjs
    - a, an
    - present_participle
    - ordinal, number_to_words
    - join
    - inflect, classical, gender
    - defnoun, defverb, defadj, defa, defan

join words into a list:
>>> p.join(("apple", "banana", "carrot"))
'apple, banana, and carrot'
>>> p.join(("apple", "banana"))
'apple and banana'
>>> p.join(("apple", "banana", "carrot"), final_sep="")
'apple, banana and carrot'
>>> p.join(('apples', 'bananas', 'carrots'), conj='and even')
'apples, bananas, and even carrots'
>>> p.join(('apple', 'banana', 'carrot'), sep='/', sep_spaced=False, conj='', conj_spaced=False)
'apple/banana/carrot'
"""

import inflect

p = inflect.engine()

def name_list():
    name = []
    while True:
        try:
            name.append(input('Name: '))
        except EOFError:
            return name

def main():
    name = name_list()
    print(f'Adieu, adieu, to {p.join((name))}')

if __name__ == '__main__':
    main()
