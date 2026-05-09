from tkinter import *
import random
from tkinter import ttk
import time
from tkinter import *
#import sounddevice as sd
#from scipy.io.wavfile import write
#from #playsound import playsound


def PFood():
    
    window=Tk()
    window.title('food Memory Game')
    #-------------------------------------------------------------memory game-----------------------------------------------------------------
    tabs = ttk.Notebook(window) 
    root= ttk.Frame(tabs)
    global base, board,ans,moves,prev,base2,ans2,guess,P, starting_time, countdown, points,Q,Jabel,S, LabelN, LabelL,words, start_time, complete
    base=Canvas(root,width=500,height=500)
    base.pack()
    root2= ttk.Frame(tabs)
    root3= ttk.Frame(tabs)
    root4 = ttk.Frame(tabs)
    tabs.add(root, text ='memory') 
    tabs.add(root2, text ='speed')
    tabs.add(root3, text ='practise')
    tabs.add(root4, text = "exit")

    tabs.pack(expand = 3, fill ="both")
    base3=Canvas(root3,width=1000,height=1000)
    base3.pack()
    complete = 0
        
    def draw(c,i,j):
        global base, matched
        e = c.upper()
        if e=='A':
            if c =='a':
                d = base.create_text(100*i+50, 100*j+50, text = "mineral water")
                #playsound('Mineral water.wav')
                return
            elif c =='A':
                d = base.create_text(100*i+50, 100*j+50, text = "woda mineralna")
                return
        elif e=='B':
            if c =='b':
                d = base.create_text(100*i+50, 100*j+50, text = "a black \n coffee")
                #playsound('a black coffee.wav')
                return
            elif c =='B':
                d = base.create_text(100*i+50, 100*j+50, text = "czarna kawa")
                return
        elif e=='C':
            if c =='c':
                d = base.create_text(100*i+50, 100*j+50, text = "tea with \n lemon")
                #playsound('tea with lemon.wav')
                return
            elif c =='C':
                d = base.create_text(100*i+50, 100*j+50, text = "Herbata z cytryna")
                return
        elif e=='D':
            if c =='d':
                d = base.create_text(100*i+50, 100*j+50, text = "sugar")
                #playsound('sugar.wav')
                return
            elif c =='D':
               d = base.create_text(100*i+50, 100*j+50, text = "Cukier")
        elif e=='E':
            if c =='e':
                d = base.create_text(100*i+50, 100*j+50, text = "milk")
                #playsound('Milk.wav')
            elif c =='E':
                d = base.create_text(100*i+50, 100*j+50, text = "Mleko")
        elif e=='F':
            if c =='f':
                d = base.create_text(100*i+50, 100*j+50, text = "salt")
                #playsound('salt.wav')
            elif c =='F':
                d = base.create_text(100*i+50, 100*j+50, text = "Sol")
        elif e=='G':
            if c =='g':
                d = base.create_text(100*i+50, 100*j+50, text = "pepper")
                #playsound('pepper.wav')
            elif c =='G':
                d = base.create_text(100*i+50, 100*j+50, text = "Pieprz")
        elif e=='H':
            if c =='h':
                d = base.create_text(100*i+50, 100*j+50, text = "a table for\n two please")
                #playsound('a table for two please.wav')
            elif c =='H':
                d = base.create_text(100*i+50, 100*j+50, text = "Stolik dla\n dwojga prosze")
        elif e=='I':
            if c =='i':
                d = base.create_text(100*i+50, 100*j+50, text = "here is the menu")
                #playsound('here is the menu.wav')
            elif c =='I':
                d = base.create_text(100*i+50, 100*j+50, text = "Oto menu")
        elif e=='J':
            if c =='j':
                d = base.create_text(100*i+50, 100*j+50, text = "do you want\n to order?")
                #playsound('do you want to order.wav')
            elif c =='J':
                d = base.create_text(100*i+50, 100*j+50, text = "Chcesz zamowic?")
        if matched == True:
            time.sleep(2)
            #playsound('matched.wav')

            
    def timeupdate2():
        global starting_time, countdown
        current_time = int(time.strftime("%M"))*60+ int(time.strftime("%S"))
        time_difference = current_time - starting_time
        countdown = 60 - time_difference
        
    def displayBoard():
        global base,ans,board,moves, matched, complete
        
        cnt=0
        for i in range(5):
            for j in range(4):
                rect=base.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="lavender")
                if(board[i][j]!='.'):
                    draw(board[i][j],i,j)
                    cnt+=1
        if cnt==20:
            Endtime = int(time.strftime("%M"))*60+ int(time.strftime("%S"))
            totaltime = Endtime - start_time
            totalmins = totaltime//60
            totalsecs = totaltime%60
            base.create_text(250,450,text="Moves "+str(moves)+ " Time taken "+ str(totalmins)+ " mins and "+ str(totalsecs)+ " secs",font=('arial',20))
            base.create_text(250,550,text="click here to save game data",font=('arial',20))
            #playsound('game end.wav')
            complete+=1
                
    def callback(event):
        global base,ans,board,moves,prev, start_time, matched
        if start_time == 10000:
            start_time = int(time.strftime("%M"))*60+ int(time.strftime("%S"))
            
        
        i=event.x//100
        j=event.y//100
        
        if j == 5:
            savedgms = open("saved games.txt", "a")
            savedgms.append("Moves: "+str(moves)+ " Time taken "+ str(totalmins))
        if board[i][j]!='.':
            return
        # if prev is invalid 
        moves+=1
        
        if(prev[0]>5):
            prev[0]=i
            prev[1]=j
            board[i][j]=ans[i][j]
            displayBoard()
        else:
            board[i][j]=ans[i][j]
            displayBoard()
            if(ans[i][j].upper()==board[prev[0]][prev[1]].upper()):
                matched = True
                print("matched")
                prev=[100,100]
                displayBoard()
                matched = False
                return
            else:
                board[prev[0]][prev[1]]='.'
                displayBoard()
                prev=[i,j]
                return
            
    start_time = 10000
    ans = list('AaBbCcDdEeFfGgHhIiJj')
    random.shuffle(ans)
    ans = [ans[:4],
           ans[4:8],
           ans[8:12],
           ans[12:16],
           ans[16:]]
    base.bind("<Button-1>", callback)
    moves=IntVar()
    moves=0
    prev=[100,100]
    board=[list('.'*4) for cnt in range(5)]
    displayBoard()
    #-------------------------------------------------------------speed-----------------------------------------------------------------




    def draw2(c,i,j):
        e = c
        c = c.upper()
        global base2
        if c== "A":
            if e == "A":
                text = "mineral water"
                return text
            if e == "a":
                text = "Woda mineralna"
                return text
        elif c== "B":
            if e == "B":
                text = "A black coffee"
                return text
            if e == "b":
                text = "Czarna kawa"
                return text
        elif c== "C":
            if e == "C":
                text = "tea with lemon"
                return text
            if e == "c":
                text = "Herbata z cytryna"
                return text
        elif c== "D":
            if e == "D":
                text = "sugar"
                return text
            if e == "d":
                text = "Cukier"
                return text
        elif c== "E":
            if e == "E":
                text = "milk"
                return text
            if e == "e":
                text = "Mleko"
                return text
        elif c== "F":
            if e == "F":
                text = "salt"
                return text
            if e == "f":
                text = "Sol"
                return text
        elif c== "G":
            if e == "G":
                text = "pepper"
                return text
            if e == "g":
                text = "Pieprz"
                return text
        elif c== "H":
            if e == "H":
                text = "a table for two please"
                return text
            if e == "h":
                text = "Stolik dla dwojga prosze"
                return text
        elif c== "I":
            if e == "I":
                text = "here is the menu"
                return text
            if e == "i":
                text = "Oto menu"
                return text
        elif c== "J":
            if e == "J":
                text = "do you want to order?"
                return text
            if e == "j":
                text = "Checesz zamowic?"
                return text

        
        
    def displayboard2():
        global base2,ans2
        cnt=0
        for I in range(5):
            for J in range(2):
                rect=base2.create_rectangle(150*I,J*150,150*I+150,150*J+150,fill="lavender")
                texta = draw2(ans2[J][I],I,J)
                label = base2.create_text(150*I+60,150*J+75, text = texta)

    def timeupdate2():
        global starting_time, countdown
        current_time = int(time.strftime("%M"))*60+ int(time.strftime("%S"))
        time_difference = current_time - starting_time
        countdown = 60 - time_difference
        
        
        
    def guesschange(P):
        global base2,Q,Jabel
        base2.delete(Jabel)
        textb = draw2(guess[P],P,Q)
        Jabel = base2.create_text(400,600, text = textb)
            
        
        
                
    def check(event):
        global base2,ans2,guess,P, starting_time, countdown, marks
        if starting_time== 1000:
            marks = 0
            countdown = 60
            starting_time = int(time.strftime("%M"))*60+ int(time.strftime("%M"))
            
        if countdown <=0:
            base2.create_text(400,450, text = "Times up")
            base2.create_text(400,475, text = " You this many correct "+ str(marks))
            complete +=1
            
        I=event.x//150
        J=event.y//150
        if (guess[P].upper() == ans2[J][I].upper()) and  countdown >=0:
            print("correct")
            
            marks = marks+1
            if P<(len(guess)-1):
                P=P+1
                guesschange(P)
            else:
                P = 0
                random.shuffle(guess)
                guesschange(P)

        else:
            print("incorrect")
        timeupdate2()   
        
            
    base2=Canvas(root2,width=1000,height=1000)
    base2.pack()
    starting_time = 1000
    P = 0
    ans2 = list("aBcDeFgHiJ")
    guess = list("AbCdEfGhIj")
    random.shuffle(guess)
    random.shuffle(ans2)
    ans2 = [ans2[:5],
            ans2[5:]]
    base2.bind("<Button-1>", check)
    Q = 0
    marks = 0
    countdown = 60
    rect=base2.create_rectangle(300,500,500,700,fill="lavender")
    textb = draw2(guess[P],P,Q)
    Jabel = base2.create_text(400,600, text = textb)
    base2.create_text(400,400, text = "Once you click your first answer the a 60 second timer will begin ")
    displayboard2()

    #------------------------------------------practise--------------------------------

    
        
    def guesschange1():
        global S, LabelN, LabelL
        base3.delete(LabelN)
        base3.delete(LabelL)
        textN = draw3(words[S],S)
        LabelN = base3.create_text(300,300, text = textN)
        textL = draw3(words[S].lower(),S)
        LabelL = base3.create_text(600,300, text = textL)
        
    def draw3(c,i):
        
       
        global base3
        if c== "A":
            text = "mineral water"
            return text
        elif c == "a":
            text = "Woda mineralna"
            return text
        elif c== "B":
            text = "a black \n coffee"
            return text
        elif c == "b":
            text = "Czarna kawa"
            return text
        elif c== "C":
            text = "tea with \n lemon"
            return text
        elif c == "c":
            text = "THerbata z cytryna"
            return text
        elif c== "D":
            text = "sugar"
            return text
        elif c == "d":
            text = "Cukier"
            return text
        elif c== "E":
            text = "milk"
            return text
        elif c == "e":
            text = "Mleko"
            return text
        elif c== "F":
            text = "salt"
            return text
        elif c == "f":
            text = "Sol"
            return text
        elif c== "G":
            text = "pepper"
            return text
        elif c == "g":
            text = "Pieprz"
            return text
        elif c== "H":
            text = "a table for two please "
            return text
        elif c == "h":
            text = "Stolik dla dwojga prosze"
            return text
        elif c== "I":
            text = "here is the menu"
            return text
        elif c == "i":
            text = "Oto menu"
            return text
        elif c== "J":
            text = "do you want\n to order?"
            return text
        elif c == "j":
            text = "Checesz zamowic?"
            return text


    def change(event):
        global S, words
        if  event.x > 700 and event.y>200:
            if S< len(words)-1:
                S = S+1
                guesschange1()
            else:
                S = 0
                guesschange1()
        elif event.x < 100 and event.y>200:
            if S == 0:
                S = len(words) - 1
                guesschange1()
            else:
                S = S-1
                print(S)
                guesschange1()
        elif event.x>500 and event.y>200 and event.x<700:
            fs = 44100  # Sample rate
            seconds = 5  # Duration of recording

            #myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            #sd.wait()  # Wait until recording is finished
            #write('output.wav', fs, myrecording)  # Save as WAV file
            playback = Tk()
            Button(playback, text="playrecording", width=10, height=1, bg="green",command=playrecording).pack()

    def playrecording():
        #playsound('output.wav')
        print("this version does not have sound packages installed")
                
    recta=base3.create_rectangle(200,200,400,400,fill="lavender")
    rect1=base3.create_rectangle(500,200,700,400,fill="lavender")

    button=base3.create_rectangle(810,250,900,350,fill="lavender")
    button1=base3.create_rectangle(10,250,100,350,fill="lavender")
    base3.create_polygon(830,260,880,300,830,340, fill="red")
    base3.create_polygon(80,260,30,300,80,340, fill="red")
    
    base3.bind("<Button 1>", change)

    words = list("ABCDEFGHIJ")
    S = 0
    textN = draw3(words[S],S)
    LabelN = base3.create_text(300,300, text = textN)
    textL = draw3(words[S].lower(),S)
    LabelL = base3.create_text(600,300, text = textL)
    base3.create_text(300,380, text = "click here to play")
    base3.create_text(600,380, text = "click here to record")
