# Morse Code Dictionary
morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
            'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
            '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
            '8': '---..', '9': '----.', '0': '-----', ' ': '/'}

# Definitions
def translate(user_input):
    user_input = user_input.upper()
    morse_code = []
    
    for char in user_input:
        morse_code.append(morse_dict.get(char, '?'))
    return ' '.join(morse_code)

# Translation
while True:
    user_input = input("Enter text to translate to Morse code: ")
    if not user_input.strip():
        print("Please enter a valid text.")
        continue

    translated = translate(user_input)
    print(f"Morse code: {translated}")

    continue_choice = input('Would you like to continue? (Yes/No): ')
    if continue_choice.lower() not in ['yes', 'y']:
        print('Goodbye!')
        break