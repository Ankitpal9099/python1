import tkinter as tk
from tkinter import messagebox
import mysql.connector

# # Database connection
# class Database:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host="localhost",
#             user="system",
#             password="",
#             database="hotel_management"
#         )
#         self.cursor = self.conn.cursor()

#     def insert_guest(self, name, room):
#         self.cursor.execute("INSERT INTO guests (name, room) VALUES (%s, %s)", (name, room))
#         self.conn.commit()

#     def checkout_guest(self, room):
#         self.cursor.execute("DELETE FROM guests WHERE room = %s", (room,))
#         self.conn.commit()

#     def get_total_guests(self):
#         self.cursor.execute("SELECT COUNT(*) FROM guests")
#         return self.cursor.fetchone()[0]

#     def close(self):
#         self.cursor.close()
#         self.conn.close()

# Hotel Management Application
class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        # self.db = Database()

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Check-in Section
        self.checkin_frame = tk.Frame(self.root)
        self.checkin_frame.pack(pady=10)

        tk.Label(self.checkin_frame, text="Guest Name:").grid(row=0, column=0)
        self.guest_name = tk.Entry(self.checkin_frame)
        self.guest_name.grid(row=0, column=1)

        tk.Label(self.checkin_frame, text="Room Number:").grid(row=1, column=0)
        self.room_number = tk.Entry(self.checkin_frame)
        self.room_number.grid(row=1, column=1)

        self.checkin_button = tk.Button(self.checkin_frame, text="Check In", command=self.check_in)
        self.checkin_button.grid(row=2, columnspan=2)

        # Checkout Section
        self.checkout_frame = tk.Frame(self.root)
        self.checkout_frame.pack(pady=10)

        tk.Label(self.checkout_frame, text="Room Number:").grid(row=0, column=0)
        self.checkout_room = tk.Entry(self.checkout_frame)
        self.checkout_room.grid(row=0, column=1)

        self.checkout_button = tk.Button(self.checkout_frame, text="Check Out", command=self.check_out)
        self.checkout_button.grid(row=1, columnspan=2)

        # Total Guests Section
        self.total_guests_button = tk.Button(self.root, text="Total Guests", command=self.show_total_guests)
        self.total_guests_button.pack(pady=10)

    def check_in(self):
        name = self.guest_name.get()
        room = self.room_number.get()
        if name and room:
            self.db.insert_guest(name, room)
            messagebox.showinfo("Success", "Guest checked in successfully!")
            self.guest_name.delete(0, tk.END)
            self.room_number.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def check_out(self):
        room = self.checkout_room.get()
        if room:
            self.db.checkout_guest(room)
            messagebox.showinfo("Success", "Guest checked out successfully!")
            self.checkout_room.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a room number.")

    def show_total_guests(self):
        total = self.db.get_total_guests()
        messagebox.showinfo("Total Guests", f"Total guests currently checked in: {total}")

    def close(self):
        self.db.close()
        self.root.destroy()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()