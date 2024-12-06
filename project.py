import tkinter as tk
import openpyxl
from tkinter import messagebox


def start_app():
    #messagebox.showinfo("Message", "Button clicked!")
    for widget in root.winfo_children():
        widget.destroy()

    new_label = tk.Label(root, text="Welcome to the second screen!", font=("Arial", 25))
    new_label.pack(pady=50)

    back_button = tk.Button(root, text="Back", command=main_menu, width=20, height=2)
    back_button.pack(pady=20)


def main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    # Creating title
    title = tk.Label(root, text="StayZen: Your Complete Hotel Management System", font=("Arial", 25))
    title.pack(pady=(100, 10))

    # Creating buttons
    button1 = tk.Button(root, text="Start Application", command=start_app, width=20, height=2)
    button1.pack(pady=(150, 10))

    button2 = tk.Button(root, text="Close Application", command=root.destroy, width=20, height=2)
    button2.pack(pady=10)

    credits = tk.Label(root, text="A project by:\nCarlos Alcoba\nZain Ahmad\nFaiza Azam\nHarbir Bains",
                       font=("Arial bold", 10))
    credits.update_idletasks()
    credits.place(x=0, y=root.winfo_height() - 90)



# Create the main application window
root = tk.Tk()
root.title("Button Interface Example")
root.state("zoomed")

main_menu()

# Start the Tkinter event loop
root.mainloop()
