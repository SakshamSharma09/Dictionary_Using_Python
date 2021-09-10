import json
from difflib import get_close_matches as gcm

def diction(dic_word):
    
    if(dic_word in file):
        return file[dic_word]
    
    elif(dic_word.title() in file):
        return file[dic_word.title()]
    
    elif(dic_word.upper() in file):
        return file[dic_word.upper()]
    
    elif len(gcm(dic_word , file.keys()))>0:
        print("Did you mean %s instead" %gcm(dic_word,file.keys())[0])
        decide = input("Y for yes and N for no")
        
        if decide.lower() == 'y':
            return file[gcm(dic_word,file.keys())[0]]
        
        elif decide.lower() == 'n':
            return ("Word Not Found!")
        
        else:
            return("Wrong input Enter Again")
        
    else:
        return ("Word Not Found!")


word = input("Enter the word to find the meaning")
dic_word = word.lower()

file = json.load(open("data_dict.json"))

app_match  = gcm(dic_word , file.keys())

result = diction(dic_word)

if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)
