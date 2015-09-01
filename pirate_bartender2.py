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

    responses = {
    }
    
    my_input = raw_input(questions['strong'])
    my_input2 = raw_input(questions['salty'])
    my_input3 = raw_input(questions['bitter'])
    my_input4 = raw_input(questions['sweet'])
    my_input5 = raw_input(questions['fruity'])
    
    responses = {
        "strong": my_input,
        "salty":my_input2,
        "bitter":my_input3,
        "sweet":my_input4,
        "fruity":my_input5
    }
    
    return responses
    
def drink_maker(responses):
    import random
    my_drink = []
    if responses['strong'] == "Yes":
        my_drink.append(random.choice(strong_ingredients))
        print my_drink

if __name__ == '__main__':
   drink_responses()
   
if __name__ == '__main__':
   drink_maker()