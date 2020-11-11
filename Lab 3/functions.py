def new_line():
    print()
def three_lines():
    for i in range(0, 3):
        new_line()
def nine_lines():
    for i in range(0, 3):
        three_lines()

def clear_screen():
    for i in range(0, 40):
        new_line()
        
nine_lines()