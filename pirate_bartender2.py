questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
} 


def drink_responses(): 
    
    responses = {            #creating a brand new dictionary and assigning it the name 'responses'
    }
    
    for flavor in questions: #create a brand new variable in the same line to loop through a dictionary 
        my_input8 = raw_input(questions[flavor]) # How to call a value, calling variable flavor
        responses[flavor] = my_input8 #watch out for order of variables when declaring 
    
    return responses #use return to output something from the function
    
   
def drink_maker(responses):
    import random
    my_drink = []
    for the_drink in ingredients:
        if (responses[the_drink]) == "Yes":
            #print(the_drink)
            my_drink.append(random.choice(ingredients[the_drink]))
    print(my_drink)
    
   # if responses['strong'] == "Yes":
       # my_drink.append(random.choice(ingredients[the_drink])
       # print my_drink
       
if __name__ == '__main__':
   new_drink = drink_responses()  #now new drink is the result of the function, MUST use this line/create a variable to capture the output of the first function
   drink_maker(new_drink)
   