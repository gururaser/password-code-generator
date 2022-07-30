import random
from string import ascii_letters


class Generator:
    letters = []

    for letter in ascii_letters:
        letters.append(letter)

    nums = []

    for num in range(0, 10):
        nums.append(f"{num}")
        num += 1

    symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
               '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

    final_code = []


    def __init__(self, long, level):
        self.long = long
        self.level = level



    def create_code(self):
        # We made a certain number (the value with given self.long) of random selections
        chosen_letters = random.sample(Generator.letters, self.long)
        chosen_nums = random.sample(Generator.nums, self.long)
        chosen_symbols = random.sample(Generator.symbols, self.long)

        if self.level == "Basic":

            result = "".join(chosen_letters)
            Generator.final_code.append(result)
            return result
        elif self.level == "Medium":
            # we combined the two lists into one list and chose values randomly

            result = "".join(random.sample(chosen_letters + chosen_nums, self.long))

            return result
        elif self.level == "Expert":

            result = "".join(random.sample(chosen_letters + chosen_nums + chosen_symbols, self.long))

            return result
while True:
    try:
        print("Welcome to password/code generator".upper())
        print("-" * 34)
        print("Choose your level and how long password you want")
        length = int(input("Enter length of password you want: "))
        print("-" * 34)
        print(
            """1 - Basic\n"""
            """2 - Medium\n"""
            """3 - Expert\n"""
            """4 - Exit"""
        )
        print("-" * 34)
        option = int(input("Enter your choice: "))
        if option == 1:
            password = Generator(long=length,level="Basic")
            print(f"Result: {password.create_code()}")
            last_message = input("Enter 'c' to continue\n")
        elif option == 2:
            password2 = Generator(long=length,level="Medium")
            print(f"Result: {password2.create_code()}")
            last_message = input("Enter 'c' to continue\n")
        if option == 3:
            password3 = Generator(long=length,level="Expert")
            print(f"Result: {password3.create_code()}")
            print("-" * 34)
            last_message = input("Enter 'c' to continue\n")
        elif option == 4:
            break
    except ValueError:
        print("Please enter integer value")
