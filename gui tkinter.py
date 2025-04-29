import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv

firstplace=9
secondplace=6
thirdplace=3
#these are the points given based on the placement of the teams
TeamList=["Red","Blue","Yellow","Green"]
IndividualList=[]
choice=()
TeamChoice=()
Red=[]
Blue=[]
Yellow=[]
Green=[]


Event1=[]
Event2=[]
Event3=[]
Event4=[]
Event5=[]
FirstPlaces=[]
SecondPlaces=[]
ThirdPlaces=[]
IndivFirst=[]
IndivSecond=[]
IndivThird=[]
IndivFourth=[]
IndivFifth=[]
global ScoreDictionary

mainwindow=("e")
def FinalWindow():
    val=list(ScoreDictionary.values())
    val.sort(reverse=True)
    FINALFIRST=list(ScoreDictionary.values())[0]
    winnertext="The Team in first place is: "+winner+" with a total point count of: "+str(FINALFIRST)
    indivscores="the winner of the first individual event is",IndivFirst






    
    FinalWindow=tk.Tk()
    FinalWindow.geometry=("1000x1000")
    FinalWindow.title("Final Scores")
    firstplacelabel=tk.Label(FinalWindow,text=winnertext)
    firstplacelabel.pack()
    indivscorelabel=tk.Label(FinalWindow,text=indivscores)
    indivscorelabel.pack()
##    secondplacelabel=tk.Label(FinalWindow,text="The Team in first place is: "+str(FINALSECOND))
##    secondplacelabel.pack()
##    thirdplacelabel=tk.Label(FinalWindow,text="The Team in first place is: "+str(FINALTHIRD))
##    thirdplacelabel.pack()



    
    FinalWindow.minsize(400, 200)
    FinalWindow.maxsize(450, 300)









    
def IndivScores():
    scorething.destroy()

    if tempvar==1:
        IndivFirst=Indivplace.get()
        print(IndivFirst)
    elif tempvar==2:
        IndivSecond=Indivplace.get()
    elif tempvar==3:
        IndivThird=Indivplace.get()
    elif tempvar==4:
        IndivFourth=Indivplace.get()
    elif tempvar==5:
        IndivFifth=Indivplace.get()

    
def PointsCalc():
    AllEvents=[Event1,Event2,Event3,Event4,Event5]
    LoopNum=0
    global RedPoints
    global BluePoints
    global YellowPoints
    global GreenPoints
    RedPoints=0
    BluePoints=0
    YellowPoints=0
    GreenPoints=0

    for i in AllEvents:
        x=0
        for i in i:
            x=x+1
            if x==1:
                FirstPlaces.append(i)
            if x==2:
                SecondPlaces.append(i)
            if x==3:
                ThirdPlaces.append(i)
    for i in FirstPlaces:
        temp=i
        if temp == "Red":
            RedPoints=RedPoints+9
            print(RedPoints)
        if temp == "Blue":
            BluePoints=BluePoints+9
        if temp == "Yellow":
            YellowPoints=YellowPoints+9
        if temp == "Green":
            GreenPoints=GreenPoints+9



    for i in SecondPlaces:
        temp=i
        if temp == "Red":
            RedPoints=RedPoints+6
            print(RedPoints)
        if temp == "Blue":
            BluePoints=BluePoints+6
        if temp == "Yellow":
            YellowPoints=YellowPoints+6
        if temp == "Green":
            GreenPoints=GreenPoints+6
                


    for i in ThirdPlaces:
        temp=i
        if temp == "Red":
            RedPoints=RedPoints+3
            print(RedPoints)
        if temp == "Blue":
            BluePoints=BluePoints+3
        if temp == "Yellow":
            YellowPoints=YellowPoints+3
        if temp == "Green":
            GreenPoints=GreenPoints+3
    FinalScores()