#-----------------------------------------Exit--------------------------------------   
    def BacktoHp():
        global complete, points
        points = points + complete*20
        homepage1()
        
    
    Exit = ttk.Button(root4, text = 'Exit', command = BacktoHp)
    Exit.pack()
    window.mainloop()
    window.mainloop()

def IFood():
    
    window=Tk()
    window.title('food Memory Game')
    #-------------------------------------------------------------memory-----------------------------------------------------------------
    tabs = ttk.Notebook(window) 
    root= ttk.Frame(tabs)
    global base, board,ans,moves,prev,base2,ans2,guess,P, starting_time, countdown, points,Q,Jabel,S, LabelN, LabelL,words, start_time, complete
    base=Canvas(root,width=500,height=500)
    base.pack()
    root2= ttk.Frame(tabs)
    root3= ttk.Frame(tabs)
    root4= ttk.Frame(tabs)
    tabs.add(root, text ='memory') 
    tabs.add(root2, text ='speed')
    tabs.add(root3, text ='practise')
    tabs.add(root4, text ='exit')

    tabs.pack(expand = 3, fill ="both")
    base3=Canvas(root3,width=1000,height=1000)
    base3.pack()
    complete = 0
        
    def draw(c,i,j):
        global base
        e = c.upper()
        if e=='A':
            if c =='a':
                d = base.create_text(100*i+50, 100*j+50, text = "mineral water")
                return
            elif c =='A':
                d = base.create_text(100*i+50, 100*j+50, text = "acqua minerale")
                return
        elif e=='B':
            if c =='b':
                d = base.create_text(100*i+50, 100*j+50, text = "a black \n coffee")
                return
            elif c =='B':
                d = base.create_text(100*i+50, 100*j+50, text = "un caffe nero")
                return
        elif e=='C':
            if c =='c':
                d = base.create_text(100*i+50, 100*j+50, text = "tea with \n lemon")
                return
            elif c =='C':
                d = base.create_text(100*i+50, 100*j+50, text = "Te con limone")
                return
        elif e=='D':
            if c =='d':
                d = base.create_text(100*i+50, 100*j+50, text = "sugar")
                return
            elif c =='D':
               d = base.create_text(100*i+50, 100*j+50, text = "Zucchero")
        elif e=='E':
            if c =='e':
                d = base.create_text(100*i+50, 100*j+50, text = "milk")
            elif c =='E':
                d = base.create_text(100*i+50, 100*j+50, text = "Latte")
        elif e=='F':
            if c =='f':
                d = base.create_text(100*i+50, 100*j+50, text = "salt")
            elif c =='F':
                d = base.create_text(100*i+50, 100*j+50, text = "Sale")
        elif e=='G':
            if c =='g':
                d = base.create_text(100*i+50, 100*j+50, text = "pepper")
            elif c =='G':
                d = base.create_text(100*i+50, 100*j+50, text = "Pepe")
        elif e=='H':
            if c =='h':
                d = base.create_text(100*i+50, 100*j+50, text = "a table for\n two please")
            elif c =='H':
                d = base.create_text(100*i+50, 100*j+50, text = "un tavolo per\n due per favour")
        elif e=='I':
            if c =='i':
                d = base.create_text(100*i+50, 100*j+50, text = "here is the menu")
            elif c =='I':
                d = base.create_text(100*i+50, 100*j+50, text = "Ecco il menu")
        elif e=='J':
            if c =='j':
                d = base.create_text(100*i+50, 100*j+50, text = "do you want\n to order?")
            elif c =='J':
                d = base.create_text(100*i+50, 100*j+50, text = "Volete ordinaire?")
        
    def timeupdate2():
        global starting_time, countdown
        current_time = int(time.strftime("%M"))*60+ int(time.strftime("%S"))
        time_difference = current_time - starting_time
        countdown = 60 - time_difference
        
    def displayBoard():
        global base,ans,board,moves, complete
        
        cnt=0
        for i in range(5):
            for j in range(4):
                rect=base.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="lavender")
                if(board[i][j]!='.'):
                    draw(board[i][j],i,j)
                    cnt+=1
        if cnt==20:
            Endtime = int(time.strftime("%M"))*60+ int(time.strftime("%S"))
            totaltime = Endtime - start_time
            totalmins = totaltime//60
            totalsecs = totaltime%60
            base.create_text(250,450,text="Moves "+str(moves)+ " Time taken "+ str(totalmins)+ "mins and "+ str(totalsecs)+ " secs",font=('arial',20))
            base.create_text(250,550,text="click here to save game data",font=('arial',20))
            complete +=1
            #playsound('game end.wav')
                
    def callback(event):
        global base,ans,board,moves,prev, start_time
        if start_time == 10000:
            start_time = int(time.strftime("%M"))*60+ int(time.strftime("%S"))
            
        i=event.x//100
        j=event.y//100

        if j == 5:
            savedgms = open("seved games.txt", "a")
            savedgms.append("Moves: "+str(moves)+ " Time taken "+ str(totalmins))
        if board[i][j]!='.':
            return
        # if prev is invalid 
        moves+=1

        if(prev[0]>5):
            prev[0]=i
            prev[1]=j
            board[i][j]=ans[i][j]
            displayBoard()
        else:
            board[i][j]=ans[i][j]
            displayBoard()
            if(ans[i][j].upper()==board[prev[0]][prev[1]].upper()):
                matched = True
                print("matched")
                prev=[100,100]
                displayBoard()
                matched = False
                return
            else:
                board[prev[0]][prev[1]]='.'
                displayBoard()
                prev=[i,j]
                return
            
    start_time = 10000
    ans = list('AaBbCcDdEeFfGgHhIiJj')
    random.shuffle(ans)
    ans = [ans[:4],
           ans[4:8],
           ans[8:12],
           ans[12:16],
           ans[16:]]
    base.bind("<Button-1>", callback)
    moves=IntVar()
    moves=0
    prev=[100,100]
    board=[list('.'*4) for cnt in range(5)]
    displayBoard()
    #-------------------------------------------------------------speed-----------------------------------------------------------------




    def draw2(c,i,j):
        e = c
        c = c.upper()
        global base2
        if c== "A":
            if e == "A":
                text = "mineral water"
                return text
            if e == "a":
                text = "acqua minerale"
                return text
        elif c== "B":
            if e == "B":
                text = "A black coffee"
                return text
            if e == "b":
                text = "un caffe nero"
                return text
        elif c== "C":
            if e == "C":
                text = "tea with lemon"
                return text
            if e == "c":
                text = "te con limone"
                return text
        elif c== "D":
            if e == "D":
                text = "sugar"
                return text
            if e == "d":
                text = "zucchero"
                return text
        elif c== "E":
            if e == "E":
                text = "milk"
                return text
            if e == "e":
                text = "latte"
                return text
        elif c== "F":
            if e == "F":
                text = "salt"
                return text
            if e == "f":
                text = "sale"
                return text
        elif c== "G":
            if e == "G":
                text = "pepper"
                return text
            if e == "g":
                text = "pepe"
                return text
        elif c== "H":
            if e == "H":
                text = "a table for two please"
                return text
            if e == "h":
                text = "un tavolo per\n due per favour"
                return text
        elif c== "I":
            if e == "I":
                text = "here is the menu"
                return text
            if e == "i":
                text = "ecco il menu"
                return text
        elif c== "J":
            if e == "J":
                text = "do you want to order?"
                return text
            if e == "j":
                text = "Volete ordinaire?"
                return text
        if matched == True:
            time.sleep(2)
            #playsound('matched.wav')
        
        
    def displayboard2():
        global base2,ans2
        cnt=0
        for I in range(5):
            for J in range(2):
                rect=base2.create_rectangle(150*I,J*150,150*I+150,150*J+150,fill="lavender")
                texta = draw2(ans2[J][I],I,J)
                label = base2.create_text(150*I+60,150*J+75, text = texta)

    def timeupdate2():
        global starting_time, countdown
        current_time = int(time.strftime("%M"))*60+ int(time.strftime("%S"))
        time_difference = current_time - starting_time
        countdown = 60 - time_difference
        
        
        
    def guesschange(P):
        global base2,Q,Jabel
        base2.delete(Jabel)
        textb = draw2(guess[P],P,Q)
        Jabel = base2.create_text(400,600, text = textb)
            
        
        
                
    def check(event):
        global base2,ans2,guess,P, starting_time, countdown, marks
        if starting_time== 1000:
            marks = 0
            countdown = 60
            starting_time = int(time.strftime("%M"))*60+ int(time.strftime("%M"))
            
        if countdown <=0:
            base2.create_text(400,450, text = "Times up")
            base2.create_text(400,475, text = " You this many correct "+ str(marks))
            complete +=1
            
        I=event.x//150
        J=event.y//150
        if (guess[P].upper() == ans2[J][I].upper()) and  countdown >=0:
            
            if P<(len(guess)-1):
                P=P+1
                guesschange(P)
            else:
                P = 0
                random.shuffle(guess)
                guesschange(P)

        else:
            print("incorrect")
        timeupdate2()   
        
            
    base2=Canvas(root2,width=1000,height=1000)
    base2.pack()
    starting_time = 1000
    P = 0
    ans2 = list("aBcDeFgHiJ")
    guess = list("AbCdEfGhIj")
    random.shuffle(guess)
    random.shuffle(ans2)
    ans2 = [ans2[:5],
            ans2[5:]]
    base2.bind("<Button-1>", check)
    Q = 0
    marks = 0
    countdown = 60
    rect=base2.create_rectangle(300,500,500,700,fill="lavender")
    textb = draw2(guess[P],P,Q)
    Jabel = base2.create_text(400,600, text = textb)
    base2.create_text(400,400, text = "Once you click your first answer the a 60 second timer will begin ")
    displayboard2()

    #------------------------------------------practise--------------------------------

    
        
    def guesschange1():
        global S, LabelN, LabelL
        base3.delete(LabelN)
        base3.delete(LabelL)
        textN = draw3(words[S],S)
        LabelN = base3.create_text(300,300, text = textN)
        textL = draw3(words[S].lower(),S)
        LabelL = base3.create_text(600,300, text = textL)
        
    def draw3(c,i):
        
       
        global base3
        if c== "A":
            text = "mineral water"
            return text
        elif c == "a":
            text = "acqua minerale"
            return text
        elif c== "B":
            text = "a black \n coffee"
            return text
        elif c == "b":
            text = "un caffe nero"
            return text
        elif c== "C":
            text = "tea with \n lemon"
            return text
        elif c == "c":
            text = "Te con limone"
            return text
        elif c== "D":
            text = "sugar"
            return text
        elif c == "d":
            text = "Zucchero"
            return text
        elif c== "E":
            text = "milk"
            return text
        elif c == "e":
            text = "latte"
            return text
        elif c== "F":
            text = "salt"
            return text
        elif c == "f":
            text = "sale"
            return text
        elif c== "G":
            text = "pepper"
            return text
        elif c == "g":
            text = "pepe"
            return text
        elif c== "H":
            text = "a table for two please "
            return text
        elif c == "h":
            text = "un tavolo per\n due per favour"
            return text
        elif c== "I":
            text = "here is the menu"
            return text
        elif c == "i":
            text = "Ecco il menu"
            return text
        elif c== "J":
            text = "do you want\n to order?"
            return text
        elif c == "j":
            text = "Volete ordinaire?"
            return text


    def change(event):
        global S, words
        if  event.x > 700 and event.y>200:
            if S< len(words)-1:
                S = S+1
                guesschange1()
            else:
                S = 0
                guesschange1()
        elif event.x < 100 and event.y>200:
            if S == 0:
                S = len(words) - 1
                guesschange1()
            else:
                S = S-1
                print(S)
                guesschange1()
        elif event.x>500 and event.y>200 and event.x<700:
            fs = 44100  # Sample rate
            seconds = 5  # Duration of recording

            #myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            #sd.wait()  # Wait until recording is finished
            #write('vocalrecording.wav', fs, myrecording)  # Save as WAV file
            playback = Tk()
            Button(playback, text="playrecording", width=10, height=1, bg="green",command=playrecording).pack()

    def playrecording():
        #playsound('vocalrecording.wav')
        print("this version does not have sound packages installed")
                
    recta=base3.create_rectangle(200,200,400,400,fill="lavender")
    rect1=base3.create_rectangle(500,200,700,400,fill="lavender")

    button=base3.create_rectangle(810,250,900,350,fill="lavender")
    button1=base3.create_rectangle(10,250,100,350,fill="lavender")
    base3.create_polygon(830,260,880,300,830,340, fill="red")
    base3.create_polygon(80,260,30,300,80,340, fill="red")
    
    base3.bind("<Button 1>", change)

    words = list("ABCDEFGHIJ")
    S = 0
    textN = draw3(words[S],S)
    LabelN = base3.create_text(300,300, text = textN)
    textL = draw3(words[S].lower(),S)
    LabelL = base3.create_text(600,300, text = textL)
    base3.create_text(300,380, text = "click here to play")
    base3.create_text(600,380, text = "click here to record")
