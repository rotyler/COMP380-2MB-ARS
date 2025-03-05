# airline.py - starting with just booking a flight
import tkinter as tk
from tkinter import messagebox

# make the window
window = tk.Tk()
window.title("Flight Booker")
window.geometry("400x300")  # picked a size that looks okay

# list of flights i came up with
flights = {
    "LA123": "Los Angeles",
    "TX456": "Texas",
    "NY789": "New York"
}

# store bookings in a dictionary for now
reservations = {}

# function to book a flight
def book_flight():
    name = name_entry.get()
    flight_num = flight_entry.get()
    # check if stuff is entered right
    if name and flight_num in flights:
        reservations[name] = flight_num  # save the booking
        messagebox.showinfo("Done", f"Booked {flight_num} to {flights[flight_num]} for {name}!")
        name_entry.delete(0, tk.END)  # clear the boxes
        flight_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Oops", "Wrong flight number or no name!")

# gui stuff
tk.Label(window, text="Flight Booker").pack(pady=10)  # simple title
tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Flight Number:").pack()
flight_entry = tk.Entry(window)
flight_entry.pack()

tk.Button(window, text="Book Flight", command=book_flight).pack(pady=10)

window.mainloop()