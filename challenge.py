"""Function to be decorated should give me the first name of a person
Its decorator should return the first name as a string with is awesome
 attached if the name starts with a [m, d, k]
if not not it should says that the name smells like teen spirit
There needs to be also some driver code
names = ["Connor", "Kevin", "Dylan", "Diana", "Caleb", "Lizette", "Gulfem", "Marcus", "Marco"] """

#input name
#output name + string


names = ["Connor F", "Kevin R", "Dylan S", "Diana B", "Caleb S", "Lizette E", "Gulfem A", "Marcus B", "Marco V"]
def add_suffix(func):
    def inner(s):
        if func(s)[0].lower() in {"m","d","k"}:
            return func(s) + " is awesome"
        else:
            return func(s) + " smells like Teen Spirit"
    return inner

@add_suffix
def first_name(s):
    first = s.split()[0]
    return first

for name in names:
    print(first_name(name))
