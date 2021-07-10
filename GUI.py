import tkinter as tk
import pandas as pd

root=tk.Tk()
 
# setting the windows size
root.geometry("800x600")
  
# declaring string variable
# for storing name and password
rno_var=tk.StringVar()
G1_var=tk.StringVar()
G2_var=tk.StringVar()
age_var=tk.StringVar()
Medu_var=tk.StringVar()
Fedu_var=tk.StringVar()
Tt_var=tk.StringVar()
St_var=tk.StringVar()
Fail_var=tk.StringVar()
Famrel_var=tk.StringVar()
Ft_var=tk.StringVar()
Gout_var=tk.StringVar()
Health_var=tk.StringVar()
Absence_var=tk.StringVar()
Result_txt=tk.StringVar()
Performance_txt=tk.StringVar()
Acc_txt=tk.StringVar()
Final_txt=tk.StringVar()

 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    rno=rno_var.get()
    G1 = G1_var.get()
    G2 = G2_var.get()
    age = age_var.get()
    Medu = Medu_var.get()
    Fedu = Fedu_var.get()
    traveltime =Tt_var.get()
    studytime = St_var.get()
    failures = Fail_var.get()
    famrel = Famrel_var.get()
    freetime =Ft_var.get()
    goout = Gout_var.get()
    health = Health_var.get()
    absences =Absence_var.get() 
    
    #password=passw_var.get()
    model = pd.read_pickle(r"D:\mcaproject\performance\DTmodel.pkl")
    print(model)
    # Make prediction
    result = model.predict(
        [[age, Medu, Fedu, traveltime, studytime, failures, famrel, freetime, goout, health, absences,G1,G2]])

    classification = result[0]
    print('G3 = ',classification) 
    print("The name is : " + rno)
    #print("The password is : " + password)
    #r="Final Score Predicted : "+ classification
    Result_txt.set(classification)
    Acc_txt.set(" 80%")
    if classification < 10:
        Performance_txt.set("Poor")
        Final_txt.set("Fail")
    elif 9 < classification < 12:
        Performance_txt.set("Sufficient")
        Final_txt.set("Passed")
    elif 11<classification<14:
        Performance_txt.set("Satisfactory")
        Final_txt.set("Passed")
    elif 13< classification < 16:
        Performance_txt.set("Good")
        Final_txt.set("Passed")
    elif classification > 15:
        Performance_txt.set("Excellent")
        Final_txt.set("Passed")
    #passw_var.set("")



def submit1():
    rno=rno_var.get()
    G1 = G1_var.get()
    G2 = G2_var.get()
    age = age_var.get()
    Medu = Medu_var.get()
    Fedu = Fedu_var.get()
    traveltime =Tt_var.get()
    studytime = St_var.get()
    failures = Fail_var.get()
    famrel = Famrel_var.get()
    freetime =Ft_var.get()
    goout = Gout_var.get()
    health = Health_var.get()
    absences =Absence_var.get() 
    #password=passw_var.get()
    model = pd.read_pickle(r"D:\mcaproject\performance\RFmodel.pkl")
    print(model)
    # Make prediction
    result = model.predict(
        [[age, Medu, Fedu, traveltime, studytime, failures, famrel, freetime, goout, health, absences,G1,G2]])

    classification = result[0]
    print('G3 = ',classification) 
    print("The name is : " + rno)
    Result_txt.set(classification)
    Acc_txt.set("82%")
    if classification < 10:
        Performance_txt.set("Poor")
        Final_txt.set("Fail")
    elif 9 < classification < 12:
        Performance_txt.set("Sufficient")
        Final_txt.set("Passed")
    elif 11<classification<14:
        Performance_txt.set("Satisfactory")
        Final_txt.set("Passed")
    elif 13< classification < 16:
        Performance_txt.set("Good")
        Final_txt.set("Passed")
    elif classification > 15:
        Performance_txt.set("Excellent")
        Final_txt.set("Passed")
    #print("The password is : " + password)

