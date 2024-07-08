from tkinter import *
from tkinter import messagebox as msgbox
import json

class pyquiz:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.option_selected = IntVar()
        self.options = self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size = len(question)
        self.correct = 0
        self.feedback_label = Label(gui, text="", font=('ariel', 16), wraplength=600, justify='left',fg="green")
        self.feedback_label.place(x=70, y=600)

    def display_title(self):
        title = Label(gui, text="The GK quiz", width=35, fg="blue", font=("algerian", 55, "bold", "underline"))
        title.place(x=0, y=5)

    def display_question(self):
        q_no = Label(gui, text=question[self.q_no], width=60, font=('ariel', 25, 'bold'), anchor='w')
        q_no.place(x=100, y=150)
    
    def radio_buttons(self):
        q_list = []
        y_pos = 210
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.option_selected, value=len(q_list)+1, font=('ariel', 16))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 60
        return q_list
    
    def display_options(self):
        val = 0
        self.option_selected.set(0)
        for option in options[self.q_no]:
            self.options[val]['text'] = option
            val += 1

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn, width=10, bg="green", fg="black", font=("ariel", 16, "bold"))
        next_button.place(x=350, y=480)
        check_button = Button(gui, text="Check", command=self.check_btn, width=10, bg="yellow", fg="black", font=("ariel", 16, "bold"))
        check_button.place(x=100, y=480)
        self.quit_button = Button(gui, text="Quit", command=gui.destroy, width=10, bg="black", fg="white", font=("ariel", 16, "bold"))
        self.quit_button.place(x=950, y=480)

    def check_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
            self.display_feedback("Correct Answer!\nScore = 1", "green")
        else:
            correct_answer = options[self.q_no][answer[self.q_no] - 1]
            self.display_feedback(f"Incorrect Answer!\nCorrect Answer: {correct_answer}\nScore = 0", "red")

    def next_btn(self):
        self.q_no += 1
        if self.q_no == self.data_size:
            self.display_result()
            gui.destroy()
        else:
            self.display_question()
            self.display_options()

    def check_ans(self, q_no):
        if self.option_selected.get() == answer[q_no]:
            return True
        return False

    def display_feedback(self, message, color):
        self.feedback_label.config(text=message, fg=color)

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        msgbox.showinfo("Result", f"{result}\n{correct}\n{wrong}")

gui = Tk()
gui.geometry("1200x600")
gui.title("GK quiz")


with open('gkquiz.json') as f:
    data = json.load(f)
question = data['question']
options = data['options']
answer = data['answer']

quiz = pyquiz()

gui.mainloop()