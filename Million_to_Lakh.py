from tkinter import *

def millions_to_lakh():
    millions=float (millions_input.get())
    lakh=millions*10
    ans_label.config(text=f"{lakh}")





window=Tk()
# window.minsize(width=400,height=200)
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)


millions_input=Entry(width=7)
millions_input.grid(column=1,row=0)



millions_label=Label(text="Million",font=("Arial"))
millions_label.grid(column=2,row=0)



equal_label=Label(text="is equal to",font=("Arial"))
equal_label.grid(column=0,row=1)

ans_label=Label(text="0",font=("Arial"))
ans_label.grid(column=1,row=1)
# ans_label.config(padx=30,pady=30)

lakh_label=Label(text="Lakh",font=("Arial"))
lakh_label.grid(column=2,row=1)


calculate_button=Button(text="Calculate" ,command=millions_to_lakh)
calculate_button.grid(column=1,row=2)





window.mainloop()