def submit2():
    rno=rno_var.get()
    G1 = G1_var.get()
    G2 = G2_var.get()
    age = age_var.get()
    Medu = Medu_var.get()
    Fedu = Fedu_var.get()
    traveltime =Tt_var.get()
    studytime = St_var.get()
    failures = Fail_var.get()
    famrel = Famrel_var.get()
    freetime =Ft_var.get()
    goout = Gout_var.get()
    health = Health_var.get()
    absences =Absence_var.get() 
    #password=passw_var.get()
    model = pd.read_pickle(r"D:\mcaproject\performance\GBmodel.pkl")
    print(model)
    # Make prediction
    result = model.predict(
        [[age, Medu, Fedu, traveltime, studytime, failures, famrel, freetime, goout, health, absences,G1,G2]])

    classification = result[0]
    print('G3 = ',classification) 
    print("The name is : " + rno)
    Result_txt.set(classification)
    Acc_txt.set("79.2%")
    if classification < 10:
        Performance_txt.set("Poor")
        Final_txt.set("Fail")
    elif 9 < classification < 12:
        Performance_txt.set("Sufficient")
        Final_txt.set("Passed")
    elif 11<classification<14:
        Performance_txt.set("Satisfactory")
        Final_txt.set("Passed")
    elif 13< classification < 16:
        Performance_txt.set("Good")
        Final_txt.set("Passed")
    elif classification > 15:
        Performance_txt.set("Excellent")
        Final_txt.set("Passed")
    #print("The password is : " + password)


def submit3():
    rno=rno_var.get()
    G1 = G1_var.get()
    G2 = G2_var.get()
    age = age_var.get()
    Medu = Medu_var.get()
    Fedu = Fedu_var.get()
    traveltime =Tt_var.get()
    studytime = St_var.get()
    failures = Fail_var.get()
    famrel = Famrel_var.get()
    freetime =Ft_var.get()
    goout = Gout_var.get()
    health = Health_var.get()
    absences =Absence_var.get() 
    #password=passw_var.get()
    model = pd.read_pickle(r"D:\mcaproject\performance\XGBmodel.pkl")
    print(model)
    # Make prediction
    result = model.predict(
        [[age, Medu, Fedu, traveltime, studytime, failures, famrel, freetime, goout, health, absences,G1,G2]])

    classification = result[0]
    print('G3 = ',classification) 
    print("The name is : " + rno)
    Result_txt.set(classification)
    Acc_txt.set("86%")
    if classification < 10:
        Performance_txt.set("Poor")
        Final_txt.set("Fail")
    elif 9 < classification < 12:
        Performance_txt.set("Sufficient")
        Final_txt.set("Passed")
    elif 11<classification<14:
        Performance_txt.set("Satisfactory")
        Final_txt.set("Passed")
    elif 13< classification < 16:
        Performance_txt.set("Good")
        Final_txt.set("Passed")
    elif classification > 15:
        Performance_txt.set("Excellent")
        Final_txt.set("Passed")
    #print("The password is : " + password)

def submit4():
    image = Image.open(r"D:\mcaproject\performance\comparison.JPG")
    image.show()
# 1
# name using widget Label
rno = tk.Label(root, text = 'roll no', font=('calibre',10, 'bold'))
  
rno_entry = tk.Entry(root,textvariable = rno_var, font=('calibre',10,'normal'))

  
# 2
# name using widget Label
G1 = tk.Label(root, text = 'G1', font=('calibre',10, 'bold'))
  
G1_entry = tk.Entry(root,textvariable = G1_var, font=('calibre',10,'normal'))
G1_op=tk.Label(root, text = 'from 0 to 20', font=('calibre',8, 'normal'))
# 3
# name using widget Label
G2 = tk.Label(root, text = 'G2', font=('calibre',10, 'bold'))
  
G2_entry = tk.Entry(root,textvariable = G2_var, font=('calibre',10,'normal'))
G2_op=tk.Label(root, text = 'from 0 to 20', font=('calibre',8, 'normal'))
# 4
# name using widget Label
age = tk.Label(root, text = 'age', font=('calibre',10, 'bold'))
  
