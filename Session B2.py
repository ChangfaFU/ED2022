from functools import partial  
import numpy as np
import pandas as pd
from PIL import ImageTk, Image
import random
import sys
import time
import tkinter as tk

class App0(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Experiment')
        self.geometry('1000x600')

        self.label = tk.Label(self, text="""Hello, my dear friend.\n
You have passed our selection phase and welcome to the survival competition.\n 
You now will participate in three 50-day survival competition. \n
You are assigned to a team of 5 competing with other teams.\n
You will be asked to make same decisions as in the trial.\n\n
Your GOAL:\n
� To Survive (Final Balance Above 0)\n
� To Maximise Your Reward\n
� To Maximise Your Group Reward\n\n
The decisions being made will affect either yourself or other group members, the decision types are randomly mixed up.\n""")
        self.label.pack()

        self.button = tk.Button(self, text='Start!')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        def retrieve(IMAGE_NAME):
            return
        
        def accept(IMAGE_NAME):
            scenario = IMAGE_NAME
            decision = 'accept'
            global dict
            loss = dict['Loss'][b] 
            gain = dict['Gain'][b]
            choice = [loss,gain]
            reward =  random.choice(choice)
            tme = int(time.time())
            new_row1 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'time':tme}
            global df_B2
            df_B2 = df_B2.append(new_row1, ignore_index=True)
            return

        def reject(IMAGE_NAME):
            scenario = IMAGE_NAME
            decision = 'reject'
            reward = 0 
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'time':tme}
            global df_B2
            df_B2 = df_B2.append(new_row2, ignore_index=True)
            return

        def change_value():
            global buttonClicked
            if buttonClicked:
                buttonClicked=False
            if not buttonClicked:
                buttonClicked=True      

        epoch = int(time.time())
        L_I = ['36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85']

        c = 1

        for c in range(1,len(L_I)+1):
            x = random.choice(L_I)
            IMAGE_NAME = "Slide"+x+".JPG"
            b = int(x)-1
            window = tk.Toplevel()
            top=window
            window.title("Day"+str(c))
            window.geometry("800x600")
            window.configure(background='grey')
            frame = tk.Frame(window)
            frame.pack()
            path = IMAGE_NAME
            img = ImageTk.PhotoImage(Image.open(path))
            panel = tk.Label(window, image = img)
            panel.pack(side = "bottom", fill = "both", expand = "yes")

            accept_button = tk.Button(frame, text="Accept", command=lambda:[accept(IMAGE_NAME)])
            reject_button = tk.Button(frame, text="Reject", command=lambda:[reject(IMAGE_NAME)])
            next_button = tk.Button(frame, text="NEXT", command=top.destroy)

            accept_button.pack(side=tk.LEFT)
            reject_button.pack(side=tk.RIGHT)
            next_button.pack(side=tk.RIGHT)

            last_row = len(df_B2)
            second_last_row = last_row - 1
  

            window.mainloop()

            L_I.remove(x)
            c = c + 1
            df_B2.to_csv("Experiment Result B2")


df_B2 = pd.DataFrame()
df1 = pd.read_csv('Graph.csv')
dict = df1.to_dict()
buttonClicked = False

if __name__ == "__main__":
    app = App0()
    app.mainloop()

