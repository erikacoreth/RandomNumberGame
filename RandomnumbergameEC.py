import random

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def check_guess(random_num, user_guess):
    return random_num == user_guess

def get_hint(random_num):
    hints = []
    hints.append(f'Hint: The number is {'even' if random_num % 2 == 0 else 'odd'}.')
    if random_num % 5 == 0:
        hints.append('Hint: The number is a multiple of 5.')
    if random_num**2 > 100:
        hints.append('Hint: The number squared is greater than 1000')
    else:
        hints.append('Hint: The number squared is less than 100')
    return random.choice(hints)

def main():
    print('Welcome to the Guess the Number Game!')
    print('I have selected a random number between 1 and 100, try to guess it!')

    random_num = generate_random_number(1, 100)
    attempts = 0
    hint_counter = 0

    while True:
        user_guess = int(input('Enter your guess:'))
        attempts += 1

        if check_guess(random_num, user_guess):
            print(f'Correct! You guessed the number in {attempts} attempts.')
            break
        else:
            hint_counter += 1
            if user_guess < random_num:
                print('Incorrect! Try a higher number.')
            else:
                print('incorrect! Try a lower number.')

            if hint_counter == 2:
                print(get_hint(random_num))
                hint_counter = 0
if __name__ == '__main__':
    main()
