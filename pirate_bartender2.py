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


def drink_responses(): 
    
    responses = {            #creating a brand new dictionary and assigning it the name 'responses'
    }
    
    for flavor in questions:
        my_input8 = raw_input(questions[flavor]) # How to call a value, calling variable flavor
        responses[flavor] = my_input8
    
    return responses
    
    
    
def drink_maker(responses):
    import random
    my_drink = []
    if responses['strong'] == "Yes":
        my_drink.append(random.choice(strong_ingredients))
        print my_drink

if __name__ == '__main__':
   new_drink = drink_responses()  #now new drink is the result of the function
   drink_maker(new_drink)