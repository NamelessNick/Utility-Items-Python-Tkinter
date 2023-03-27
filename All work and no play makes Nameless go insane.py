import random, pyperclip, sys, time
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox

screen= ThemedTk(theme="equilux")
screen.configure(themebg="equilux")
screen.geometry("510x250")

#Definitions
def Starting_menu(event=0):
    for widget in screen.winfo_children():
        widget.destroy()
    cal_menu_bt = ttk.Button(text="Calculator",command=Cal_menu)
    cal_menu_bt.place(x=210,y=100,height=50,width=110)
    sp_test_menu_bt = ttk.Button(text="Speed test",command=Speed_test)
    sp_test_menu_bt.place(x=210 , y=50,height=50,width=110)
    #check_interest = ttk.Button(text="Check Interest" , command=Check_interest_Screen)
    #check_interest.place(x=85 , y=160 , height=50 , width=110)
    #stock_exchange = ttk.Button(text="Stock exchange" , command=Stock_exchange_Screen)
    #stock_exchange.place(x=85 , y=230 , height=50 , width=110)
    #leave = ttk.Button(text="Exit",command=Exit)
    #leave.place(x=85, y=300,height=50,width=110)
def Cal_menu(event=0):
    for widget in screen.winfo_children():
        widget.destroy()
    UI = ttk.Entry(screen,width=30,font=('Times' , 15))
    UI.grid(column=0,row=0,columnspan=7)

    #Defs
    def Clear(event=0):
        UI.delete('0' , END)
    def press(num):
        num = str(num)
        UI.insert(INSERT,num)
    def Evaluate(event=0):
        try:
            fraction = UI.get()
            result = str(eval(fraction))
            UI.delete('0' , END)
            UI.insert(INSERT , result)
        except:
            UI.delete('0' , END)
            UI.insert(INSERT , "error")

    def end2(event=0):
        UI.delete(END,"1")
        UI.delete(len(UI.get())-1, END)

    def  Add_commas(event=0):
        try:
            fraction = UI.get()
            fraction = "{:,}".format(int(fraction))
            UI.delete('0' , END)
            UI.insert(INSERT , fraction)
        except:
            print()

    #Buttons
    button_1 = ttk.Button(text="1",command=lambda: press("1"))
    button_1.grid(column=1,row=1)
    button_2 = ttk.Button(text="2",command=lambda: press("2"))
    button_2.grid(column=2,row=1)
    button_3 = ttk.Button(text="3",command=lambda: press("3"))
    button_3.grid(column=3,row=1)
    button_4 = ttk.Button(text="4",command=lambda: press("4"))
    button_4.grid(column=1,row=2)
    button_5 = ttk.Button(text="5",command=lambda: press("5"))
    button_5.grid(column=2,row=2)
    button_6 = ttk.Button(text="6",command=lambda: press("6"))
    button_6.grid(column=3,row=2)
    button_7 = ttk.Button(text="7",command=lambda: press("7"))
    button_7.grid(column=1,row=3)
    button_8 = ttk.Button(text="8",command=lambda: press("8"))
    button_8.grid(column=2,row=3)
    button_9 = ttk.Button(text="9",command=lambda: press("9"))
    button_9.grid(column=3,row=3)
    button_0 = ttk.Button(text="0",command=lambda: press("0"))
    button_0.grid(column=2,row=4)
    button_dot = ttk.Button(text=".",command=lambda: press("."))
    button_dot.grid(column=3,row=5)

    button_add = ttk.Button(text="+",command=lambda: press("+"))
    button_add.grid(column=2,row=5)

    button_subtract = ttk.Button(text="-",command=lambda: press("-"))
    button_subtract.grid(column=1,row=5)

    button_multiply= ttk.Button(text="*",command=lambda: press("*"))
    button_multiply.grid(column=4,row=4)

    button_divide= ttk.Button(text="/",command=lambda: press("/"))
    button_divide.grid(column=4,row=5)

    button_in_power= ttk.Button(text="Power of",command=lambda: press("**"))
    button_in_power.grid(column=1,row=4)

    button_root= ttk.Button(text="Square root",command=lambda: press("sqrt("))
    button_root.grid(column=3,row=4)

    button_equals= ttk.Button(text="Equals",command= Evaluate)
    button_equals.grid(column=4,row=1)

    button_close_parenthesis= ttk.Button(text=")",command=lambda: press(")"))
    button_close_parenthesis.grid(column=2,row=6)

    button_open_parenthesis= ttk.Button(text="(",command=lambda: press("("))
    button_open_parenthesis.grid(column=1,row=6)

    button_clear = ttk.Button(text="Clear",command = Clear)
    button_clear.grid(column=4,row=2)

    button_add_commas = ttk.Button(text="Comma",command = Add_commas)
    button_add_commas.grid(column=4,row=3)

    button_add_commas = ttk.Button(text="Back",command = Starting_menu)
    button_add_commas.grid(column=3,row=6)

    screen.title("Calculator")
