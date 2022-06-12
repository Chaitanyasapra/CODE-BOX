from cProfile import label
from tkinter import *
import datetime
root = Tk()
root.geometry("1000x750")
root.resizable(0,0)
root.title(" QUIZ TIME ---- MADE BY CHAITANYA SAPRA ")
root.iconbitmap('C:/Users/Chaitanya/Desktop/python project folder/icon.ico')
bg = PhotoImage(file="C:/Users/Chaitanya/Desktop/python project folder/background 1.png")

Canvas1 = Canvas(root, width=1000, height=750)
Canvas1.pack(fill="both", expand=True)
Canvas1.create_image(0, 0, image=bg, anchor = "nw")

pass_c1= open("C:/Users/CHAITANYA/Desktop/python project folder/PASS CODE.txt")
pass_code = pass_c1.read()
pass_c1.close()

global questions
global answers
global options
global user_answers
global mark_ques

user_answers =[]
mark_ques = []
enter1=open("C:/Users/CHAITANYA/Desktop/python project folder/ENTRY.txt")
entery1=list(enter1.read().split("\n"))
enter1.close()
questions=list(entery1[0].split(", "))
options=list(entery1[1].split(", "))
answers=list(entery1[2].split(", "))
ques_no=0
score=0
check=0                

def check1():
    global check
    check=1
    Label_pin= Label(root, text="Enter PASS CODE HERE ",font='bold',bg="white")
    Label_pin.place(x=392, y=30)
    pin_e = Entry(root, bg="#000080",fg="white",font='bold')
    pin_e.place(x=404, y=80)
    pin_b= Button(root, text="ENTER PASS CODE",bg="black",fg="white",font='bold',command= lambda:[pin_func()])
    pin_b.place(x=400, y=330)
    ab['state'] = DISABLED
    start_button['state'] = DISABLED
    def pin_func():
        if pin_e.get() == pass_code:
         Label_pin.destroy()
         pin_e.destroy()
         pin_b.destroy()
         admin()
        else:
         Label_pin.destroy()
         pin_e.destroy()
         pin_b.destroy()
         ab['state'] = NORMAL
         start_button['state'] = NORMAL

def admin():
      
    def submit():
        global questions
        global answers
        global options
        questions=i.get().split(sep=", ")
        answers=o.get().split(sep=", ")
        options=i2.get().split(sep=", ")
        i.destroy(), o.destroy(), sb.destroy(), i2.destroy()
        ab['state'] = NORMAL
        start_button['state'] = NORMAL

        
    if check==1:
        
        Label1= Label(root, text="Enter All Questions Here, Separate Every Question By (, ) ",font='bold',bg="white")
        Label1.place(x=302, y=30)

        i = Entry(root, bg="#000080",fg="white",font='bold')
        i.place(x=404, y=80)
        
        Label_options = Label(root, text="Enter All Set Of Options Here, Separate Every Set Of Option By (, ) ",font='bold',bg="white")
        Label_options.place(x=277, y=130)

        i2 = Entry(root, bg="#000080",fg="white",font='bold')
        i2.place(x=404, y=180)

        Label2 = Label(root, text="Enter All Answers Here, Separate Every Answer By (, ) ",font='bold',bg="white")
        Label2.place(x=302, y=230)
        
        o = Entry(root, bg="#000080", fg="white", text="(a)",font='bold')
        o.place(x=404, y=280)
        

        sb= Button(root, text="SUBMIT",bg="black",fg="white",font='bold',command= lambda:[Label1.destroy(),Label2.destroy(),Label_options.destroy(),submit()])
        sb.place(x=462, y=330)

def mark_button_func():
    global marked_quetion
    global unmark_button
    global mark_button
    global marked_quetion
    mark_ques[ques_no]="x"
    marked_quetion = Label(root, text="You Have Marked This Question",font="bold", bg="#4A148C", fg="white")
    marked_quetion.place(x=25, y=18)
    unmark_button["state"]=NORMAL
    mark_button["state"]=DISABLED

def unmark_button_func():
    global marked_quetion
    global unmark_button
    global mark_button
    global marked_quetion
    mark_ques[ques_no]=0
    marked_quetion.destroy()

    unmark_button["state"]=DISABLED
    mark_button["state"]=NORMAL

