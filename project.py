import tkinter as tk
from tkinter import Label, ttk, messagebox
from PIL import Image, ImageTk
from openpyxl import workbook, load_workbook

EXCEL_FILE = "Database.xlsx"


def start_app():
    for widget in root.winfo_children():
        widget.destroy()

    # Title
    title = tk.Label(root, text="StayZen: Your Complete Hotel Management System", font=("Arial", 25))
    title.pack(pady=(50, 10))
    # Add Rooms
    add_rooms_button = tk.Button(root, text="Add Rooms", command=add_rooms, width=20, height=2)
    add_rooms_button.pack(pady=20)

    # Remove Rooms
    remove_rooms_button = tk.Button(root, text="Remove Rooms", command=remove_rooms, width=20, height=2)
    remove_rooms_button.pack(pady=20)


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

    workbook = load_workbook(EXCEL_FILE)
    sheet = workbook.active

    # Validation
    if not room_num or not price or not room_type or not room_view:
        messagebox.showerror("Error", "All fields are required!")
        return
    room_num = str(room_num).zfill(3)
    for i in range(1, sheet.max_row + 1):
        cell_room = sheet.cell(row=i, column=1)
        if room_num == cell_room.value:
            messagebox.showerror("Error", "Room number already exist")
            return

    sheet.append([room_num, room_type, price, room_view, "Yes"])
    workbook.save(EXCEL_FILE)

    # Clear inputs
    room_number.delete(0, tk.END)
    room_price.delete(0, tk.END)
    messagebox.showinfo(title="Success", message="Room Added")

def remove_rooms():
    def room_info(event):
        room = rooms_var.get()

        for i in range(1, sheet.max_row + 1):
            room_num = sheet.cell(row=i, column=1).value
            if room_num == room:
                room_type = sheet.cell(row=i, column=2).value
                price = float(sheet.cell(row=i, column=3).value)
                view = sheet.cell(row=i, column=4).value

                room_info_label.config(text=f"Type: {room_type}\nPrice: ${price:,.2f}\nView: {view}")
                return

    def remove():
        room = rooms_var.get()

        for i in range(2, sheet.max_row + 1):
            room_num = sheet.cell(row=i, column=1).value
            if room_num == room:
                sheet.delete_rows(i)
                workbook.save(EXCEL_FILE)
                messagebox.showinfo(title="Success", message="Room removed")
                return



    for widget in root.winfo_children():
        widget.destroy()

    title = tk.Label(root, text="StayZen: Your Complete Hotel Management System", font=("Arial", 25))
    title.pack(pady=(50, 10))

    title = tk.Label(root, text="Remove Rooms", font=("Arial", 25))
    title.pack(pady=(10, 10))

    workbook = load_workbook(EXCEL_FILE)
    sheet = workbook.active

    rooms_label = tk.Label(root, text="Current Rooms", font=("Arial", 12))
    rooms_label.pack(pady=(20, 5))

    optionsR = [sheet.cell(row=i, column=1).value for i in range(2, sheet.max_row + 1)]
    rooms_var = tk.StringVar()
    rooms = ttk.Combobox(root, textvariable=rooms_var, values=optionsR, state="readonly", width=30)
    rooms.pack(pady=10)

    room_info_label = tk.Label(root, text="Select a room to see details", font=("Arial", 12), justify="left")
    room_info_label.pack(pady=(20, 10))

    rooms.bind("<<ComboboxSelected>>", room_info) # triggers when an item is selected in the list

    feedback_label = tk.Label(root, text="Reason for removal:", font=("Arial", 12))
    feedback_label.pack(pady=(20, 10))
    feedback_text = tk.Text(root, font=("Arial", 12), width=30, height=5)
    feedback_text.pack(pady=10)

    remove_button = tk.Button(root, text="Remove", command=remove, width=20, height=2)
    remove_button.pack(pady=20)


    back_button = tk.Button(root, text="Back", command=start_app, width=20, height=2)
    back_button.pack(pady=20)



# Create the main application window
root = tk.Tk()
root.title("StayZen")
root.state("zoomed")

# Load the main menu
main_menu()

# Start the Tkinter event loop
root.mainloop()
