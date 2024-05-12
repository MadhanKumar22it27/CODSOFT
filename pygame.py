import tkinter as tk
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    def play_round(user_choice):
        nonlocal user_score, computer_score
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        result_label.config(text=result)
        user_choice_label.config(text="Your choice: " + user_choice)
        computer_choice_label.config(text="Computer's choice: " + computer_choice)

        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1

        score_label.config(text="Score - You: {} Computer: {}".format(user_score, computer_score))
        
        if user_score == 3 or computer_score == 3:
            final_result = "Congratulations! You win!" if user_score == 3 else "Computer wins. Better luck next time!"
            result_label.config(text=final_result)
            rematch_button.config(state=tk.NORMAL)
            rock_button.config(state=tk.DISABLED)
            paper_button.config(state=tk.DISABLED)
            scissors_button.config(state=tk.DISABLED)

    def on_choice_click(choice):
        play_round(choice)

    def exit_game():
        root.destroy()

    def rematch():
        nonlocal user_score, computer_score
        user_score = 0
        computer_score = 0
        result_label.config(text="")
        user_choice_label.config(text="")
        computer_choice_label.config(text="")
        score_label.config(text="")
        rematch_button.config(state=tk.DISABLED)
        rock_button.config(state=tk.NORMAL)
        paper_button.config(state=tk.NORMAL)
        scissors_button.config(state=tk.NORMAL)

    root = tk.Tk()
    root.title("Rock Paper Scissors")

    choice_frame = tk.Frame(root)
    choice_frame.pack()

    rock_button = tk.Button(choice_frame, text="Rock", command=lambda: on_choice_click('rock'))
    rock_button.grid(row=0, column=0, padx=5, pady=5)

    paper_button = tk.Button(choice_frame, text="Paper", command=lambda: on_choice_click('paper'))
    paper_button.grid(row=0, column=1, padx=5, pady=5)

    scissors_button = tk.Button(choice_frame, text="Scissors", command=lambda: on_choice_click('scissors'))
    scissors_button.grid(row=0, column=2, padx=5, pady=5)

    result_label = tk.Label(root, text="")
    result_label.pack()

    user_choice_label = tk.Label(root, text="")
    user_choice_label.pack()

    computer_choice_label = tk.Label(root, text="")
    computer_choice_label.pack()

    score_label = tk.Label(root, text="")
    score_label.pack()
    
    rematch_button = tk.Button(root, text="Rematch", command=rematch, state=tk.DISABLED)
    rematch_button.pack()

    exit_button = tk.Button(root, text="Exit", command=exit_game)
    exit_button.pack()

    root.mainloop()

play_game()