def start():

    global score
    global ques_no
    global ques_label
    global opt_label
    global answers_entry
    global current_ques_label
    global mark_ques
    ques_no=0
    score=0
    global user_answers
    global mark_ques_label
    global marked_quetion
    global unmark_button
    global mark_button
    global start_time
    start_time = datetime.datetime.now()
    marked_quetion = Label(root, text="You Have Marked This Question",font="bold", bg="#4A148C", fg="white")
    marked_quetion.place(x=25, y=18)   
    marked_quetion.destroy()
    user_answers =[0 for i in range(len(questions))]
    mark_ques = [0 for i in range(len(questions))]
    ques_label= Label(root, text=questions[0],bg="#00FFFF",fg="#000000",font='bold')
    ques_label.place(x=270, y=275)
    opt_label= Label(root, text=options[0],bg="#00FFFF",fg="#000000",font='bold')
    opt_label.place(x=270, y=300)
    total_ques_label= Label(root, text=f"The Total NO. of Questions are {len(questions)} ",font='bold')
    total_ques_label.place(x=600, y=20)
    current_ques_label= Label(root, text=f"You are on Question NO. {(ques_no)+1}",font='bold')
    current_ques_label.place(x=600, y= 60)
    answers_entry= Entry(root, bg="#FFFF00",font='bold')
    answers_entry.place(x=380, y=329)
    mark_button = Button(root, text="Mark", bg="green",font="bold", fg="white",command= lambda:[mark_button_func()])
    mark_button.place(x=25, y=50)
    unmark_button = Button(root, text="Unmark", bg="green",font="bold", fg="white",command= lambda:[unmark_button_func()])
    unmark_button.place(x= 25, y=92)    
    
    if user_answers[ques_no] == 0:
        mark_ques_label = Label(root, text="You have not answered this Question",font="bold")
        mark_ques_label.place(x=600, y=100)
    if user_answers[ques_no] != 0:
        str1=str(user_answers[ques_no])
        mark_ques_label = Label(root, text=f"You have answered this Question, "+str1+" ", font="bold")
        mark_ques_label.place(x=600, y=100)
    
    if mark_ques[ques_no] == 0:
        mark_button["state"] = NORMAL
        unmark_button['state'] = DISABLED

    if mark_ques[ques_no] != 0:
        marked_quetion = Label(root, text="You Have Marked This Question",font="bold", bg="#4A148C", fg="white")
        marked_quetion.place(x=25, y=18)
        mark_button["state"] = DISABLED
        unmark_button['state'] = NORMAL

    

    def next_question():
        global score
        global ques_no
        global ques_label
        global opt_label
        global answers_entry
        global current_ques_label
        global mark_ques_label
        mark_ques_label.destroy()
        global marked_quetion
        marked_quetion.destroy()
        
        print(ques_no)
        ques_no = ques_no + 1
        current_ques_label.destroy()
        
        if ques_no==(len(questions)-1):
            next_question_button["state"]=DISABLED
                        
        if ques_no>0:
            ques_label= Label(root, text=questions[ques_no],bg="#00FFFF",fg="#000000",font='bold')
            ques_label.place(x=270, y=275)
            opt_label= Label(root, text=options[ques_no],bg="#00FFFF",fg="#000000",font='bold')
            opt_label.place(x=270, y=300)
            answers_entry= Entry(root, bg="#FFFF00",font='bold')
            answers_entry.place(x=380, y=329)

        if user_answers[ques_no] == 0:
            mark_ques_label = Label(root, text="You have not answered this Question",font="bold")
            mark_ques_label.place(x=600, y=100)
        if user_answers[ques_no] != 0:
            str1=str(user_answers[ques_no])
            mark_ques_label = Label(root, text=f"You have answered this Question, "+str1+" ", font="bold")
            mark_ques_label.place(x=600, y=100)    

        if mark_ques[ques_no] == 0:
            mark_button["state"] = NORMAL
            unmark_button['state'] = DISABLED

        if mark_ques[ques_no] != 0:
            marked_quetion = Label(root, text="You Have Marked This Question",font="bold", bg="#4A148C", fg="white")
            marked_quetion.place(x=25, y=18)
            mark_button["state"] = DISABLED
            unmark_button['state'] = NORMAL       



        current_ques_label= Label(root, text=f"You are on Question NO. {(ques_no)+1}",font='bold')
        current_ques_label.place(x=600, y= 60)
           
        
        select_ans_button['state']=NORMAL
        #next_question_button['state']= DISABLED
        Last_question_button["state"]= NORMAL
        
    
    def select_ans():
        global ques_no
        
        global score

        global mark_ques_label
        mark_ques_label.destroy()
        
        ans=answers_entry.get()
        
        user_answers[(ques_no)] = ans
        if user_answers[ques_no] == 0:
            mark_ques_label = Label(root, text="You have not answered this Question",font="bold")
            mark_ques_label.place(x=600, y=100)
        if user_answers[ques_no] != 0:
            str1=str(user_answers[ques_no])
            mark_ques_label = Label(root, text=f"You have answered this Question, "+str1+" ", font="bold")
            mark_ques_label.place(x=600, y=100)
        print(user_answers)

    
    def Last_question():
        global score
        global ques_no
        global ques_label
        global opt_label
        global answers_entry
        global current_ques_label
        global mark_ques_label
        global marked_quetion
        marked_quetion.destroy()
        mark_ques_label.destroy()
        print(ques_no)
        ques_no = ques_no - 1
        current_ques_label.destroy()
        
        if ques_no== 0:
            Last_question_button['state'] = DISABLED
            
        ques_label= Label(root, text=questions[ques_no],bg="#00FFFF",fg="#000000",font='bold')
        ques_label.place(x=270, y=275)
        opt_label= Label(root, text=options[ques_no],bg="#00FFFF",fg="#000000",font='bold')
        opt_label.place(x=270, y=300)
        answers_entry= Entry(root, bg="#FFFF00",font='bold')
        answers_entry.place(x=380, y=329)
        if user_answers[ques_no] == 0:
            mark_ques_label = Label(root, text="You have not answered this Question",font="bold")
            mark_ques_label.place(x=600, y=100)
        if user_answers[ques_no] != 0:
            str1=str(user_answers[ques_no])
            mark_ques_label = Label(root, text=f"You have answered this Question, "+str1+" ", font="bold")
            mark_ques_label.place(x=600, y=100)

        if mark_ques[ques_no] == 0:
            mark_button["state"] = NORMAL
            unmark_button['state'] = DISABLED

        if mark_ques[ques_no] != 0:
            marked_quetion = Label(root, text="You Have Marked This Question",font="bold", bg="#4A148C", fg="white")
            marked_quetion.place(x=25, y=18)
            mark_button["state"] = DISABLED
            unmark_button['state'] = NORMAL    
        
        current_ques_label= Label(root, text=f"You are on Question NO. {(ques_no)+1}",font='bold')
        current_ques_label.place(x=600, y= 60)
        
        select_ans_button['state']=NORMAL
        next_question_button['state']= NORMAL       
    
    def End_test():
        End_test_button["state"]=DISABLED
        next_question_button["state"]=DISABLED
        Last_question_button["state"]=DISABLED
        select_ans_button["state"]=DISABLED
        change_ques_button["state"]=DISABLED
        ques_left=0
        for i in range(len(questions)):
            if user_answers[i] == 0:
                ques_left = ques_left + 1

        new_label= Label(root, text=f"Are sure you that you want to SUBMIT your TEST ??? {ques_left} Questions are left",bg="black",fg="white", font="bold")
        new_label.place(x=180, y=500)
        c_yes_button=Button(root, text="YES", font="bold",bg="black",fg="white", command= lambda:[c_yes()])
        c_yes_button.place(x= 350, y = 600)
        
        c_no_button=Button(root, text="NO", font="bold",bg="black",fg="white", command= lambda:[c_no()])
        c_no_button.place(x= 550, y = 600)

        def c_yes():
            score = 0
            next_question_button.destroy()
            select_ans_button.destroy()
            Last_question_button.destroy()
            ques_label.destroy()
            opt_label.destroy()
            answers_entry.destroy()
            total_ques_label.destroy()
            current_ques_label.destroy()
            new_label.destroy()
            End_test_button.destroy()
            c_yes_button.destroy()
            c_no_button.destroy()
            mark_ques_label.destroy()
            marked_quetion.destroy()
            mark_button.destroy()
            unmark_button.destroy()
            change_ques_button.destroy()
            right_now = datetime.datetime.now()
            global start_time
            time_taken = right_now - start_time
            for i in range(len(questions)):
                if user_answers[i] == answers[i]:
                    score = score + 1
            print(score)
            
            score_label= Label(text=f"THE QUIZ IS OVER YOU SCORED {score}/{len(questions)}, {((score)/(len(questions)))*(100)}%",bg="#33ff00",fg="white",font='bold')
            score_label.place(x=295, y=395)
            
            per_c = (((score)/(len(questions)))*(100))
            if per_c<= 50:
                score_label_2 = Label(text="THERE IS STILL HOPE! YOU CAN DO IT ! NEVER GIVE UP",bg="#33ff00",fg="white",font='bold')
                score_label_2.place(x=235, y=420)
            
            elif per_c > 50 and per_c<=70:
                score_label_2 = Label(text="YOU GOT POTENTIAL ! YOU CAN IMPROVE ! ",bg="#33ff00",fg="white",font='bold')
                score_label_2.place(x=295, y=420)
            
            elif per_c > 70 and per_c<90:
                score_label_2 = Label(text="KEEP UP THE GOOD WORK!",bg="#33ff00",fg="white",font='bold')
                score_label_2.place(x=380, y=420)
            
            elif per_c>= 90 and per_c<100:
                score_label_2 = Label(text="WOW YOU ARE GOOD!",bg="#33ff00",fg="white",font='bold')
                score_label_2.place(x=400, y=420)

            elif per_c == 100:
                score_label_2 = Label(text="PERFECT",bg="#33ff00",fg="white",font='bold')
                score_label_2.place(x=460, y=420)        

            f1=open("C:/Users/CHAITANYA/Desktop/python project folder/Test_History.txt","a")
            f1.write(f"\nTime of Starting the test was: {start_time}\nTime of Submission of Test: {right_now} \nTotal Time Taken: {time_taken}\nThe marks obtained were: {score}/{len(questions)}\nThe percentage of the marks was: {per_c}\nThe Question were: {questions} \nThe options Given were: {options}\nThe correct answers were: {answers} \nThe answers given were: {user_answers}\n")
            f1.close()
            
            print(user_answers)
            
            
        
        def c_no():
            global ques_no
            global questions
            End_test_button["state"]=NORMAL
            next_question_button["state"]=NORMAL
            Last_question_button["state"]=NORMAL
            select_ans_button["state"]=NORMAL
            change_ques_button["state"]=NORMAL
            new_label.destroy()
            c_yes_button.destroy()
            c_no_button.destroy()
            if ques_no == 0:
                Last_question_button["state"]=DISABLED
           
            if ques_no == ((len(questions))-1):
                next_question_button["state"]=DISABLED
        
    
    def change_ques():
        print(ques_no)
        change_ques_button["state"]=DISABLED
        global change_ques_label
        change_ques_label =Label(root, text="ENTER QUESTION NUMBER BELOW",bg="black",fg="white",font="bold")
        change_ques_label.place(x=289, y=500)
        change_ques_entry = Entry(root,font="bold")
        change_ques_entry.place(x=350, y=530)
        End_test_button["state"]=DISABLED
        Last_question_button["state"]=DISABLED
        End_test_button["state"]=DISABLED
        select_ans_button["state"]=DISABLED
        next_question_button["state"]=DISABLED
        def change_ques_y_func():
            try:
                
                print()
                global score
                global ques_no
                global ques_label
                global opt_label
                global answers_entry
                global current_ques_label
                global mark_ques_label
                mark_ques_label.destroy()
                global marked_quetion
                marked_quetion.destroy()
                
                
                print(ques_no)
                
                current_ques_label.destroy()
                
                ques_no= (int(change_ques_entry.get())-1)
                if ques_no<0:
                    ques_no=0
                if ques_no >=(len(questions)):
                    ques_no=((len(questions)-1))

                                
                
                ques_label= Label(root, text=questions[ques_no],bg="#00FFFF",fg="#000000",font='bold')
                ques_label.place(x=270, y=275)
                opt_label= Label(root, text=options[ques_no],bg="#00FFFF",fg="#000000",font='bold')
                opt_label.place(x=270, y=300)
                answers_entry= Entry(root, bg="#FFFF00",font='bold')
                answers_entry.place(x=380, y=329)

                if user_answers[ques_no] == 0:
                    mark_ques_label = Label(root, text="You have not answered this Question",font="bold")
                    mark_ques_label.place(x=600, y=100)
                if user_answers[ques_no] != 0:
                    str1=str(user_answers[ques_no])
                    mark_ques_label = Label(root, text=f"You have answered this Question, "+str1+" ", font="bold")
                    mark_ques_label.place(x=600, y=100)    

                if mark_ques[ques_no] == 0:
                    mark_button["state"] = NORMAL
                    unmark_button['state'] = DISABLED

                if mark_ques[ques_no] != 0:
                    
                    marked_quetion = Label(root, text="You Have Marked This Question",font="bold", bg="#4A148C", fg="white")
                    marked_quetion.place(x=25, y=18)
                    mark_button["state"] = DISABLED
                    unmark_button['state'] = NORMAL       



                current_ques_label= Label(root, text=f"You are on Question NO. {(ques_no)+1}",font='bold')
                current_ques_label.place(x=600, y= 60)
                
                
                select_ans_button['state']=NORMAL
                next_question_button['state']= NORMAL
                Last_question_button["state"]= NORMAL
                if ques_no==0:
                    Last_question_button["state"]= DISABLED
                if ques_no==((len(questions))-1):
                    next_question_button['state']= DISABLED
                
                change_ques_y.destroy()
                change_ques_n.destroy()
                change_ques_entry.destroy()
                change_ques_button['state']=NORMAL
                End_test_button["state"]=NORMAL

            except:
                global change_ques_label
                mark_button["state"] = DISABLED
                unmark_button['state'] = DISABLED
                change_ques_n["state"] = DISABLED
                change_ques_label.destroy()
                change_ques_label =Label(root, text="INVALID INPUT! PLEASE PUT IN A NUMBER",bg="black",fg="white",font="bold")
                change_ques_label.place(x=261, y=500)

        def  change_ques_n_func():
            
            change_ques_button["state"]=NORMAL
            End_test_button["state"]=NORMAL
            select_ans_button['state']=NORMAL
            next_question_button['state']= NORMAL
            Last_question_button["state"]= NORMAL
            if ques_no==0:
                Last_question_button["state"]= DISABLED
            if ques_no==((len(questions))-1):
                next_question_button['state']= DISABLED
            change_ques_entry.destroy()
            change_ques_y.destroy()
            change_ques_n.destroy()
                  
                
        change_ques_y = Button(root,text="Move to that Question",bg="black",fg="white",font="bold",command=lambda:[opt_label.destroy(),ques_label.destroy(),answers_entry.destroy(),change_ques_label.destroy(),change_ques_y_func()])
        change_ques_y.place(x=250, y=650)
        change_ques_n = Button(root, text="Stop",font="bold",bg="black",fg="white",command=lambda:[change_ques_label.destroy(),change_ques_n_func()])
        change_ques_n.place(x=600, y=650)


    start_button.destroy()
    ab.destroy()

    next_question_button = Button(root, text="NEXT QUESTION",bg="#33ff00",fg="white",font='bold', command=lambda:[opt_label.destroy(),ques_label.destroy(),answers_entry.destroy(),next_question()])
    
    next_question_button.place(x=750, y=395)       
    
    select_ans_button= Button(root, text="SELECT ANSWER",bg="#33ff00",fg="white",font='bold', command=select_ans)
    
    select_ans_button.place(x=400, y=395)

    Last_question_button = Button(root, text="LAST QUESTION",bg="#33ff00",fg="white",font='bold', command=lambda:[opt_label.destroy(),ques_label.destroy(),answers_entry.destroy(),Last_question()])
    
    Last_question_button.place(x=70, y= 395)

    End_test_button = Button(root, text="SUBMIT TEST",bg="green",fg="white",font='bold', command=lambda:[End_test()])
    
    End_test_button.place(x=25, y= 600)

    change_ques_button = Button(root, text="CHANGE QUESTION",bg="green",fg="white",font='bold', command=lambda:[change_ques()])
    
    change_ques_button.place(x=770, y= 600) 
    select_ans_button['state']=NORMAL
    next_question_button['state']= NORMAL
    Last_question_button["state"]= NORMAL
    if ques_no==0:
        Last_question_button["state"]= DISABLED
    if ques_no==((len(questions))-1):
        next_question_button['state']= DISABLED

ab=Button(root, text="ADMIN",bg="green",fg="white",font='bold',command=lambda:[check1()])
ab.place(x=25,y=600)
start_button= Button(root, text="START",bg="#33ff00",fg="white",font='bold', command= lambda:[start()])
start_button.place(x=462, y=395)
root.mainloop()