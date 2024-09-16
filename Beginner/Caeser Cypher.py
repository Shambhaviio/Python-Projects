import string
alphabet = list(string.ascii_lowercase)

print('''
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝        
''')
def caeser():
    todo = input("Enter 'E' for Encode or 'D' for Decode: ")
    whattodo = input("Enter what you want to encode or decode: ")
    shift = int(input("What is the shift value to use: "))

    #Encoding 
    def encrypt(original_text, shift_amount):
        final = ""
        for i in original_text:
            x = alphabet.index(i)
            new = x + shift_amount 
            final = final + alphabet[new]
        
        print(f"Your encoded text is {final}")

    def decrypt(original_text,shift_amount):
        final = ""
        for i in original_text:
            x = alphabet.index(i)
            new = x - shift_amount 
            final = final + alphabet[new]
        print(f"Your decoded text is {final}")

    if todo=="E" or "e":
        encrypt(whattodo,shift)
    elif todo=="D" or "d":
        decrypt(whattodo, shift)
    else:
        print("Invalid input")

caeser()
answer =  input("Y for Yes and N for No: ")
while answer=="y" or "Y":
    caeser()



