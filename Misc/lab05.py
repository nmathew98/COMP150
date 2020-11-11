def compare(x, y):
    if x < y:
        print(x, "is less than", y)
    elif x > y:
        print(x, "is greater than", y)
    else:
        print(x, "and", y, "are equal")        
compare(5, 10);
compare(10, 5)
compare(10, 10)

def guess_right(secret, guess):
    print("You win.", guess, "is equal to", secret) if guess == secret else print("You lose.", guess, "is not equal to", secret)
secret = 55
guess = int(input("Guess a number between 50 and 100: "))
guess_right(secret, guess)

def is_divisible_by_3(x):
    print("This number is divisible by three") if x%3 == 0 else print("This number is not divisible by three.")
def is_divisible_by_5(x):
    print("This number is divisible by three") if x%5 == 0 else print("This number is not divisible by three.")
def is_divisible(x, y):
    print(x, "is divisible by", y) if x%y == 0 else print(x, "is not divisible by", y)
is_divisible(3, 2)
is_divisible(6, 3)

def water_state(temp):
    if temp > 100:
        print("Steam")
    elif temp < 0:
        print("Ice")
    else:
        print("Liquid")
        
def yes_or_no():
    yos = input("Is a dog a fish? ").lower()
    print("You chose Yes") if yos[0] == "y" else print("You chose No")
yes_or_no()

def any_equal(x, y, z):
    print("At least two inputs are the same.") if (x == y) or (x == z) or (y == z) else print("No inputs match.")
any_equal(1, 2, 3)
any_equal(1, 2, 1)
any_equal(1, 1, 3)
any_equal("ant", "ant", 3)
any_equal("ant", "ant", "ant")

def next_level(a, b, c, d, e, f):
    lowestScore = min(a, b, c, d, e, f)
    totalScore = (a+b+c+d+e+f) - lowestScore
    print("Pass") if totalScore >= 200 else print("Repeat")
next_level(10, 10, 50, 20, 20, 50)
next_level(100, 100, 50, 80, 70, 50)

def inOrder(x, y, z):
    list = [x, y, z]
    list.sort()
    print("In order: ", list)
    return list
inOrder(5, 6, 4)

def find_middle(x, y, z):
    sortedList = inOrder(x, y, z)
    print("The middle value is ", sortedList[1])
find_middle(5, 6, 4)