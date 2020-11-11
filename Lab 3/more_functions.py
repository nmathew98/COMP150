def powers(n):
    print("The first 5 powers of", n, "are: ", end= "")
    for i in range(0, 5):
        print(pow(n, i), end = " ")
    print("")

def score_summary(name, x, y, z):
    print(name + " - ", "Max: ", max(x, y, z), " , Min: ", min(x, y, z), " , Average: ", (x+y+z)/3)
def signature():
    print("Yours sincerely")
    print("Humphrey Hopalong")
def reject(name):
    print("Dear", name)
    print("I am sorry to inform you that you do not have the job")
    signature()
def accept(name):
    print("Dear", name)
    print("I am sorry to inform you that you have the job")
    signature()

def show_first(input):
    print(min(input))
    
powers(6)
powers(10)
score_summary("Bruce", 9.5, 7, 8.5)
score_summary("Fred", 9, 7, 8)
print()
reject("Bill")
print()
reject("Amanda")
print()
accept("Vicki")
print()
show_first("dog")
show_first("xylophone")
show_first("elephant")
show_first("Elephant")