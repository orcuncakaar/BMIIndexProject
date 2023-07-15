import tkinter

#Create Window
my_window = tkinter.Tk(screenName="BMI Calculator")
my_window.title("BMI Calculator")
my_window.geometry("300x300")

FONT=("Arial",9,"italic")

#Create UI
my_entry_weight=tkinter.Entry()
my_entry_weight.pack()
my_entry_weight.place(x=87, y=100)

my_label_weight=tkinter.Label(text="Enter Your Weight.(kg)",font=FONT)
my_label_weight.pack()
my_label_weight.place(x=85,y=80)

my_entry_height=tkinter.Entry()
my_entry_height.pack()
my_entry_height.place(x=87,y=170)

my_label_height=tkinter.Label(text="Enter Your Height.(cm)",font=FONT)
my_label_height.pack()
my_label_height.place(x=85,y=150)

my_bmi_label=tkinter.Label()
my_bmi_label.pack()
my_bmi_label.place(x=85,y=250)

my_healthstate_label=tkinter.Label()
my_healthstate_label.pack()
my_healthstate_label.place(x=85,y=270)

#Create Functions
def calculate_bmi():
    try:
        height=float(my_entry_height.get())
        weight=float(my_entry_weight.get())

        bmi=weight / (height/100)**2
        bmi=round(bmi,2)
        my_bmi_label.config(text="Your BMI Score is: " + str(bmi))

        if bmi<18.5:
            my_healthstate_label.config(text="You are Under Weight.")
        elif bmi>18.5 and bmi<24.9:
            my_healthstate_label.config(text="You are Normal Weight.")
        elif bmi>=25 and bmi<29.9:
            my_healthstate_label.config(text="You are Over Weight.")
        elif bmi>=30 and bmi<34.9:
            my_healthstate_label.config(text="You are Obesity (Class 1)")
        elif bmi>=35 and bmi<39.9:
            my_healthstate_label.config(text="You are Obesity (Class 2)")
        elif bmi>=40:
            my_healthstate_label.config(text="You are Obesity (Class 3)")


    except ValueError:
        my_bmi_label.config(text="Please, enter valid data!")




my_calculate_button=tkinter.Button(text="Calculate", command=calculate_bmi)
my_calculate_button.pack()
my_calculate_button.place(x=117,y=200)






my_window.mainloop()