def FinalScores():
    Start.destroy()
    global tempvar
    tempvar=1
    for i in range (1,6):
        global scorething
        
        scorething=tk.Tk()
        #collegepic=PhotoImage(file = "college.png")
        #window77.iconphoto(False,collegepic)
        scorething.geometry=("1000x1000")
        #set the program title
        scorething.title("Final scores")
        #FinalPointsEnd=[RedPoints,BluePoints,YellowPoints,GreenPoints]
        #FinalPointsEnd.sort(reverse=True)
        actual22=tk.Label(scorething,text="Enter first name")
        actual22.pack()
        scorething.minsize(400, 200)
        #set maximum window size value
        scorething.maxsize(450, 300)
        global Indivplace
        Indivplace=StringVar()
        Indivplace.set("Choose individual winner")
        drop33 = OptionMenu(scorething,Indivplace,*IndividualList)
        drop33.pack(side=tk.TOP)
        enterButton = tk.Button(scorething,text="Submit Score",command=IndivScores,height=2,width=10,bg="#B0FC38")
        enterButton.pack(padx=50,pady=50)
        scorething.mainloop()
        tempvar=tempvar+1

    global ScoreDictionary
    ScoreDictionary = {'Red': RedPoints, 'Blue': BluePoints, 'Yellow': YellowPoints, 'Green': GreenPoints}
    global winner
    winner = max(ScoreDictionary, key=ScoreDictionary.get)
    FinalWindow()
    





    
def MainWindow():
    mainwindow=("69")
    global window
    window=tk.Tk()
    collegepic=PhotoImage(file = "college.png")
    #window.iconphoto(False,collegepic)
    window.geometry=("1000x1000")
    #set the program title
    window.title("Team Selector")
    # set minimum window size value
    #window.minsize(400, 200)
    # set maximum window size value
    #window.maxsize(450, 300)
    actual=tk.Label(text="Enter first name")
    actual.pack()

    #entry form for players name
    global name
    global var
    global variable
    name=tk.Entry()
    name.pack()




    var=IntVar()
    #choice for team
    label2 = tk.Radiobutton(
        text="Team",value=1,
        font="Verdana",
        variable=var
    )

    #choice for individual
    label3 = tk.Radiobutton(
        text="individual",value=2,
        font="Verdana",
        variable=var
    )


    label2.pack(padx=15,pady=20)
    label3.pack(padx=15,pady=20)


    enterButton = tk.Button(window, text="Enter",command=addplayer,height=2,width=10)
    #bg="#B0FC38")
    enterButton.pack(padx=15,pady=15)

    enterButton2 = tk.Button(window, text="Click when Finished adding players",command=StartEvent,height=2,width=30)
    #,bg="#82EEFD")
    #enterButton2.pack(padx=15,pady=15)

    enterButton3 = tk.Button(window, text="Import Data From File",command=GetScores,height=2,width=30)
    #,bg="#B584f4")
    #enterButton3.pack(padx=15,pady=15)
    window.mainloop()

def SubmitScores():
    if EventNumberLoop==1:
        FirstEventPlace=firstplace.get()
        Event1.append(FirstEventPlace)
        SecondEventPlace=secondplace.get()
        Event1.append(SecondEventPlace)
        ThirdEventPlace=thirdplace.get()
        Event1.append(ThirdEventPlace)

    elif EventNumberLoop==2:
        FirstEventPlace=firstplace.get()
        Event2.append(FirstEventPlace)
        SecondEventPlace=secondplace.get()
        Event2.append(SecondEventPlace)
        ThirdEventPlace=thirdplace.get()
        Event2.append(ThirdEventPlace)
    elif EventNumberLoop==3:
        FirstEventPlace=firstplace.get()
        Event3.append(FirstEventPlace)
        SecondEventPlace=secondplace.get()
        Event3.append(SecondEventPlace)
        ThirdEventPlace=thirdplace.get()
        Event3.append(ThirdEventPlace)
    elif EventNumberLoop==4:
        FirstEventPlace=firstplace.get()
        Event4.append(FirstEventPlace)
        SecondEventPlace=secondplace.get()
        Event4.append(SecondEventPlace)
        ThirdEventPlace=thirdplace.get()
        Event4.append(ThirdEventPlace)
    elif EventNumberLoop==5:
        FirstEventPlace=firstplace.get()
        Event5.append(FirstEventPlace)
        SecondEventPlace=secondplace.get()
        Event5.append(SecondEventPlace)
        ThirdEventPlace=thirdplace.get()
        Event5.append(ThirdEventPlace)
        PointsCalc()


        
    Start.destroy()
    
    #this closes the last scoring window to open the one for the next event
    
