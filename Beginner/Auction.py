print('''
▀█▀ █░█ █▀▀   █▀█ █▀█ █ █░█ ▄▀█ ▀█▀ █▀▀   █▄▄ █ █▀▄ █▀▄ █ █▄░█ █▀▀   ▄▀█ █░█ █▀▀ ▀█▀ █ █▀█ █▄░█
░█░ █▀█ ██▄   █▀▀ █▀▄ █ ▀▄▀ █▀█ ░█░ ██▄   █▄█ █ █▄▀ █▄▀ █ █░▀█ █▄█   █▀█ █▄█ █▄▄ ░█░ █ █▄█ █░▀█
''')
x = {} 

def auction():
    name = input("Enter your name: ")
    bid = int(input("Enter the bid you want place in dollars: "))
    x[name] = bid
    move()

def winner():
    l = []
    for i in x:
        l.append(x[i])
    xim = max(l)
    winner = ""
    for i in x: 
        if x[i] == xim:
            winner += i
    print(f"Winner is {winner}")

def move():
    m = input("More people? Enter Y for Yes and N for No: ")
    if m=="y":
        auction()
    else:
        winner()

auction()