#--------------------------------------------Exit---------------------------------
    def BacktoHp():
        global complete, points
        points = points + complete*20
        homepage1()
        
    
    Exit = ttk.Button(root4, text = 'Exit', command = BacktoHp)
    Exit.pack()
    window.mainloop()

def homepage1():
    global Nativeclicked, Learnclicked, points
    def leaderboard():
        leaderboard=Tk()
        leaderboard.title('leaderboard')
        text_area = tk.Text(master=leaderboard,height=12,width=30,bg="#FFFF99")
        text_area.grid(column=0,row=4)
        
        
        scores = [] 
        #LEADERBOARD SECTION 
        for line in open('Leaderboard.txt', 'r'):
            name, score = line.split(",")
            score = int(score) 
            scores.append((name, score))

        scores = sorted(scores, reverse = True)
        for i in range(0,len(scores)-1):
            text_area.insert(tk.END,scores[i])
            text_area.insert(tk.END,"\n")

        window.mainloop()

    def appfeedback():

        feedback = Tk()
        e = Entry(feedback)
        e.pack()

        e.focus_set()

        def write():
                A = e.get()
                
                A = str(A)
                print(A)
                File = open('app feedback.txt', 'a')
                File.write(A+ "\n")
                File.close

        b = Button(feedback, text = "OK", width = 10, command = write)
        b.pack()
        
    def module1():
        global Nativeclicked, Learnclicked
        A = Nativeclicked.get()
        if A == "Italian":
            IFood()
        elif A == "Polish":
            PFood()

    def NA():
        ModuleError = Tk()
        ModuleError.title('this module/function does not exist')
        ErrorMessage = ttk.Label(ModuleError, text = 'Error this module/function does not yet exist')
        ErrorMessage.pack()

    homepage = Tk()
    homepage.geometry('600x600')
    homepage.title("homepage")

    homepage.columnconfigure(0,weight = 2 )
    homepage.columnconfigure(1,weight =1 )
    homepage.columnconfigure(2,weight =1 )
    homepage.columnconfigure(3,weight =1 )
    homepage.columnconfigure(4,weight =1 )
    
    homepage.rowconfigure(0,weight = 2)
    homepage.rowconfigure(1,weight = 2)
    homepage.rowconfigure(2,weight = 2)
    homepage.rowconfigure(3,weight = 2)
    homepage.rowconfigure(4,weight = 2)
    homepage.rowconfigure(5,weight = 1)
    
    
                          


    
    Nativeclicked = StringVar(homepage)
    Learnclicked = StringVar(homepage)

    logo = ttk.Label(homepage, text = 'Name+Logo', font = ('Arial', '20'))
    logo.grid(column =0, row = 0, sticky=W)

    profile = ttk.Label(homepage, text = 'profile', font = ('Arial', '16'))
    profile.grid(column =4, row = 0, sticky=W)

    Admin = ttk.Button(homepage, text = 'Admin', command = NA)
    Admin.grid(column =1 , row =0 )

    leaderboard = ttk.Button(homepage, text = 'leaderboard', command = leaderboard)
    leaderboard.grid(column =2 , row =0, sticky=W )

    

    AvMod = ttk.Label(homepage, text = 'available modules' , font = ('Arial 12 underline'), )
    AvMod.grid(column =1 , row =1, sticky=W )

    CC = ttk.Label(homepage, text = 'Course choose' , font = ('Arial 12 underline'))
    CC.grid(column =0 , row =1, sticky=W )

    pts = ttk.Label(homepage, text = 'points: '+ str(points) , font = ('Arial 12 '))
    pts.grid(column =3 , row =0, sticky=W )
    
    Ntive = ttk.Label(homepage, text = 'native language ', font = ('Arial 12 underline'))
    Ntive.grid(column =0 , row =2, sticky=NW )

    Lrn = ttk.Label(homepage, text = 'learning language ', font = ('Arial 12 underline'))
    Lrn.grid(column =0 , row =3, sticky=NW )
    
    dif = ttk.Label(homepage, text = 'difficulty setting', font = ('Arial 12 underline'))
    dif.grid(column =0 , row =4, sticky=NW )
    # Dropdown menu options
    Nativeoptions = [
        "Italian",
        "Polish",
    ]
      
    # datatype of menu text

    # initial menu text

      
    # Create Dropdown menu
    Nativedrop = OptionMenu( homepage , Nativeclicked , *Nativeoptions )
    Nativedrop.grid(column =0 , row =2, )

    Learnoptions = [
        "English",
        
    ]
      
    # datatype of menu text
      
    # Create Dropdown menu
    Learndrop = OptionMenu( homepage , Learnclicked , *Learnoptions )
    Learndrop.grid(column =0 , row =3 )

    Diffoptions = [
        "Easy",
        "Normal",
        "Hard"
        
    ]
      
    # datatype of menu text
    Diffclicked = StringVar()
      
    # initial menu text

      
    # Create Dropdown menu
    Diffdrop = OptionMenu( homepage , Diffclicked , *Diffoptions )
    Diffdrop.grid(column =0 , row =4 )



    b = Button(homepage, text = "appfeedback", width = 10, command = appfeedback)
    b.grid(column =0 , row =5 )



    Food = ttk.Button(homepage, text = 'Food', command = module1)
    Food.grid(column =1 , row =2 )

    module2 = ttk.Button(homepage, text = 'module2', command = NA)
    module2.grid(column =2 , row =2 )

    module3 = ttk.Button(homepage, text = 'module3', command = NA)
    module3.grid(column =3 , row =2)

    module4 = ttk.Button(homepage, text = 'module4', command = NA)
    module4.grid(column =4 , row =2 )

    module5 = ttk.Button(homepage, text = 'module5', command = NA)
    module5.grid(column =1 , row =4 )

    module6 = ttk.Button(homepage, text = 'module6', command = NA)
    module6.grid(column =2 , row =4 )

    module7 = ttk.Button(homepage, text = 'module7', command = NA)
    module7.grid(column =3 , row =4 )

    module8 = ttk.Button(homepage, text = 'module8', command = NA)
    module8.grid(column =4 , row =4 )


    homepage.mainloop()

