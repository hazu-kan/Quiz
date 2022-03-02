from tkinter import *

names = [] 
global questions_answers
asked=[]
score=0
class QuizStarter:
  def __init__(self, parent): 

    background_color="light blue"

    self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)

    self.quiz_frame.grid()

    self.heading_label=Label(self.quiz_frame, text="NZ Road Rules", font= ("Tw Cen Mt","18","bold"),bg=background_color)
    self.heading_label.grid(row=0, padx=20)

    self.var1=IntVar()

    self.user_label=Label(self.quiz_frame, text="Please enter your username below:", font=("Tw Cen Mt","16"),bg=background_color)
    self.user_label.grid(row=1, padx=20, pady=20)

    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=2,padx=20, pady=20)

    self.continue_button=Button(self.quiz_frame, text="Continue", font=("Helvetia", "13", "bold"), bg="orange", command=self.name_collection)
    self.continue_button.grid(row=3, padx=20, pady=20)

    

  def name_collection(self):
    name=self.entry_box.get()
    names.append(name)
    self.quiz_frame.destroy()

questions_answers = {
  1: []

  
}

def randomiser (): 

  global qnum 
  qnum=random.radint(1,10)

  if qnum not in asked: 
    asked.append(qnum)

  elif qnum in asked:
    randomiser()

randomiser()

if __name__ == "__main__" :
  root = Tk()
  root.title("NZ Road Rules Quiz")
  quiz_instance = QuizStarter(root)
  root.mainloop()