age_entry = tk.Entry(root,textvariable = age_var, font=('calibre',10,'normal'))
age_op=tk.Label(root, text = 'from 15 to 22', font=('calibre',8, 'normal'))
# 5
# name using widget Label
Medu = tk.Label(root, text = 'Mother Education', font=('calibre',10, 'bold'))
  
Medu_entry = tk.Entry(root,textvariable = Medu_var, font=('calibre',10,'normal'))
Medu_op=tk.Label(root, text = '0 - none, 1 -primary education, 2 -5 to 9 , 3 -secondary education, 4 - higher education', font=('calibre',8, 'normal'))
# 6
# name using widget Label
Fedu = tk.Label(root, text = 'Father Education', font=('calibre',10, 'bold'))
  
Fedu_entry = tk.Entry(root,textvariable = Fedu_var, font=('calibre',10,'normal'))
Fedu_op=tk.Label(root, text = '0 - none, 1 -primary education, 2 -5 to 9 , 3 -secondary education, 4 - higher education', font=('calibre',8, 'normal'))
# 7
# name using widget Label
Tt = tk.Label(root, text = 'Travel Time', font=('calibre',10, 'bold'))
  
Tt_entry = tk.Entry(root,textvariable = Tt_var, font=('calibre',10,'normal'))
Tt_op=tk.Label(root, text = '1 -<15 min., 2 -15 to 30 min., 3 -30 min. to 1 hr, 4 ->1 hr', font=('calibre',8, 'normal'))
# 8
# name using widget Label
St = tk.Label(root, text = 'Study Time', font=('calibre',10, 'bold'))
  
St_entry = tk.Entry(root,textvariable = St_var, font=('calibre',10,'normal'))
St_op=tk.Label(root, text = '1 -<2 hr, 2 -2 to 5 hr, 3 -5 to 10 hr, 4 ->10 hr', font=('calibre',8, 'normal'))
# 9
# name using widget Label
Fail = tk.Label(root, text = 'Failures', font=('calibre',10, 'bold'))
  
Fail_entry = tk.Entry(root,textvariable = Fail_var, font=('calibre',10,'normal'))
Fail_op=tk.Label(root, text = 'n if 1<=n<3, else 4', font=('calibre',8, 'normal'))
# 10
# name using widget Label
Famrel = tk.Label(root, text = 'Family relation', font=('calibre',10, 'bold'))
  
Famrel_entry = tk.Entry(root,textvariable = Famrel_var, font=('calibre',10,'normal'))
Famrel_op=tk.Label(root, text = 'from 1 - very bad to 5 - excellent', font=('calibre',8, 'normal'))
# 11
# name using widget Label
Ft = tk.Label(root, text = 'Free Time', font=('calibre',10, 'bold'))
  
Ft_entry = tk.Entry(root,textvariable = Ft_var, font=('calibre',10,'normal'))
Ft_op=tk.Label(root, text = 'from 1 - very low to 5 - very high', font=('calibre',8, 'normal'))
# 12
# name using widget Label
Gout = tk.Label(root, text = 'Go Out', font=('calibre',10, 'bold'))
  
Gout_entry = tk.Entry(root,textvariable = Gout_var, font=('calibre',10,'normal'))
Gout_op=tk.Label(root, text = '1 - very low to 5 - very high', font=('calibre',8, 'normal'))
# 13
# name using widget Label
Health = tk.Label(root, text = 'Health', font=('calibre',10, 'bold'))
  
Health_entry = tk.Entry(root,textvariable = Health_var, font=('calibre',10,'normal'))
Health_op=tk.Label(root, text = 'from 1 - very bad to 5 - very good', font=('calibre',8, 'normal'))
# 14
# name using widget Label
Absence = tk.Label(root, text = 'Absence', font=('calibre',10, 'bold'))
  
Absence_entry = tk.Entry(root,textvariable = Absence_var, font=('calibre',10,'normal'))
Absence_op=tk.Label(root, text = 'from 0 to 93', font=('calibre',8, 'normal'))

