import tkinter as tk


def handle_submit():
    global name_entry, email_entry, message_text, result_label  
    name = name_entry.get()
    email = email_entry.get()
    message = message_text.get("1.0", tk.END)

    if name and email and message.strip():
        result_label.config(text="Thank you for submitting the form!", fg="green")
      
    else:
        result_label.config(text="Please fill in all fields.", fg="red")


def build_gui():
    root = tk.Tk()
    root.title("Final Lab HCI")


    frame = tk.Frame(root, bg="white")
    frame.pack(padx=20, pady=20)

    
    global name_entry, email_entry, message_text, result_label  
    name_label = tk.Label(frame, text="Name:", font=("Arial", 12))
    name_label.grid(row=0, column=0, sticky=tk.W)
    name_entry = tk.Entry(frame, width=30, font=("Arial", 12))
    name_entry.grid(row=0, column=1)

    email_label = tk.Label(frame, text="Email:", font=("Arial", 12))
    email_label.grid(row=1, column=0, sticky=tk.W)
    email_entry = tk.Entry(frame, width=30, font=("Arial", 12))
    email_entry.grid(row=1, column=1)

    message_label = tk.Label(frame, text="Message:", font=("Arial", 12))
    message_label.grid(row=2, column=0, sticky=tk.W)
    message_text = tk.Text(frame, width=30, height=5, font=("Arial", 12))
    message_text.grid(row=2, column=1)


    submit_button = tk.Button(frame, text="Submit", bg="#007bff", fg="white", padx=10, pady=5, font=("Arial", 12), command=handle_submit)
    submit_button.grid(row=3, columnspan=2, pady=10)


    result_label = tk.Label(frame, text="", font=("Arial", 12))
    result_label.grid(row=4, columnspan=2, pady=10)

 
    root.mainloop()


build_gui()
