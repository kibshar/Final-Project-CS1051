import tkinter

from tkinter import *
import random
ResponsesToHello=('Hello', 'Wassup','Whats cooking good lookin','Hola','Insert Generic Greeting Here','おはようございます','Hey')
wordsbotknows=()
def module1():
    pass
def module2():
    pass
def module3():
    pass
def module4():
    pass
def module5():
    pass
def module6():
    pass
#Basic Chatbot GUI taken & Modified from https://data-flair.training/blogs/python-chatbot-project/
#From base, I changed fonts, title, name of bot, some colors, all the responses are made by me

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg == 'hello' or msg=="Hello"or msg=="Hey"or msg=="Hi"or msg=="Heyo"or msg=="hey"or msg=="hi":
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = random.choice(ResponsesToHello)
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'start' or msg=='Start':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = "BEEP-BOOP Hello! I am Professor Rosen Bot I Teach Python. To begin your Python learning journey choose one of the modules below"
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n' + "Module 1:Downloading Python"+ '\n' + "Module 2:For Loops" + '\n'+ "Module 3: If Statements" +'\n'+"Module 4:Turtles"+'\n'+"Module 5:RegEX"+'\n'+"Module 6:TBD"+'\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'Module 1' or msg=="m1" or msg=='module 1' or msg== 'M1':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+"Welcome to Module 1: downloading Python"+'\n'+ "to download python go to https://www.python.org/" +'\n'+'Now click on downloads, it will detect your os automatically so just click the link that says download python version x.x.x')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m1 q1 Did you manage to successfully download python?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm1 q1 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('Congratulations! You are on'+'\n'+ 'your first step towards becoming a programmer. We will be using IDLE which comes preinstalled with'+'\n'+ 'python to code, to open IDLE simply search for IDLE in your search bar at the bottom left of your screen" ')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m1 q2 Were you able to open IDLE?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm1 q2 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('IDLE is a text editor and an example of an integrated development environment for our purposes the basics you should know is that to run a script which is what we will be doing primarily you need to press file, new file, and the resulting window will be where the coding will happen')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'Module 1 Complete please move on to module 2')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'Module 2' or msg=="m2" or msg=='module 2' or msg== 'M2':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+"Welcome to Module 2: For Loops"+'\n'+'A for loop is a control structure in python used to'+'\n'+ 'execute a program nonlinearly'+'\n'+'Instead of evaluating the code line by line until it'+'\n' +'reaches the end, once the program reaches a for'+'\n'+' loop, it will tell the program to execute a set of lines repeatedly. After doing all that, the program will then continue to evaluate and execute whatever is below the for loop')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+' m2 q1 Make Sense So far?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm2 q1 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'Good! To create a for loop in python the syntax is as  follows'+'\n'+'for i in range(10):'+'\n'+'      print("hello")')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'This would print out the world Hello 10 times, each     Hello would be on a separate line'+ '\n\n' + 'm2 q2 make sense so far?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm2 q2 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'Essentially you to create a for loop you need to put for (some variable) in range(some number):'+'\n'+'This for loop will repeat for as many times as you specify, but there are other types of for loops as well')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m2 q3 continue?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

    if msg == 'm2 q3 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'We can also use for loops to iterate through a list or even a string for example if x=apple and I were to write the code for i in x:' +'\n' +'      print(i)')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m2 q4 what would happen? try it out and type continue if you wanna know the answer')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm2 q4 continue':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'What happens is that each letter in the word apple      would be printed on a different line in the correct order, so as you can see for loops can also be used to iterate through a string or list. Another type of loop we are going to talk about is the while loop')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m2 q5 ready to keep going?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm2 q5 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'A while loop is like a for loop in the sense that it can be used to repeat the same code repeatedly, except a while loop can be used to create infinite loops or loops that continue until a task is done. For example if I were to write x=10'+'\n'+'while x=10:'+'\n'+'      print(Hi) '+'\n'+'the word hi would be printed infinitely since x will always equal 10')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'That concludes module 2 please move on to module 3')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'Module 3' or msg=="m3" or msg=='module 3' or msg== 'M3':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+"Welcome to Module 3: If Statements"+'\n'+'Before we talk about if statements its important to talk about boolean expressions which is the basis for all computer arithmetic. There are two boolean values True and False, and for boolean expressions or otherwise to determine if something is true or false you use the operator == so if we want to know if 5 is equal to 6 we would type 5==6')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m3 q1 That covers boolean expressions ready to keep going?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm3 q1 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'if statements are also called selection statements or conditional statements they are useful for binary selection if there are two possible paths for execution'+'\n'+'For example if i want to create a script that will tell me if a number is even or odd I could use an if statement')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m3 q2 In the next part I will give some sample code for an if statement, ready to continue?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm3 q2 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'x=15'+'\n'+'if x % 2 == 0:'+'\n'+'      print(x, "is even")'+'\n'+' else:'+'\n'+'      print(x, "is odd")'+'\n'+'This is an example of an if statement that will determine whether x is even or odd. As you can see if statements are useful for binary paths and the syntax requires if and an else followed by a colon and indent')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'This concludes module 3 and please continue on to module 4')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'Module 4' or msg=="m4" or msg=='module 4' or msg== 'M4':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'Welcome to Module 4 Turtles, in python there is a module called turtle that can be used to draw pictures. Turtle graphics, as it is known, is based on a very simple metaphor. Imagine that you have a turtle that understands English. You can tell your turtle to do simple commands such as go forward and turn right. As the turtle moves around, if its tail is down touching the ground, it will draw a line (leave a trail behind) as it moves. If you tell your turtle to lift up its tail it can still move around but will not leave a trail. As you will see, you can make some pretty amazing drawings with this simple capability')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m4 q1 make sense so far?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm4 q1 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'sample code for creating a turtle is as follows'+'\n'+'wn=turtle.Screen()'+'\n'+'bob=turtle.Turtle()'+'\n'+'bob.forward(90)'+'\n'+'bob.left(90)'+'\n'+'bob.forward(75)')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m4 q2 try running this script on your own, when done type done')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm4 q2 done':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'Here are a couple of things you’ll need to understand about this program. The first line tells Python to load a module named turtle. That module brings us two new types that we can use: the Turtle type, and the Screen type. The dot notation turtle.Turtle means “The Turtle type that is defined within the turtle module”. (Remember that Python is case sensitive, so the module name, turtle, with a lowercase t, is different from the type Turtle because of the uppercase T.) We then create and open what the turtle module calls a screen (we would prefer to call it a window, or in the case of this web version of Python simply a canvas), which we assign to variable wn. Every window contains a canvas, which is the area inside the window on which we can draw. In line 3 we create a turtle. The variable bob is made to refer to this turtle. These first three lines set us up so that we are ready to do some drawing. In lines 4-6, we instruct the object bob to move and to turn. We do this by invoking or activating bob’s methods — these are the instructions that all turtles know how to respond to.')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'That concludes module 4 move on to module 5')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        #Explanation of turtle example taken from runestone and modified slightly
    if msg == 'Module 5' or msg=="m5" or msg=='module 5' or msg== 'M5':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'Welcome to module 5 where we are going to talk about regular expressions, also sometimes called rational expressoins they are used to define a search pattern generally in a string. Essentially its a find and replace operation. In python the re module is used for regular expressions')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m5 q1 Ready to keep going?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm5 q1 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'python has 2 different operations based on regex matching and searching they differ in that match checks for a match at the beginning of a string while search checks for a match anywhere in the string the syntax is as follows for the match function re.match(pattern,string,flags=0) for the search function it is re.search(pattern,string,flags=0')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'m5 q2 That covers the basic syntax ready for an example?')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'm5 q2 yes':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'import re'+'\n'+'x=cats are smarter than dogs'+'\n'+'match=re.match(r(.*)are(.*?).*,x,re.M|re.I'+'\n'+'print (match.group(2))')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n'+'The resulting output should give you "smarter", that concludes module 5 you should be able to use regular expressions based off that example')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    if msg == 'Module 6' or msg=="m6" or msg=='module 6' or msg== 'M6':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("arial", 12 ))
        res = ('\n'+'This module does not exist yet, but is a work in progress')
        ChatLog.insert(END, "Professor Rosen Bot: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
base = Tk()
base.title("Professor Rosen Bot v1.2")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)
#Code for Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font=("Times New Roman",20))
ChatLog.config(state=DISABLED)
#code for getting scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
#Button Code
SendButton = Button(base, font=("Times New Roman",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )
#Code for Box
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font=("Times New Roman",20))
#EntryBox.bind("<Return>", send)
#Screen Placements
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)
base.mainloop()


