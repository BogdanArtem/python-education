import tkinter as tk
from tkinter import messagebox
from hangman import Hangman

root = tk.Tk()
new_game = Hangman(5)


def click():
    user_inp = main_input.get().lower()
    print(user_inp)
    new_game.guess(user_inp)
    print(new_game.get_masked_word())
    main_text.config(text=new_game.get_masked_word())

    # Add text to "display" label
    label_text = attempts_var.get()
    label_text += user_inp + " "
    attempts_var.set(label_text)

    # Change lives count
    label_num = lives_var.get()
    label_num = f"Lives: {new_game.lives}"
    lives_var.set(label_num)

    if new_game.is_guessed():
        messagebox.showinfo("CONGRATS!", "You nailed it!")
        root.quit()

    elif new_game.is_dead():
        messagebox.showinfo(
            "WASTED!", 
            f"You've run out of lives. The word was {new_game.get_word()}"
            )
        root.quit()
    

main_text = tk.Label(root, text=new_game.get_masked_word(), font=("Kumar One", 50))
tried = tk.Label(root, text="Attempted:")
main_input = tk.Entry(root, justify='center')
guess_button = tk.Button(root, text='Enter', command=click, width=21, highlightcolor='blue')

# Show lives
lives_var = tk.StringVar()
label_num = lives_var.get()
label_num = f"Lives: {new_game.lives}"
lives_var.set(label_num)
lives = tk.Label(root, textvariable=lives_var)


# Show attempts
attempts_var = tk.StringVar()
label_text = attempts_var.get()
label_text += "Attempts:\n"
attempts_var.set(label_text)
attempts = tk.Label(root, textvariable=attempts_var)


main_text.grid(row=1, column=0)
main_input.grid(row=2, column=0)
guess_button.grid(row=3, column=0)

attempts.grid(row=4, column=0)
lives.grid(row=0, column=0)

root.mainloop()