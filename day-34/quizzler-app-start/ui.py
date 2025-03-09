from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = 'Arial'




class User_interface():
    def __init__(self,quiz_brain:QuizBrain):

        #Window
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("You have been Quized")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0",highlightthickness=0,bg=THEME_COLOR,fg='white')
        self.score_label.grid(row=0,column=1,pady=20)

        #Canvas
        self.canvas = Canvas(height=250,width=300,bg='white')
        self.canvas.grid(row=1,column=0,columnspan=2,)
        self.question_text = self.canvas.create_text(150,125,text="WOW",fill='black',font=(FONT,20,'italic'),width=280)

        #Button images
        tick_img = PhotoImage(file='images/true.png')
        cross_img = PhotoImage(file='images/false.png')
        #Button
        self.tick_button = Button(image=tick_img,highlightthickness=0,bg=THEME_COLOR,command=self.true_check)
        self.tick_button.grid(row=2,column=0,pady=30)

        self.wrong_button = Button(image=cross_img,highlightthickness=0,bg=THEME_COLOR,command=self.false_check)
        self.wrong_button.grid(row=2,column=1,pady=30)
        
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end,Score: {self.quiz.score}")
            self.tick_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def true_check(self):
        is_right = self.quiz.check_answer( 'True')
        self.feedback(is_right)

    def false_check(self):
        is_right= self.quiz.check_answer('False')
        self.feedback(is_right)

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.window.after(500,self.get_next_question)
          
            # self.canvas.config(bg='white')
        else:
            self.canvas.config(bg='red')
            self.window.after(500,self.get_next_question)



