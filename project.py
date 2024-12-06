import tkinter as tk
from tkinter import Label, ttk, messagebox
from PIL import Image, ImageTk

def start_app():
    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="StayZen: Your Complete Hotel Management System", font=("Arial", 25))
    title.pack(pady=(50, 10))

    add_rooms_button = tk.Button(root, text="Add Rooms", command=add_rooms, width=20, height=2)
    add_rooms_button.pack(pady=20)

    back_button = tk.Button(root, text="Back", command=main_menu, width=20, height=2)
    back_button.pack(pady=20)

def main_menu():
    global logo  # Prevent garbage collection of the image

    for widget in root.winfo_children():
        widget.destroy()

    # Title
    title = tk.Label(root, text="StayZen: Your Complete Hotel Management System", font=("Arial", 25))
    title.pack(pady=(100, 10))

    # Logo
    logo = Image.open("StayZenLogo2-removebg.png")
    logo = logo.resize((720, 400))
    logo = ImageTk.PhotoImage(logo)

    image_label = Label(root, image=logo)
    image_label.pack(pady=20)

    # Buttons
    button1 = tk.Button(root, text="Start Application", command=start_app, width=40, height=3)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Close Application", command=root.destroy, width=40, height=3)
    button2.pack(pady=10)

    credits = tk.Label(root, text="A project by:\nCarlos Alcoba\nZain Ahmad\nFaiza Azam\nHarbir Bains",
                       font=("Arial bold", 10))
    credits.update_idletasks()
    credits.place(x=0, y=root.winfo_height() - 90)

def add_rooms():
    global room_number, room_price, rType_var, rView_var  # Declare variables as global

    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="StayZen: Your Complete Hotel Management System", font=("Arial", 25))
    title.pack(pady=(50, 10))

    title = tk.Label(root, text="Add Rooms", font=("Arial", 25))
    title.pack(pady=(10, 10))

    # Room Number
    rNum_label = tk.Label(root, text="Room Number:", font=("Arial", 12))
    rNum_label.pack(pady=(20, 5))
    room_number = tk.Entry(root, font=("Arial", 12), width=30)
    room_number.pack(pady=5)

    # Room Type
    rType_label = tk.Label(root, text="Room Type:", font=("Arial", 12))
    rType_label.pack(pady=(20, 5))
    options = ["Single Room", "Double Room", "Suite", "Deluxe Room"]
    rType_var = tk.StringVar()  # Correctly declare and initialize
    room_type = ttk.Combobox(root, textvariable=rType_var, values=options, state="readonly", width=30)
    room_type.pack(pady=10)

    # Room Price
    rPrice_label = tk.Label(root, text="Room Price:", font=("Arial", 12))
    rPrice_label.pack(pady=(20, 5))
    room_price = tk.Entry(root, font=("Arial", 12), width=30)
    room_price.pack(pady=5)

    # Room View
    rView_label = tk.Label(root, text="Room View:", font=("Arial", 12))
    rView_label.pack(pady=(20, 5))
    optionsV = ["None", "Ocean", "Monument", "City", "Garden", "Pool"]
    rView_var = tk.StringVar()  # Correctly declare and initialize
    room_view = ttk.Combobox(root, textvariable=rView_var, values=optionsV, state="readonly", width=30)
    room_view.pack(pady=10)

    # Submit Button
    submit_button = tk.Button(root, text="Submit", command=submit_room, width=20, height=2)
    submit_button.pack(pady=20)

    # Back Button
    back_button = tk.Button(root, text="Back", command=start_app, width=20, height=2)
    back_button.pack(pady=20)

def submit_room():
    room_num = room_number.get()
    room_type = rType_var.get()
    price = room_price.get()
    room_view = rView_var.get()

    # Validation
    if not room_num or not price or not room_type or not room_view:
        messagebox.showerror("Error", "All fields are required!")
        return

    #Check if room number already exists

    # Clear inputs
    room_number.delete(0, tk.END)
    room_price.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("StayZen")
root.state("zoomed")

# Load the main menu
main_menu()

# Start the Tkinter event loop
root.mainloop()
