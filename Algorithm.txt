Algorithm
1. Import random number generator function

2. Generate a Random Number:
-Use the generate_random_number(min_num, max_num) function to generate and store a random number between 1 and 100.

3.Define check guess function

4.Define the get hint function
-add all hints that will be given once the user makes 2 incorrect guesses

5. Initialize the Game:
-Print a welcome message.
-Set the range for the random number (1 to 100).
-Initialize the guess attempt counter and hint_counter, set both to zero.

6. Check the Guess:
-Use check_guess(random_num, user_guess) to verify if the guess is correct.
-If correct:
 -Print a success message with the number of attempts taken.
 -Break the loop.
-If incorrect:
-Start hint counter
 -Provide feedback on whether the guess should be higher or lower.
 -Every two incorrect attempts, provide an additional hint:
  -Select a random hint from a list (even/odd, multiple of 5, or if the square of the number is greater than or less than 1000).

5. Repeat:
-Continue to prompt the user to enter guesses until the correct number is guessed.
