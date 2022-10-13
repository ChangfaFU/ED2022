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
         
class App1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Experiment')
        self.geometry('1000x600')

        self.label = tk.Label(self, text="""Continue to compete with other teams!!!\n
Now you has been allocated an INTIAL RESOURCES POINT of:\n\n
100 \n\n
Please keep your goals in mind:\n
� To Survive (Final Balance Above 0)\n
� To Maximise Your Reward\n
� To Maximise Your Group Reward (To Be Number 1!!!)\n\n
The performance is judged on personal RPs and aggregated group RPs, and thus rewarded with cash at a conversion rate of 0.1, randomly chosen one outcome from three trials.\n
REWARD: Additional 50 points for the team with the highest aggregated team RPs.\n
PENALTY: For each team member marked as �failed to survive� (Net Balance Below 0), -10 points punishment will be given to the aggregated team RPs.\n\n
""")
        self.label.pack()

        self.button = tk.Button(self, text='Start!')
        self.button['command'] = self.button_clicked
        self.button.pack()
    def button_clicked(self):
        def retrieve(IMAGE_NAME):
            return
        
        def accept(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'accept'
            global dict
            loss = dict['Loss'][b] 
            gain = dict['Gain'][b]
            choice = [loss,gain]
            reward =  random.choice(choice)
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row1 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G1
            df_G1 = df_G1.append(new_row1, ignore_index=True)
            return net_balance

        def reject(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'reject'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G1
            df_G1 = df_G1.append(new_row2, ignore_index=True)
            return

        def change_value():
            global buttonClicked
            if buttonClicked:
                buttonClicked=False
            if not buttonClicked:
                buttonClicked=True     
        
        def defer(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'defer'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G1
            df_G1 = df_G1.append(new_row2, ignore_index=True)
            return

        def ask(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'ask'
            reward = 100 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G1
            df_G1 = df_G1.append(new_row2, ignore_index=True)
            window = tk.Toplevel()
            top=window
            window.title("Day"+str(c))
            window.geometry("400x300")
            donation = tk.Label(top, text = "Your current balance has been updated to:" + str(net_balance)).place(x = 20,y = 10)
            next_button = tk.Button(top, text="NEXT", command=top.destroy).place(x = 200, y = 80) 
            window.mainloop()
            return

        def help(IMAGE_NAME, net_balance):
            def call_result(label_result, n1):
                num1 = (n1.get())  
                result = int(num1)  
                label_result.config(text="You have donated %d to the requester!" % result)
                reward = -result
                NBD = net_balance - result
                scenario = IMAGE_NAME
                decision = 'help'
                tme = int(time.time())
                new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':NBD, 'time':tme}

                global df_G1
                df_G1 = df_G1.append(new_row2, ignore_index=True)

                return

            window = tk.Toplevel()
            top=window
            window.title("Day"+str(c))
            window.geometry("400x300")
            donation = tk.Label(top, text = "Please specify your amount of donation:").place(x = 20,y = 10)
            next_button = tk.Button(top, text="NEXT", command=top.destroy).place(x = 200, y = 80) 

            number1 = tk.StringVar()
            labelNum1 = tk.Label(top, text="Your Donation:").place(x = 20, y = 30) 
            labelResult = tk.Label(top)  
            labelResult.place(x = 20, y = 50) 
            entryNum1 = tk.Entry(top, textvariable=number1).place(x = 120, y = 30) 
            call_result = partial(call_result, labelResult, number1)
            buttonCal = tk.Button(top, text="Confirm", command=call_result).place(x = 20, y = 80) 
           
            window.mainloop()
            return

        def skip(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'refuse'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G1
            df_G1 = df_G1.append(new_row2, ignore_index=True)
            return 

        def skip2(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'no_ask'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G1
            df_G1 = df_G1.append(new_row2, ignore_index=True)
            return

        epoch = int(time.time())
        L_I = ['36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85']
        L_S = ['86','87', '88','89']
        L_G = ['Slide60.JPG','Slide61.JPG','Slide62.JPG','Slide63.JPG','Slide64.JPG','Slide65.JPG','Slide66.JPG','Slide67.JPG','Slide68.JPG','Slide69.JPG','Slide70.JPG','Slide71.JPG','Slide72.JPG','Slide73.JPG','Slide74.JPG','Slide75.JPG','Slide76.JPG','Slide77.JPG','Slide78.JPG','Slide79.JPG','Slide80.JPG','Slide81.JPG','Slide82.JPG','Slide83.JPG','Slide84.JPG','Slide85.JPG',
]
        c = 1
        net_balance = 100
        group_balance = 0
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
            panel = tk.Label(window, image = img, text="NET BALANCE: "+str(net_balance))
            panel.pack(side = "bottom", fill = "both", expand = "yes")
                        
            accept_button = tk.Button(frame, text="Accept", command=lambda:[accept(IMAGE_NAME, net_balance)])
            reject_button = tk.Button(frame, text="Reject", command=lambda:[reject(IMAGE_NAME, net_balance)])
            next_button = tk.Button(frame, text="NEXT", command=top.destroy)
            defer_button = tk.Button(frame, text="Defer", command=lambda:[defer(IMAGE_NAME, net_balance)])

            accept_button.pack(side=tk.LEFT)
            reject_button.pack(side=tk.RIGHT)
            defer_button.pack(side=tk.LEFT)
            next_button.pack(side=tk.RIGHT)

            last_row = len(df_G1)
            second_last_row = last_row - 1

            window.mainloop()

            net_balance = df_G1.loc[last_row,'balance']
            
            if IMAGE_NAME in L_G:
                j = df_G3.iat[last_row, 2]
                group_balance = group_balance + j
            else:
                pass

            if df_G1.loc[last_row,'decision'] == 'defer':
                L_I = L_I
            else:
                L_I.remove(x)

            c = c + 1
            if (c - 1) % 5 == 0:
                window = tk.Toplevel()
                top=window
                window.title("5-Day Update")
                window.geometry("400x300")
                window.configure(background='grey')
                frame = tk.Frame(window)
                frame.pack()
                
                window.label=tk.Label(top, text="YOUR CURRENT NET BALANCE: "+str(net_balance)+"\n YOUR GROUP HAS ACCUMULATED " +str(group_balance)+" RPs")
                window.label.pack()
                next_button = tk.Button(frame, text="NEXT", command=top.destroy)

                next_button.pack(side=tk.RIGHT)
                window.mainloop()

                w = "86"
                IMAGE_NAME = "Slide"+w+".JPG"
                window = tk.Toplevel()
                top=window
                window.title("5-Day Update")
                window.geometry("800x600")
                window.configure(background='grey')
                frame = tk.Frame(window)
                frame.pack()

                path = IMAGE_NAME
                img = ImageTk.PhotoImage(Image.open(path))
                panel = tk.Label(window, image = img)
                panel.pack(side = "bottom", fill = "both", expand = "yes")

                ask_button = tk.Button(frame, text="Ask", command=lambda:[ask(IMAGE_NAME, net_balance)])
                skip_button = tk.Button(frame, text="Skip", command=lambda:[top.destroy,skip2(IMAGE_NAME, net_balance)])
                next_button = tk.Button(frame, text="NEXT", command=top.destroy)

                ask_button.pack(side=tk.LEFT)
                skip_button.pack(side=tk.RIGHT)
                next_button.pack(side=tk.RIGHT)
                window.mainloop()

            if c in [9,18,27,36,45]:
                y = random.choice(["87","89"])
                IMAGE_NAME = "Slide"+y+".JPG"
                if y == "87":
                    requester = "teammate"
                else:
                    requester = "stranger"
                window = tk.Toplevel()
                top=window
                window.title("Request for donation")
                window.geometry("800x600")
                window.configure(background='grey')
                frame = tk.Frame(window)
                frame.pack()

                path = IMAGE_NAME
                img = ImageTk.PhotoImage(Image.open(path))
                panel = tk.Label(window, image = img)
                panel.pack(side = "bottom", fill = "both", expand = "yes")

            
                donate_button = tk.Button(frame, text="Donate", command=lambda:[help(IMAGE_NAME, net_balance)])
                refuse_button = tk.Button(frame, text="Refuse", command=lambda:[top.destroy,skip(IMAGE_NAME, net_balance)])
                next_button = tk.Button(frame, text="NEXT", command=top.destroy)


                donate_button.pack(side=tk.LEFT)
                refuse_button.pack(side=tk.RIGHT)
                next_button.pack(side=tk.RIGHT)
                window.mainloop()

            df_G1.to_csv("Experiment Result1")



class App2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Experiment')
        self.geometry('1000x600')

        self.label = tk.Label(self, text="""Congradulations, my friend!\n
You have entered our second round of the competition.\n\n
YOUR INTIAL RESOURCES POINT:\n\n
200 \n\n
""")
        self.label.pack()

        self.button = tk.Button(self, text='Start!')
        self.button['command'] = self.button_clicked
        self.button.pack()
    def button_clicked(self):
        def retrieve(IMAGE_NAME):
            return
        
        def accept(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'accept'
            global dict
            loss = dict['Loss'][b] 
            gain = dict['Gain'][b]
            choice = [loss,gain]
            reward =  random.choice(choice)
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row1 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G2
            df_G2 = df_G2.append(new_row1, ignore_index=True)
            return net_balance

        def reject(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'reject'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G2
            df_G2 = df_G2.append(new_row2, ignore_index=True)
            return

        def change_value():
            global buttonClicked
            if buttonClicked:
                buttonClicked=False
            if not buttonClicked:
                buttonClicked=True     
        
        def defer(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'defer'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G2
            df_G2 = df_G2.append(new_row2, ignore_index=True)
            return

        def ask(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'ask'
            reward = 100 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G2
            df_G2 = df_G2.append(new_row2, ignore_index=True)
            window = tk.Toplevel()
            top=window
            window.title("Day"+str(c))
            window.geometry("400x300")
            donation = tk.Label(top, text = "Your current balance has been updated to:" + str(net_balance)).place(x = 20,y = 10)
            next_button = tk.Button(top, text="NEXT", command=top.destroy).place(x = 200, y = 80) 
            window.mainloop()
            return

        def help(IMAGE_NAME, net_balance):
            def call_result(label_result, n1):
                num1 = (n1.get())  
                result = int(num1)  
                label_result.config(text="You have donated %d to the requester!" % result)
                reward = -result
                NBD = net_balance - result
                scenario = IMAGE_NAME
                decision = 'help'
                tme = int(time.time())
                new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':NBD, 'time':tme}

                global df_G2
                df_G2 = df_G2.append(new_row2, ignore_index=True)

                return

            window = tk.Toplevel()
            top=window
            window.title("Day"+str(c))
            window.geometry("400x300")
            donation = tk.Label(top, text = "Please specify your amount of donation:").place(x = 20,y = 10)
            next_button = tk.Button(top, text="NEXT", command=top.destroy).place(x = 200, y = 80) 

            number1 = tk.StringVar()
            labelNum1 = tk.Label(top, text="Your Donation:").place(x = 20, y = 30) 
            labelResult = tk.Label(top)  
            labelResult.place(x = 20, y = 50) 
            entryNum1 = tk.Entry(top, textvariable=number1).place(x = 120, y = 30) 
            call_result = partial(call_result, labelResult, number1)
            buttonCal = tk.Button(top, text="Confirm", command=call_result).place(x = 20, y = 80) 
           
            window.mainloop()
            return

        def skip(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'refuse'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G2
            df_G2 = df_G2.append(new_row2, ignore_index=True)
            return 

        def skip2(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'no_ask'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G2
            df_G2 = df_G2.append(new_row2, ignore_index=True)
            return

        epoch = int(time.time())
        L_I = ['36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85']
        L_S = ['86','87', '88','89']
        L_G = ['Slide60.JPG','Slide61.JPG','Slide62.JPG','Slide63.JPG','Slide64.JPG','Slide65.JPG','Slide66.JPG','Slide67.JPG','Slide68.JPG','Slide69.JPG','Slide70.JPG','Slide71.JPG','Slide72.JPG','Slide73.JPG','Slide74.JPG','Slide75.JPG','Slide76.JPG','Slide77.JPG','Slide78.JPG','Slide79.JPG','Slide80.JPG','Slide81.JPG','Slide82.JPG','Slide83.JPG','Slide84.JPG','Slide85.JPG',
]
        c = 1
        net_balance = 200
        group_balance = 0
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
            panel = tk.Label(window, image = img, text="NET BALANCE: "+str(net_balance))
            panel.pack(side = "bottom", fill = "both", expand = "yes")
                        
            accept_button = tk.Button(frame, text="Accept", command=lambda:[accept(IMAGE_NAME, net_balance)])
            reject_button = tk.Button(frame, text="Reject", command=lambda:[reject(IMAGE_NAME, net_balance)])
            next_button = tk.Button(frame, text="NEXT", command=top.destroy)
            defer_button = tk.Button(frame, text="Defer", command=lambda:[defer(IMAGE_NAME, net_balance)])

            accept_button.pack(side=tk.LEFT)
            reject_button.pack(side=tk.RIGHT)
            defer_button.pack(side=tk.LEFT)
            next_button.pack(side=tk.RIGHT)

            last_row = len(df_G2)
            second_last_row = last_row - 1

            window.mainloop()

            net_balance = df_G2.loc[last_row,'balance']
            
            if IMAGE_NAME in L_G:
                j = df_G3.iat[last_row, 2]
                group_balance = group_balance + j
            else:
                pass

            if df_G2.loc[last_row,'decision'] == 'defer':
                L_I = L_I
            else:
                L_I.remove(x)

            c = c + 1
            if (c - 1) % 5 == 0:
                window = tk.Toplevel()
                top=window
                window.title("5-Day Update")
                window.geometry("400x300")
                window.configure(background='grey')
                frame = tk.Frame(window)
                frame.pack()
                
                window.label=tk.Label(top, text="YOUR CURRENT NET BALANCE: "+str(net_balance)+"\n YOUR GROUP HAS ACCUMULATED " +str(group_balance)+" RPs")
                window.label.pack()
                next_button = tk.Button(frame, text="NEXT", command=top.destroy)

                next_button.pack(side=tk.RIGHT)
                window.mainloop()

                w = "86"
                IMAGE_NAME = "Slide"+w+".JPG"
                window = tk.Toplevel()
                top=window
                window.title("5-Day Update")
                window.geometry("800x600")
                window.configure(background='grey')
                frame = tk.Frame(window)
                frame.pack()

                path = IMAGE_NAME
                img = ImageTk.PhotoImage(Image.open(path))
                panel = tk.Label(window, image = img)
                panel.pack(side = "bottom", fill = "both", expand = "yes")

                ask_button = tk.Button(frame, text="Ask", command=lambda:[ask(IMAGE_NAME, net_balance)])
                skip_button = tk.Button(frame, text="Skip", command=lambda:[top.destroy,skip2(IMAGE_NAME, net_balance)])
                next_button = tk.Button(frame, text="NEXT", command=top.destroy)

                ask_button.pack(side=tk.LEFT)
                skip_button.pack(side=tk.RIGHT)
                next_button.pack(side=tk.RIGHT)
                window.mainloop()

            if c in [9,18,27,36,45]:
                y = random.choice(["87","89"])
                IMAGE_NAME = "Slide"+y+".JPG"
                if y == "87":
                    requester = "teammate"
                else:
                    requester = "stranger"
                window = tk.Toplevel()
                top=window
                window.title("Request for donation")
                window.geometry("800x600")
                window.configure(background='grey')
                frame = tk.Frame(window)
                frame.pack()

                path = IMAGE_NAME
                img = ImageTk.PhotoImage(Image.open(path))
                panel = tk.Label(window, image = img)
                panel.pack(side = "bottom", fill = "both", expand = "yes")

            
                donate_button = tk.Button(frame, text="Donate", command=lambda:[help(IMAGE_NAME, net_balance)])
                refuse_button = tk.Button(frame, text="Refuse", command=lambda:[top.destroy,skip(IMAGE_NAME, net_balance)])
                next_button = tk.Button(frame, text="NEXT", command=top.destroy)


                donate_button.pack(side=tk.LEFT)
                refuse_button.pack(side=tk.RIGHT)
                next_button.pack(side=tk.RIGHT)
                window.mainloop()

            df_G2.to_csv("Experiment Result2")


class App3(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Experiment')
        self.geometry('1000x600')

        self.label = tk.Label(self, text="""Congradulations, my friend!\n
You have entered our second round of the competition.\n\n
YOUR INTIAL RESOURCES POINT:\n\n
500 \n\n
""")
        self.label.pack()

        self.button = tk.Button(self, text='Start!')
        self.button['command'] = self.button_clicked
        self.button.pack()
    def button_clicked(self):
        def retrieve(IMAGE_NAME):
            return
        
        def accept(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'accept'
            global dict
            loss = dict['Loss'][b] 
            gain = dict['Gain'][b]
            choice = [loss,gain]
            reward =  random.choice(choice)
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row1 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G3
            df_G3 = df_G3.append(new_row1, ignore_index=True)
            return net_balance

        def reject(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'reject'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G3
            df_G3 = df_G3.append(new_row2, ignore_index=True)
            return

        def change_value():
            global buttonClicked
            if buttonClicked:
                buttonClicked=False
            if not buttonClicked:
                buttonClicked=True     
        
        def defer(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'defer'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G3
            df_G3 = df_G3.append(new_row2, ignore_index=True)
            return

        def ask(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'ask'
            reward = 100 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G3
            df_G3 = df_G3.append(new_row2, ignore_index=True)
            window = tk.Toplevel()
            top=window
            window.title("Day"+str(c))
            window.geometry("400x300")
            donation = tk.Label(top, text = "Your current balance has been updated to:" + str(net_balance)).place(x = 20,y = 10)
            next_button = tk.Button(top, text="NEXT", command=top.destroy).place(x = 200, y = 80) 
            window.mainloop()
            return

        def help(IMAGE_NAME, net_balance):
            def call_result(label_result, n1):
                num1 = (n1.get())  
                result = int(num1)  
                label_result.config(text="You have donated %d to the requester!" % result)
                reward = -result
                NBD = net_balance - result
                scenario = IMAGE_NAME
                decision = 'help'
                tme = int(time.time())
                new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':NBD, 'time':tme}

                global df_G3
                df_G3 = df_G3.append(new_row2, ignore_index=True)

                return

            window = tk.Toplevel()
            top=window
            window.title("Day"+str(c))
            window.geometry("400x300")
            donation = tk.Label(top, text = "Please specify your amount of donation:").place(x = 20,y = 10)
            next_button = tk.Button(top, text="NEXT", command=top.destroy).place(x = 200, y = 80) 

            number1 = tk.StringVar()
            labelNum1 = tk.Label(top, text="Your Donation:").place(x = 20, y = 30) 
            labelResult = tk.Label(top)  
            labelResult.place(x = 20, y = 50) 
            entryNum1 = tk.Entry(top, textvariable=number1).place(x = 120, y = 30) 
            call_result = partial(call_result, labelResult, number1)
            buttonCal = tk.Button(top, text="Confirm", command=call_result).place(x = 20, y = 80) 
           
            window.mainloop()
            return

        def skip(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'refuse'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G3
            df_G3 = df_G3.append(new_row2, ignore_index=True)
            return 

        def skip2(IMAGE_NAME, net_balance):
            scenario = IMAGE_NAME
            decision = 'no_ask'
            reward = 0 
            net_balance = net_balance + reward
            tme = int(time.time())
            new_row2 = {'scenario':scenario, 'decision':decision, 'reward':reward, 'balance':net_balance, 'time':tme}
            global df_G3
            df_G3 = df_G3.append(new_row2, ignore_index=True)
            return

        epoch = int(time.time())
        L_I = ['36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85']
        L_S = ['86','87', '88','89']
        L_G = ['Slide60.JPG','Slide61.JPG','Slide62.JPG','Slide63.JPG','Slide64.JPG','Slide65.JPG','Slide66.JPG','Slide67.JPG','Slide68.JPG','Slide69.JPG','Slide70.JPG','Slide71.JPG','Slide72.JPG','Slide73.JPG','Slide74.JPG','Slide75.JPG','Slide76.JPG','Slide77.JPG','Slide78.JPG','Slide79.JPG','Slide80.JPG','Slide81.JPG','Slide82.JPG','Slide83.JPG','Slide84.JPG','Slide85.JPG',
]
        c = 1
        net_balance = 500
        group_balance = 0
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
            panel = tk.Label(window, image = img, text="NET BALANCE: "+str(net_balance))
            panel.pack(side = "bottom", fill = "both", expand = "yes")
                        
            accept_button = tk.Button(frame, text="Accept", command=lambda:[accept(IMAGE_NAME, net_balance)])
            reject_button = tk.Button(frame, text="Reject", command=lambda:[reject(IMAGE_NAME, net_balance)])
            next_button = tk.Button(frame, text="NEXT", command=top.destroy)
            defer_button = tk.Button(frame, text="Defer", command=lambda:[defer(IMAGE_NAME, net_balance)])

            accept_button.pack(side=tk.LEFT)
            reject_button.pack(side=tk.RIGHT)
            defer_button.pack(side=tk.LEFT)
            next_button.pack(side=tk.RIGHT)

            last_row = len(df_G3)
            second_last_row = last_row - 1

            window.mainloop()

            net_balance = df_G3.loc[last_row,'balance']

            if IMAGE_NAME in L_G:
                group_balance = group_balance + int(df_G3.loc[df_G3['scenario'] == IMAGE_NAME, 'reward'])
            else:
                pass

            if IMAGE_NAME in L_G:
                j = df_G3.iat[last_row, 2]
                group_balance = group_balance + j
            else:
                pass

            c = c + 1
            if (c - 1) % 5 == 0:
                window = tk.Toplevel()
                top=window
                window.title("5-Day Update")
                window.geometry("400x300")
                window.configure(background='grey')
                frame = tk.Frame(window)
                frame.pack()
                
                window.label=tk.Label(top, text="YOUR CURRENT NET BALANCE: "+str(net_balance)+"\n YOUR GROUP HAS ACCUMULATED " +str(group_balance)+" RPs")
                window.label.pack()
                next_button = tk.Button(frame, text="NEXT", command=top.destroy)

                next_button.pack(side=tk.RIGHT)
                window.mainloop()

                w = "86"
                IMAGE_NAME = "Slide"+w+".JPG"
                window = tk.Toplevel()
                top=window
                window.title("5-Day Update")
                window.geometry("800x600")
                window.configure(background='grey')
                frame = tk.Frame(window)
                frame.pack()

                path = IMAGE_NAME
                img = ImageTk.PhotoImage(Image.open(path))
                panel = tk.Label(window, image = img)
                panel.pack(side = "bottom", fill = "both", expand = "yes")

                ask_button = tk.Button(frame, text="Ask", command=lambda:[ask(IMAGE_NAME, net_balance)])
                skip_button = tk.Button(frame, text="Skip", command=lambda:[top.destroy,skip2(IMAGE_NAME, net_balance)])
                next_button = tk.Button(frame, text="NEXT", command=top.destroy)

                ask_button.pack(side=tk.LEFT)
                skip_button.pack(side=tk.RIGHT)
                next_button.pack(side=tk.RIGHT)
                window.mainloop()

            if c in [9,18,27,36,45]:
                y = random.choice(["87","89"])
                IMAGE_NAME = "Slide"+y+".JPG"
                if y == "87":
                    requester = "teammate"
                else:
                    requester = "stranger"
                window = tk.Toplevel()
                top=window
                window.title("Request for donation")
                window.geometry("800x600")
                window.configure(background='grey')
                frame = tk.Frame(window)
                frame.pack()

                path = IMAGE_NAME
                img = ImageTk.PhotoImage(Image.open(path))
                panel = tk.Label(window, image = img)
                panel.pack(side = "bottom", fill = "both", expand = "yes")

            
                donate_button = tk.Button(frame, text="Donate", command=lambda:[help(IMAGE_NAME, net_balance)])
                refuse_button = tk.Button(frame, text="Refuse", command=lambda:[top.destroy,skip(IMAGE_NAME, net_balance)])
                next_button = tk.Button(frame, text="NEXT", command=top.destroy)


                donate_button.pack(side=tk.LEFT)
                refuse_button.pack(side=tk.RIGHT)
                next_button.pack(side=tk.RIGHT)
                window.mainloop()

            df_G3.to_csv("Experiment Result3")


df = pd.DataFrame()
df_B2 = pd.DataFrame()
df_G1 = pd.DataFrame()
df_G2 = pd.DataFrame()
df_G3 = pd.DataFrame()
df1 = pd.read_csv('Graph.csv')
dict = df1.to_dict()
buttonClicked = False

if __name__ == "__main__":
    app = App()
    app.mainloop()

if __name__ == "__main__":
    app = App0()
    app.mainloop()

if __name__ == "__main__":
    app = App1()
    app.mainloop()


if __name__ == "__main__":
    app = App2()
    app.mainloop()


if __name__ == "__main__":
    app = App3()
    app.mainloop()
