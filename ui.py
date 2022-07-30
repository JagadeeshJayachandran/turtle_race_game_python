from tkinter import *
from quiz_brain import  QuizBrain
THEME_COLOR = "#375362"

WHITE = "#FAFAEB"

# wrong_img = PhotoImage(file='false.png')

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label(text="Score: ", fg=WHITE)
        self.score.grid(column=1, row=0)
        self.score.config(padx=20, pady=5)
        self.canvas = Canvas(width=300, height = 250, bg = WHITE)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",20, "italic"))
        self.canvas.grid(columnspan=2, row=1, pady=20)
        self.correct_img = PhotoImage(file='images/true.png')
        self.correct_button = Button(image=self.correct_img, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2 )
        self.correct_button.config(padx=20)
        self.false_img = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)
        self.wrong_button.config(padx=20)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Thats the end of the quiz")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")




    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)






