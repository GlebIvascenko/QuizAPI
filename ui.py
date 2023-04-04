from tkinter import *
from quiz_brain import  QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=500, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(250, 125, width=480, text="QUIZ QueSTIONS", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        red_button_img = PhotoImage(file="images/false.png")
        self.red_button = Button(image=red_button_img, highlightthickness=0, command=self.set_False)
        self.red_button.grid(column=1, row=2)

        green_button_img = PhotoImage(file="images/true.png")
        self.green_button = Button(image=green_button_img, highlightthickness=0, command=self.set_True)
        self.green_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of your quiz.\n"
                                                            f" Your final Score: {self.quiz.score}")
            self.red_button.config(state="disabled")
            self.green_button.config(state="disabled")

    def set_True(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def set_False(self):
        #same as above
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

