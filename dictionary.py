alphToMorse = {
    'a': '.-', 'A': '.-',
    'b': '-...', 'B': '-...',
    'c': '-.-.', 'C': '-.-.',
    'd': '-..', 'D': '-..',
    'e': '.', 'E': '.',
    'f': '..-.', 'F': '..-.',
    'g': '--.', 'G': '--.',
    'h': '....', 'H': '....',
    'i': '..', 'I': '..',
    'j': '.---', 'J': '.---',
    'k': '-.-', 'K': '-.-',
    'l': '.-..', 'L': '.-..',
    'm': '--', 'M': '--',
    'n': '-.', 'N': '-.',
    'o': '---', 'O': '---',
    'p': '.--.', 'P': '.--.',
    'q': '--.-', 'Q': '--.-',
    'r': '.-.', 'R': '.-.',
    's': '...', 'S': '...',
    't': '-', 'T': '-',
    'u': '..-', 'U': '..-',
    'v': '...-', 'V': '...-',
    'w': '.--', 'W': '.--',
    'x': '-..-', 'X': '-..-',
    'y': '-.--', 'Y': '-.--',
    'z': '--..', 'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '!': '-.-.--',
    '?': '..--..',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': ''
}

morseToAlph = { #NOTE: not the final version,
    'A': '.-',  # need to swap the keys and values
    'B': '-...', #rather than hardcoding them again
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '!': '-.-.--',
    '?': '..--..',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': ' '
}

morseToAlphabet = {v:k for k,v in morseToAlph.items()} #final version of the dictionary

def translateToMorse(inputString):
    returnString = ''
    for character in inputString:
        returnString += alphToMorse[character] + ' '
    return returnString


def translateFromMorse(inputString):
    inputString = inputString.strip()
    inputString += ' ' #We have to add a space to the end of the string because they are triggers
                        #for decrypting
    returnString = ''
    characterCode = ''
    for character in inputString:
        if (character != ' '):
            i = 0
            characterCode += character
        else:
            i += 1
            if i == 2:
                returnString += ' '
            else:
                returnString += morseToAlphabet[characterCode]
                characterCode = ''
    return returnString