import tkinter as tk  # Importing the Tkinter library for GUI
from tkinter import messagebox  # Importing messagebox to show pop-up messages

# Create the main window
window = tk.Tk()  # Initialize the Tkinter window
window.title("Flight Booker")  # Set the title of the window
window.geometry("400x300")  # Set the size of the window (width x height)

# Dictionary of available flights (flight number -> destination)
flights = {
    "LA123": "Los Angeles",
    "TX456": "Texas",
    "NY789": "New York"
}

# Dictionary to store booked flights (name -> flight number)
reservations = {}

# Function to handle flight booking
def book_flight():
    name = name_entry.get()  # Get the name entered by the user
    flight_num = flight_entry.get()  # Get the flight number entered by the user

    # Check if the name is entered and the flight number exists in the flights dictionary
    if name and flight_num in flights:
        reservations[name] = flight_num  # Save the booking (name -> flight number)
        # Show a confirmation message
        messagebox.showinfo("Done", f"Booked {flight_num} to {flights[flight_num]} for {name}!")
        
        # Clear the text fields after booking
        name_entry.delete(0, tk.END)  
        flight_entry.delete(0, tk.END)
    else:
        # Show an error message if the input is wrong
        messagebox.showerror("Oops", "Wrong flight number or no name!")

# GUI elements

# Title label at the top
tk.Label(window, text="Flight Booker").pack(pady=10)  

# Label and input field for name
tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window)  
name_entry.pack()

# Label and input field for flight number
tk.Label(window, text="Flight Number:").pack()
flight_entry = tk.Entry(window)  
flight_entry.pack()

# Button to book the flight, calls book_flight() when clicked
tk.Button(window, text="Book Flight", command=book_flight).pack(pady=10)

# Run the main event loop to keep the window open
window.mainloop()
