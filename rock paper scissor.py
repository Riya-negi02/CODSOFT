import tkinter
import random
user_count=0      #score count set to zero
computer_count=0

def game(user_choice):
    option= ['rock','paper','scissors']
    
    Computer_choice = random.choice(option)      #randomly choosing from options
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"computer choice: {Computer_choice}")

    global user_count, computer_count   #count variables declared globally

    if user_choice== Computer_choice:
        winner= 'no winner'
        result_label.config(text="It's a tie!")
    elif (user_choice== 'rock' and Computer_choice== 'scissors')or (user_choice== 'paper' and Computer_choice== 'rock')or (user_choice== 'scissors' and Computer_choice== 'paper'):
        winner= 'user'
        user_count+=1
        result_label.config(text="you win this round")
    elif (Computer_choice== 'rock' and user_choice== 'scissors')or (Computer_choice== 'paper' and user_choice== 'rock')or (Computer_choice== 'scissors' and user_choice == 'paper'):
        winner= 'computer'
        computer_count+=1
        result_label.config(text="Computer win this round")

    score_label.config(text=f"Score: USER= {user_count}  || COMPUTER= {computer_count}")

#GUI setup
window= tkinter.Tk()
window.title("Game")
window.geometry('500x500')
window.config(bg='lightgrey')

label_title= tkinter.Label(window, text= "ROCK PAPER SCISSOR GAME", font=('Microdoft Himalaya',18,'bold'), bg='Lavender', fg= 'blue').pack(pady=10)
label_user_input= tkinter.Label(window,text="Make a choice",font=('Microsoft Himalaya',18,'bold'),bg='lightgrey').pack(pady=20)

#button frame
button_frame= tkinter.Frame(window, bg= 'lightgrey')
button_frame.pack(pady=10)

#rock button
rock_button= tkinter.Button (button_frame, text="ROCK", width=10, height= 5, command= lambda: game("rock"),font=('Arial', 12, 'bold'), bg='lightblue')
rock_button.grid(row=0, column=0, padx=10)

#paper button
paper_button= tkinter.Button(button_frame, text="PAPER", width=10, height= 5, command= lambda: game("paper"),font=('Arial', 12, 'bold'), bg='lightblue')
paper_button.grid(row=0, column=1, padx=10)

#scissors button
scissor_button= tkinter.Button(button_frame, text="SCISSORS", width=10, height= 5, command= lambda: game("scissors"),font=('Arial', 12, 'bold'), bg='lightblue')
scissor_button.grid(row=0, column=2, padx=10)

#display of user's choice
user_choice_label= tkinter.Label(window, text="Your Choice:",font=('Microsoft Himalaya',18,'bold'), bg='lightgrey')
user_choice_label.pack(pady=10)

#display of computer's choice
computer_choice_label= tkinter.Label(window, text="Computer Choice:",font=('Microsoft Himalaya',18,'bold'), bg='lightgrey')
computer_choice_label.pack(pady=10)

#result display
result_label= tkinter.Label(window, text="Result:",font=('Microsoft Himalaya',18,'bold'), bg='lightgrey')
result_label.pack(pady=10)\

#score count display
score_label= tkinter.Label(window,text=f"Score: User={user_count}| Computer={computer_count}",font=('Microsoft Himalaya',18,'bold'), bg='lightgrey')
score_label.pack(pady=10)

window.mainloop()

    

