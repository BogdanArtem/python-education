import tkinter as tk
from tkinter import messagebox
from hangman import Hangman

class Application(tk.Frame):            
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  
        self.grid()                      
        self.game = Hangman()
        self.create_widgets()

    def create_widgets(self):
        """Create all widgets and display them."""
        self._add_lives(row=0, column=0)
        self._add_display_hangman(row=1, column=0)
        self._add_text_input(row=2, column=0)
        self._add_button(row=3, column=0)
        self._add_attemps(row=4, column=0)
        
    def click(self):
        """Click initialized by "guess button."""
        # Get user input
        self.user_inp = self.text_input.get().lower()
        self.game.guess(self.user_inp)
        self.main_text.config(text=self.game.get_masked_word())

        self._click_update_attempts()
        self._click_update_lives()
        self._click_if_endgame()

    def _click_update_attempts(self):
        """Update displayed attempts."""
        label_text = self.attempts_var.get()
        label_text += self.user_inp + " "
        self.attempts_var.set(label_text)

    def _click_update_lives(self):
        """Update displayed lives."""
        label_num = self.lives_var.get()
        label_num = f"Lives: {self.game.get_lives()}"
        self.lives_var.set(label_num)

    def _click_if_endgame(self):
        """ Checks if the game has ended """
        if self.game.is_guessed():
            messagebox.showinfo("CONGRATS!", "You nailed it!")
            self.quit()

        elif self.game.is_dead():
            messagebox.showinfo(
                "WASTED!", 
                f"You've run out of lives. The word was {self.game.get_word()}"
                )
            self.quit()

    def _add_lives(self, row, column):
        """Add widget for displaying lives"""
        # Create widget variable for future change
        self.lives_var = tk.StringVar()
        # Get widget variable value and change it
        label_num = self.lives_var.get()
        label_num = f"Lives: {self.game.lives}"
        # Lock widget variable
        self.lives_var.set(label_num)
        self.lives = tk.Label(self, textvariable=self.lives_var)    
        # Display widget variable
        self.lives.grid(row=0, column=0)
          
    def _add_attemps(self, row, column):
        """Add widget for displaying attempts"""
        # Create widget variable for future change
        self.attempts_var = tk.StringVar()
        # Get widget variable value and change it
        label_text = self.attempts_var.get()
        label_text += "Attempts:\n"
        # Lock widget variable
        self.attempts_var.set(label_text)
        self.attempts = tk.Label(self, textvariable=self.attempts_var)
        # Display widget variable
        self.attempts.grid(row=row, column=column)

    def _add_display_hangman(self, row, column):
        """Add widget for displaying words of hangman"""
        self.main_text = tk.Label(self, text=self.game.get_masked_word(), font=("Kumar One", 50))
        self.main_text.grid(row=row, column=column)

    def _add_text_input(self, row, column):
        """Add widget for inputing letters or words"""
        self.text_input = tk.Entry(self, justify='center')
        self.text_input.grid(row=row, column=column)

    def _add_button(self, row, column):
        """Add button to initialize "click" function"""
        self.guess_button = tk.Button(
            self, 
            text='Enter', 
            command=self.click, 
            width=21, 
            highlightcolor='blue'
        )
        self.guess_button.grid(row=row, column=column)
        

app = Application()                      
app.master.title('Hangman')  
app.mainloop()  