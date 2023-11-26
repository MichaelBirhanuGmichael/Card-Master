from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_list ={}
current_word = {}

try:
  data_to_learn = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  original_data = pandas.read_csv("data/french_words.csv")
  data_list = original_data.to_dict(orient="records")
else:
  data_list = data_to_learn.to_dict(orient="records")  

# ------- generate new random french word --------
def generate_french_word():
  global current_word,flip_timer
  window.after_cancel(flip_timer)
  current_word = random.choice(data_list)
  canvas.itemconfig(title,text = "French",fill = "black")
  canvas.itemconfig(word , text = current_word["French"], fill = "black")
  canvas.itemconfig(card_front_image , image =card_front )
  flip_timer = window.after(3000,flip_card)

  
# ---- remove the words that are known and add the unknown words to words_to_learn.csv file
def remove_data():
  data_list.remove(current_word)
  words_to_learn = pandas.DataFrame(data_list)
  words_to_learn.to_csv("data/words_to_learn.csv",index=False) 
  generate_french_word()
   
# ---- flip the card ----
def flip_card():
  
  canvas.itemconfig(title , text ="English",fill = "white")
  canvas.itemconfig(word , text = current_word["English"],fill ="white")
  canvas.itemconfig(card_front_image , image =card_back )



window  = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50 , pady=50)
flip_timer =window.after(3000,flip_card)
  
# --- images ---
card_front = PhotoImage(file="images/card_front.png")
wrongImage = PhotoImage(file="images/wrong.png")
rightImage = PhotoImage(file ="images/right.png")
card_back = PhotoImage(file="images/card_back.png")

# ---- Flash card ---
canvas  = Canvas(height=526 , width=800 ,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_image =canvas.create_image(400,263,image = card_front)
title=canvas.create_text(400,150 , text="" ,font=("Arial",40,"italic"))
word  = canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(row=0 ,column= 0 ,columnspan= 2)

# --- Buttons ----
wrongButton = Button(image=wrongImage,highlightthickness=0,command=generate_french_word)
wrongButton.grid(row=1 ,column=0)
rightButton = Button(image=rightImage,highlightthickness=0,command=remove_data)
rightButton.grid(row = 1 , column=1)


generate_french_word()

window.mainloop()