def Speed_test(event=0):
    for widget in screen.winfo_children():
        widget.destroy()
    # varibles and lists
    words = ["nice" , "fascism" , "liberty" , "aquatic" , "aquatance" , "capital" , "washington" , "moscow" , "resort" ,
             "illness" , "shrimp" ,
             "odd" , "speed" , "advert" , "avert" , "aviation" , "athens" , "stress" , "terraria" , "gaia" ,
             "blackberry" , "pain" , "agony" , "thorns" ,
             "capitalisim" , "salveholder" , "shareholder" , "exploitation" , "natives" , "oil" , "lifegiver"]
    score = 0
    time_left = 60
    attempts = 0
    cr_attempts = 0
    letter_number = 0

    def game_start(event=0):
        if time_left == 60:
            timer()
            new_word()
            str_button.place(x=2200000 , y=2100000)
            text_box.config(state=NORMAL)

    def new_word():
        global word_choice , words
        word_choice = (random.choice(words))
        words.remove(word_choice)
        if len(words) == 0:
            words = ["nice" , "fascism" , "liberty" , "aquatic" , "aquatance" , "capital" , "washington" , "moscow" ,
                     "resort" , "illness" , "shrimp" ,
                     "odd" , "speed" , "advert" , "avert" , "aviation" , "athens" , "stress" , "terraria" , "gaia" ,
                     "blackberry" , "pain" , "agony" , "thorns"]
        # if random.randint(1,0) == 1: game_text.configure(text=word_choice)
        # else: game_text.configure(text=(random.choice(sentences)))
        game_text.configure(text=word_choice , font=("Calibri" , 40))

    def check_answer(event):
        global word_choice , score , attempts , cr_attempts , letter_number
        answer = text_box.get()
        answer = answer.lower()
        attempts += 1
        if answer == word_choice:
            score += 1
            cr_attempts += 1
            text_box.delete('0' , END)
            score_lbl.configure(text="Your score is: " + str(score))
            letter_number += len(answer)
            new_word()
        elif answer != "":
            text_box.delete('0' , END)
            new_word()

    def timer():
        global time_left , score , attempts , cr_attempts , letter_number
        if time_left > 0:
            time_left -= 1
            timer_lbl.configure(text="Time left: " + str(time_left))
            timer_lbl.after(1000 , timer)
        elif time_left == 0:
            score = 0
            text_box.delete('0' , END)
            time_left = 60
            text_box.config(state=DISABLED)
            str_button.place(x=220 , y=210)
            letter_number_per_second = letter_number
            score_lbl.configure(text="Your score is " + str(cr_attempts) + " / " + str(attempts))
            timer_lbl.configure(text="Time left: " + str(time_left))
            game_text.configure(text=" You got " + str(letter_number_per_second) + " letters per minute",font=("Calibri" , 12))
            attempts = 0
            cr_attempts = 0
            letter_number = 0
            text_box.delete('0' , END)

    # Labels

    game_text = ttk.Label(screen,text="",font=("Calibri" , 40))
    game_text.place(x=10, y=120)

    starter_text = ttk.Label(screen, text="Type the letters as fast as you can!", font=("Calibri", 12))
    starter_text.place(x=10, y=0)

    starter_text2 = ttk.Label(screen, text="Press 'enter' to confirm.", font=("Calibri", 12))
    starter_text2.place(x=10, y=30)

    score_lbl = ttk.Label(screen, text="Your score is: " + str(score), font=("Calibri", 12))
    score_lbl.place(x=10 , y=60)

    timer_lbl = ttk.Label(screen, text="Time left: " + str(time_left), font=("Calibri", 12))
    timer_lbl.place(x=10 , y=90)

    str_button = ttk.Button(screen, text="Start", command=game_start)
    str_button.place(x=140, y=186)

    text_box = ttk.Entry(screen)
    text_box.place(x=10, y=190)
    text_box.config(state=DISABLED)

    screen.bind("<Return>", check_answer)

    screen.title("Speed typer")





Starting_menu()
screen.title("Utility Closet")
screen.mainloop()