Acdetails = tk.Label(root, text = 'Academic details', font=('calibre',12, 'bold'))
Psdetails = tk.Label(root, text = 'Personal details', font=('calibre',12, 'bold'))  
# creating a button using the widget
# Button that will call the submit function
Predict_Using  = tk.Label(root, text = 'Predict Using', font=('calibre',10, 'bold'))
sub_btn1=tk.Button(root,text = 'DecisionTree', command = submit)
sub_btn2=tk.Button(root,text = 'RandomForest', command = submit1)
sub_btn3=tk.Button(root,text = 'AdaBoost', command = submit2)
sub_btn4=tk.Button(root,text = 'XGBoost', command = submit3)
sub_btn5=tk.Button(root,text = 'Prediction Anlysis', command = submit4)


#Result Labels
Result_lbl= tk.Entry(root,textvariable = Result_txt, font=('calibre',12,'bold'))
Acc_lbl=tk.Entry(root,textvariable = Acc_txt, font=('calibre',12,'bold'))
Performance=tk.Entry(root,textvariable = Performance_txt, font=('calibre',12,'bold'))
FinalRe=tk.Entry(root,textvariable = Final_txt, font=('calibre',12,'bold'))
FG = tk.Label(root, text = 'Final Grade', font=('calibre',12, 'bold'))
Accuracy=tk.Label(root, text = 'Accuracy', font=('calibre',12, 'bold'))
Category=tk.Label(root, text = 'Category', font=('calibre',12, 'bold'))
FinalR=tk.Label(root, text = 'Final Result', font=('calibre',12, 'bold'))
  
# placing the label and entry in
# the required position using grid
# method
Acdetails.grid(row=0,column=0)

rno.grid(row=1,column=0)
rno_entry.grid(row=1,column=1)
G1.grid(row=2,column=0)
G1_entry.grid(row=2,column=1)
G1_op.grid(row=2,column=2)
G2.grid(row=3,column=0)
G2_entry.grid(row=3,column=1)
G2_op.grid(row=3,column=2)
St.grid(row=4,column=0)
St_entry.grid(row=4,column=1)
St_op.grid(row=4,column=2)
Tt.grid(row=5,column=0)
Tt_entry.grid(row=5,column=1)
Tt_op.grid(row=5,column=2)
Fail.grid(row=6,column=0)
Fail_entry.grid(row=6,column=1)
Fail_op.grid(row=6,column=2)
Absence.grid(row=7,column=0)
Absence_entry.grid(row=7,column=1)
Absence_op.grid(row=7,column=2)

Psdetails.grid(row=8,column=0)
age.grid(row=9,column=0)
age_entry.grid(row=9,column=1)
age_op.grid(row=9,column=2)
Ft.grid(row=10,column=0)
Ft_entry.grid(row=10,column=1)
Ft_op.grid(row=10,column=2)
Gout.grid(row=11,column=0)
Gout_entry.grid(row=11,column=1)
Gout_op.grid(row=11,column=2)
Health.grid(row=12,column=0)
Health_entry.grid(row=12,column=1)
Health_op.grid(row=12,column=2)
Medu.grid(row=13,column=0)
Medu_entry.grid(row=13,column=1)
Medu_op.grid(row=13,column=2)
Fedu.grid(row=14,column=0)
Fedu_entry.grid(row=14,column=1)
Fedu_op.grid(row=14,column=2)
Famrel.grid(row=15,column=0)
Famrel_entry.grid(row=15,column=1)
Famrel_op.grid(row=15,column=2)


Predict_Using.grid(row=16,column=0)
sub_btn1.grid(row=16,column=1)
sub_btn2.grid(row=16,column=2)
sub_btn3.grid(row=17,column=1)
sub_btn4.grid(row=17,column=2)

FG.grid(row=18,column=1)
Result_lbl.grid(row=18, column=2)
Accuracy.grid(row=19,column=1)
Acc_lbl.grid(row=19,column=2)
Category.grid(row=20, column=1)
Performance.grid(row=20, column=2)
FinalR.grid(row=21, column=1)  
FinalRe.grid(row=21, column=2)

sub_btn5.grid(row=22,column=1)
# performing an infinite loop
# for the window to display
root.mainloop()
