secret_word = "Hello"
guess = ""
count = 0
limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if count < limit:
        guess = input("Enter guess: ")
        count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("You lost")
else:
    print("You win!")