def login():
    global New, points, login_screen
    points = 0
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        loginmessage.set("fill the empty field!!!")
    
    elif uname=="a" and pwd=="a":
        loginmessage.set("Login success")
        homepage1()
        
    elif uname=="a" and pwd==New:
        loginmessage.set("Login success")
        homepage1()
          
    else:
       loginmessage.set("Wrong username or password!!!")

def Loginform():
    global login_screen , loginmessage, username, password
    #Setting up login window
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("300x250")
    #declaring variables
    username = StringVar()
    password = StringVar()
    loginmessage=StringVar()
    Label(login_screen,width="300", text="Please enter details below", bg="green",fg="white").pack()
    #Username label and entry textbox
    Label(login_screen, text="Username").place(x=20,y=40)
    
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    #password label and entry textbox
    Label(login_screen, text="Password").place(x=20,y=80)

    Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    #Label for displaying login result
    Label(login_screen, text="",textvariable=loginmessage).place(x=95,y=100)
    
    Button(login_screen, text="Login", width=10, height=1, bg="green",fg="white",command=login).place(x=105,y=130)
    Button(login_screen, text="forgot password", width=12, height=1, bg="green",fg="white",command=passwordreset).place(x=100,y=170)
    login_screen.mainloop()
    
    
def checkusername():
    global New
    New = New.get()
    New = str(New)
    print(New)
    Label(Checkuser, text="incorrect username").pack()


def passwordreset():
    global New, Checkuser
    Checkuser = Tk()
    Label(Checkuser, text="Input new password").pack()
    New= Entry(Checkuser)
    New.pack()
    New.focus_set()
    b = Button(Checkuser, text = "OK", width = 10, command = checkusername)
    b.pack()
    
    
        
        

    
    
Loginform()
