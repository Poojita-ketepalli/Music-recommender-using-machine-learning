import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from tkinter import *

music_data = pd.read_csv("music.csv")
X = music_data.drop(columns=['genre'])
y = music_data['genre']
model = DecisionTreeClassifier()
model.fit(X,y)

root = Tk()
root.geometry("300x300+100+100")
frame1 = Frame(root, width=300, height=300, relief=RIDGE)
frame1.place(x=0, y=0)
gender = StringVar()
age = StringVar()
gender_lbl = Label(frame1, text="Gender", font=("times new roman", 13), fg="black")
gender_lbl.place(x=20, y=30)
entry_gender = Entry(frame1, font=("times new roman", 13), fg="black", width=10, textvariable=gender)
entry_gender.place(x=90, y=30)
age_lbl = Label(frame1, text="Age", font=("times new roman", 13), fg="black")
age_lbl.place(x=20, y=70)
entry_age = Entry(frame1, font=("times new roman", 13), fg="black", width=10, textvariable=age)
entry_age.place(x=90, y=70)
answer = StringVar()
predict_entry = Entry(frame1, font=("times new roman", 13), fg="black", width=15, textvariable=answer)
predict_entry.place(x=100, y=150)


def prediction():
    if (gender.get() == "female"):
        g = 1
    else:
        g = 0
    predictions = model.predict([[int(age.get()), g]])
    answer.set(predictions[0])


predict_btn = Button(frame1, text="Predict", font=("times new roman", 13), fg="black", command=prediction)
predict_btn.place(x=20, y=150)

root.mainloop()
