from tkinter import *
from quizbrain import QuizBrain

THEME_COLOR = "#375362"






class QuizInterface(Label):
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz Game')
        self.window.config(padx=50, pady=50, background=THEME_COLOR)
        self.score_label = Label(text='score = 0', fg='white',background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=250,
                                                     text="some text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     )
        self.canvas.grid(row=1, column=2, columnspan=2, pady=50)
        true = PhotoImage(file="/Users/james/Desktop/true.png")
        self.true_button = Button(image=true, highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_button = PhotoImage(file="/Users/james/Desktop/false.png")
        self.false_button = Button(image=false_button, highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f"Your score {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)















# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=400, height=500)
#
#
# question = Label(text='hey there traveler', width=5, height=5)
# question.grid(row=0, column=0)


# true_button = Button(text='helloo', width=5, height=5)
# true_button.grid(row=2, column=0)
#
# false_button = Button(text='helloo', width=5, height=5)
# false_button.grid(row=2, column=1)
#
#
#
#
#
# window.mainloop()
