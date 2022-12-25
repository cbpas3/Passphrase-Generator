# Import file reader and randomizer
import random

def main(choices):

    file = open("Input.txt", "r")
    phrases = file.read().splitlines()
    
    for phrase in phrases:
        newPhrase = phrase[:]
        for index, letter in enumerate(phrase):
            magicNumber = random.random()
            if magicNumber >= 0.85:
                try:
                    replacements = choices[letter.lower()]
                    replacement = random.choice(replacements)
                    newPhrase = replaceInString(index,newPhrase,replacement)
                except:
                    pass
            elif magicNumber >= 0.7:
                newPhrase = replaceInString(index,newPhrase,letter.swapcase())
            else:
                pass
        print(newPhrase)
        
def replaceInString(index,oldString,replacementCharacter):
    stringList = list(oldString)
    stringList[index] = replacementCharacter
    newStr = ''.join(stringList)
    return newStr

            
choices = {
    'a':['@','4','^'],
    'b':['6','8'],
    'c':['<','(','{','['],
    'd':['<','(','7'],
    'e':['3','6'],
    'f':['#'],
    'g':['9','&'],
    'h':['#'],
    'i':['|','/',':','l'],
    'j':[';'],
    'k':['<'],
    'l':['|','/','I'],
    'm':['3'],
    'n':['^'],
    'o':['0'],
    'p':['?'],
    'q':['9'],
    'r':['n'],
    's':['z','Z','$'],
    't':['+'],
    'u':['w','W'],
    'v':['<','>','^'],
    'w':['}','{','3'],
    'x':['+','t'],
    'y':['V','v'],
    'z':['s','S','2'],
    '1':['|','l',"I"],
    '2':['z','Z'],
    '3':['w','W'],
    '4':['A','<'],
    '5':['s','S','$'],
    '6':['G',],
    '7':['>'],
    '8':['B'],
    '9':['g','q']
}
    
main(choices)