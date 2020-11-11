def function_a():
    print("function_a was called")
def function_b():
    print("function_b was called")
def function_c():
    print("function_c was called")

def dispatch(choice):
    function_a() if choice == 'a' else (function_b() if choice == 'b' else (function_c() if choice == 'c' else print("Invalid choice")))
choice = input("Which function to call? ")
dispatch(choice.lower())