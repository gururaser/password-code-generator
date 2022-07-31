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

    def __init__(self, long, level):
        self.long = long
        self.level = level

    def create_code(self):
        if self.level == "Basic":

            random.shuffle(Generator.letters)

            chosen_letter = random.sample(Generator.letters, self.long)

            result = "".join(chosen_letter)
            return result

        elif self.level == "Medium":

            while True:
                try:
                    # number of character types
                    letters_count = int(input("Enter letters count in password: "))
                    numbers_count = int(input("Enter numbers count in password: "))
                    total_count = letters_count + numbers_count

                    # check the total length with characters sum count
                    # print not valid if the sum is greater than length
                    if total_count > self.long:
                        print("Characters total count is greater than the password length")

                    code = []
                    #  We are picking random letters
                    for i in range(letters_count):
                        code.append(random.choice(Generator.letters))
                    #  We are picking random numbers
                    for i in range(numbers_count):
                        code.append(random.choice(Generator.nums))

                    # if total count is less than the code length
                    # we are adding some random characters from symbols
                    # if you wish, you can change it.

                    if total_count < self.long:
                        random.shuffle(Generator.letters)
                        for i in range(self.long - total_count):
                            code.append(random.choice(Generator.letters))

                    # # if you want user to re-enter total count again instead of
                    # # adding some random numbers. You can use the code below
                    #
                    # if total_count < self.long:
                    #     print(f"You've entered {total_count} characters count\nbut you must enter {self.long}. Please try again.")
                    #     continue

                    random.shuffle(code)

                    return "".join(code)

                except ValueError:
                    print("Please enter integer number.")

        elif self.level == "Expert":
            while True:
                try:
                    # number of character types
                    letters_count = int(input("Enter letters count in password: "))
                    numbers_count = int(input("Enter numbers count in password: "))
                    symbols_count = int(input("Enter symbols count in password: "))
                    total_count = letters_count + numbers_count + symbols_count

                    # check the total length with characters sum count
                    # print not valid if the sum is greater than length
                    if total_count > self.long:
                        print("Characters total count is greater than the password length")
                        continue

                    code = []
                    #  We are picking random letters
                    for i in range(letters_count):
                        code.append(random.choice(Generator.letters))
                    #  We are picking random numbers
                    for i in range(numbers_count):
                        code.append(random.choice(Generator.nums))
                    # We are picking random symbols
                    for i in range(symbols_count):
                        code.append(random.choice(Generator.symbols))

                    # if total count is less than the code length
                    # we are adding some random characters from symbols
                    # if you wish, you can change it.

                    if total_count < self.long:
                        random.shuffle(Generator.symbols)
                        for i in range(self.long - total_count):
                            code.append(random.choice(Generator.symbols))

                    # # if you want user to re-enter total count again instead of
                    # # adding some random numbers. You can use the code below
                    #
                    # if total_count < self.long:
                    #     print(f"You've entered {total_count} characters count\nbut you must enter {self.long}. Please try again.")
                    #     continue


                    random.shuffle(code)

                    return "".join(code)

                except ValueError:
                    print("Please enter integer number.")


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
        option = int(input("Enter your choice: ".capitalize()))
        if option == 1:
            password = Generator(long=length, level="Basic")
            print(f"Result: {password.create_code()}")
            last_message = input("Press Enter to continue\n")
        elif option == 2:
            password2 = Generator(long=length, level="Medium")
            print(f"Result: {password2.create_code()}")
            last_message = input("Press Enter to continue\n")
        if option == 3:
            password3 = Generator(long=length, level="Expert")
            print(f"Result: {password3.create_code()}")
            print("-" * 34)
            last_message = input("Press Enter to continue\n")
        elif option == 4:
            break
    except ValueError:
        print("Please enter integer value")