#This opens the team csv file and adds the data to the team variables inside the program
def GetScores():
    with open("NameList.csv","r") as OpenCSV:
        lis = [line.split() for line in OpenCSV]
        for i,x in enumerate(lis):
            if i==0 and x not in Red:   
                Red.append(x)
                print(Red)
            elif i==1 and x not in Blue:
                Blue.append(x)
            elif i==2 and x not in Yellow:
                Yellow.append(x)
            elif i==3 and x not in Green:
                Green.append(x)
            elif i==4 and x not in IndividualList:
                IndividualList.append(x)
        print(Red)

def WriteData():
    with open('NameList.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(Red)
        spamwriter.writerow(Blue)
        spamwriter.writerow(Yellow)
        spamwriter.writerow(Green)
        spamwriter.writerow(IndividualList)
        

def StartEvent():
       window.destroy()
       for i in range (1,6):
        global EventNumberLoop
        EventNumberLoop = i
        global Start
        Start=tk.Tk()
        Start.geometry=("400x400")
        #set the program title
        title=("Event",i,"Scores")
        Start.title(title)
         #set minimum window size value
        Start.minsize(400, 400)
         #set maximum window size value
        Start.maxsize(450, 2500)

        
        texting=tk.Label(Start,text="1st Place")
        texting.config(bg="gold")
        texting.pack(side=tk.TOP,pady=20)
        global firstplace
        firstplace=StringVar()
        firstplace.set("Choose team")
        drop = OptionMenu(Start,firstplace,*TeamList)
        drop.pack(side=tk.TOP )

        
        texting2=tk.Label(Start,text="2nd Place")
        texting2.config(bg="silver")
        texting2.pack(side=tk.TOP,pady=20)
        global secondplace
        secondplace=StringVar()
        secondplace.set("Choose team")
        drop2 = OptionMenu(Start,secondplace,*TeamList)
        drop2.pack(side=tk.TOP)


        texting3=tk.Label(Start,text="3rd Place")
        texting3.config(bg="#CD7F32")
        texting3.pack(side=tk.TOP,pady=20)
        global thirdplace
        thirdplace=StringVar()
        thirdplace.set("Choose team")
        drop3 = OptionMenu(Start,thirdplace,*TeamList)
        drop3.pack(side=tk.TOP)

        enterButton = tk.Button(Start,text="Submit Scores",command=SubmitScores,height=2,width=10,bg="#B0FC38")
        enterButton.pack(padx=50,pady=50)
        Start.mainloop()
    



            
def _msgBox():
    if PlayerType==1:
        tk.messagebox.showinfo(title="Player has been added",message=Name+" Has Been Added To The "+teams.get())
        window2.destroy()
        MainWindow()
    elif PlayerType==2:

        tk.messagebox.showinfo(title="Player has been added",message=Name+" Has Been Added To The Individuals List")
    #MainWindow()
def appendTeam():
    TeamChoice=teams.get()
    if TeamChoice=="Red Team" and len(Red)<5:
        Red.append(Name)
        WriteData()
        _msgBox()
    elif TeamChoice=="Blue Team"and len(Blue)<5:
        Blue.append(Name)
        WriteData()
        _msgBox()
    elif TeamChoice=="Yellow Team"and len(Yellow)<5:
        Yellow.append(Name)
        WriteData()
        _msgBox()
    elif TeamChoice=="Green Team"and len(Green)<5:
        Green.append(Name)
        WriteData()
        _msgBox()

    else:
         tk.messagebox.showinfo(title="The Team Is Full",message=Name+" Has  NOT Been Added  To The Team\nThe Team Is Full! ",icon="error")
         window2.destroy()
         MainWindow()
        

    
def addplayer():
    global Name

    Name=name.get()
    global PlayerType
    PlayerType=var.get()
    print(PlayerType)
    print(IndividualList)
    print(Name)
    print(PlayerType)
    if PlayerType==2:
        IndivLength=len(IndividualList)
        if IndivLength>20:
            tk.messagebox.showinfo(title="Individuals List Is Full",message=Name+" Has  NOT Been Added\n The Individual list Already Has \n20 Players",icon="error")
        else:
            
            IndividualList.append(Name)
            WriteData()
            _msgBox()
            #MainWindow()



    

    else:
        if mainwindow!=("69"):
            window.destroy()
        
        global window2
        window2=tk.Tk()
        window2.geometry=("400x400")
        #set the program title
        window2.title("Team Selector")
         #set minimum window size value
        window2.minsize(400, 200)
         #set maximum window size value
        window2.maxsize(450, 2500)
        actual=tk.Label(text="Select Correct Team")
        actual.pack()
        #entry form for Team name
        global teams
        teams=StringVar()
        teams.set("Choose Team")
        teamlist=["Red Team","Blue Team","Yellow Team","Green Team"]
        drop = OptionMenu(window2,teams,*teamlist)
        drop.pack()
        enterButton = tk.Button(window2,text="Enter",command=appendTeam,height=2,width=10,bg="#B0FC38")
        enterButton.pack(padx=15,pady=15)
        window2.mainloop()
   


def openwindow():
    window=tk.Tk()
    window.geometry=("400x400")
    #set the program title
    window.title("Team Selector")
    # set minimum window size value
    window.minsize(400, 200)
    # set maximum window size value
    window.maxsize(450, 2500)
    actual=tk.Label(text="Enter first name")
    actual.pack()

    #entry form for players name
    global name
    name=tk.Entry()
    name.pack()




    var=IntVar()
    #choice for team
    label2 = tk.Radiobutton(
        text="Team",value=1,
        font="Verdana",
        variable=var
    )

    #choice for individual
    label3 = tk.Radiobutton(
        text="individual",value=2,
        font="Verdana",
        variable=var
    )


    label2.pack(padx=15,pady=20)
    label3.pack(padx=15,pady=20)


    enterButton = tk.Button(window, text="Enter",command=addplayer,height=2,width=10,bg="#B0FC38")
    enterButton.pack(padx=15,pady=15)
MainWindow()
##window=tk.Tk()
##collegepic=PhotoImage(file = "college.png")
##window.iconphoto(False,collegepic)
##window.geometry=("1000x1000")
###set the program title
##window.title("Team Selector")
### set minimum window size value
###window.minsize(400, 200)
### set maximum window size value
###window.maxsize(450, 300)
##actual=tk.Label(text="Enter first name")
##actual.pack()
##
###entry form for players name
##name=tk.Entry()
##name.pack()
##
##
##
##
##var=IntVar()
###choice for team
##label2 = tk.Radiobutton(
##    text="Team",value=1,
##    font="Verdana",
##    variable=var
##)
##
###choice for individual
##label3 = tk.Radiobutton(
##    text="individual",value=2,
##    font="Verdana",
##    variable=var
##)
##
##
##label2.pack(padx=15,pady=20)
##label3.pack(padx=15,pady=20)
##
##
##enterButton = tk.Button(window, text="Enter",command=addplayer,height=2,width=10,bg="#B0FC38")
##enterButton.pack(padx=15,pady=15)
##
##enterButton2 = tk.Button(window, text="Click when Finished adding players",command=StartEvent,height=2,width=30,bg="#82EEFD")
##enterButton2.pack(padx=15,pady=15)
##
##enterButton3 = tk.Button(window, text="Import Data From File",command=GetScores,height=2,width=30,bg="#B584f4")
##enterButton3.pack(padx=15,pady=15)








