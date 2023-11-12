from tkinter import*
root=Tk()
root.title("ASCII")
root.geometry("400x600")
root.configure(bg='yellow')

enter_word=Entry(root)
enter_word.place(relx="0.5" , rely="0.4" , anchor=CENTER)

label=Label(root , text="Your name in ASCII code is: ", bg='orange' , fg='black')
label_encrypted=Label(root , text="Your name in Encrypted code is: ", bg='orange' , fg='black')

def ascii_converter():
    input_word=enter_word.get()
    
    for everyletter in input_word:
        label["text"] += str(ord(everyletter)) + " "
        ascii= int(ord(everyletter))
        encrypted=ascii -1 
        label_encrypted["text"] += str(chr(encrypted)) + ""
        
btn_1=Button(root,text="Your ASCII code and your Encrypted number is!!",command=ascii_converter , bg='orange',fg='black')
btn_1.place(relx="0.5", rely="0.5", anchor=CENTER)        
label.place(relx="0.5", rely="0.6", anchor=CENTER)    
label_encrypted.place(relx="0.5" , rely="0.7" , anchor=CENTER)

root.mainloop()