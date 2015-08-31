questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?"
}

strong_ingredients = ["glug of rum", "slug of whisky", "splash of gin"]
salty_ingredients = ["olive on a stick", "salt-dusted rim", "rasher of bacon"]
bitter_ingredients = ["shake of bitters", "splash of tonic", "twist of lemon peel"]
sweet_ingredients = ["sugar cube", "spoonful of honey", "spash of cola"]
fruity_ingredients = ["slice of orange", "dash of cassis", "cherry on top"]

import random
my_drink = []

my_input = raw_input(questions['strong'])
responses = {
"strong": [my_input]
}

if my_input == "Yes":
    my_drink.append(random.choice(strong_ingredients))
    
my_input2 = raw_input(questions['salty'])

responses = {
"salty": [my_input2]
}
    
if my_input2 == "Yes":
    my_drink.append(random.choice(bitter_ingredients))
    
my_input3 = raw_input(questions['bitter'])

responses = {
"bitter": [my_input3]
}
    
if my_input3 == "Yes":
    my_drink.append(random.choice(sweet_ingredients))
    
my_input4 = raw_input(questions['sweet'])

responses = {
"sweet": [my_input4]
}
    
if my_input4 == "Yes":
    my_drink.append(random.choice(salty_ingredients))
    
my_input5 = raw_input(questions['fruity'])

responses = {
"fruity": [my_input5]
}
    
if my_input5 == "Yes":
    my_drink.append(random.choice(fruity_ingredients))
    
print my_drink 
    
