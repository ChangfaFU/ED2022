from functools import partial  
import numpy as np
import pandas as pd
from PIL import ImageTk, Image
import random
import sys
import time
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Experiment')
        self.geometry('1000x600')

        self.label = tk.Label(self, text="""Hello, my dear friend.\n
You are participating a 35 survival competition. \n
You are assigned to a team of 5 competing with other teams.\n
You will be asked to make the decision on whether to collect resources (RPs).\n\n
Your GOAL:\n
• To Survive (Final Balance Above 0)\n
• To Maximise Your Reward\n\n
To make decisions, you will be given.\n
• The possible gain and loss.\n
• The probability of gain and loss with a level of uncertainty.\n\n
The performance is judged on personal RPs and aggregated group RPs, and thus rewarded with cash at a conversion rate of 0.1.\n\n""")
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
            global df
            df = df.append(new_row1, ignore_index=True)
            return

        def reject(IMAGE_NAME):
            scenario = IMAGE_NAME
            decision = 'reject'
            reward = 0 
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'time':tme}
            global df
            df = df.append(new_row2, ignore_index=True)
            return

        def change_value():
            global buttonClicked
            if buttonClicked:
                buttonClicked=False
            if not buttonClicked:
                buttonClicked=True      

        epoch = int(time.time())
        L_B = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35']

        c = 1

        for c in range(1,len(L_B)+1):
            x = random.choice(L_B)
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

            last_row = len(df)
            second_last_row = last_row - 1
  

            window.mainloop()

            L_B.remove(x)
            c = c + 1
            df.to_csv("Experiment Result B1")

df = pd.DataFrame()
df1 = pd.read_csv('Graph.csv')
dict = df1.to_dict()
buttonClicked = False

if __name__ == "__main__":
    app = App()
    app.mainloop()
