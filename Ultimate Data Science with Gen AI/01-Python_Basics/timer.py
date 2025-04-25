import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.root.geometry("400x300")

        # Timer display
        self.time_var = tk.StringVar(value="00:00:00")
        self.label = tk.Label(root, textvariable=self.time_var, font=("Helvetica", 48))
        self.label.pack(pady=20)

        # Entry for input seconds
        self.entry = tk.Entry(root, font=("Helvetica", 20), justify='center')
        self.entry.insert(0, "Enter seconds")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.pack(pady=10)

        # Button frame for better layout
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        # Start Button
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_timer, font=("Helvetica", 18))
        self.start_button.grid(row=0, column=0, padx=10)

        # Stop Button
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_timer, font=("Helvetica", 18))
        self.stop_button.grid(row=0, column=1, padx=10)

        # Reset Button
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_timer, font=("Helvetica", 18))
        self.reset_button.grid(row=0, column=2, padx=10)

        self.running = False
        self.remaining = 0

    def clear_placeholder(self, event):
        if self.entry.get() == "Enter seconds":
            self.entry.delete(0, tk.END)

    def start_timer(self):
        if not self.running:
            try:
                self.remaining = int(self.entry.get())
                if self.remaining <= 0:
                    raise ValueError
                self.running = True
                self.countdown()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a positive integer.")
                self.reset_timer()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_var.set("00:00:00")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "Enter seconds")

    def countdown(self):
        if self.running:
            if self.remaining <= 0:
                self.time_var.set("00:00:00")
                self.running = False
            else:
                hrs, rem = divmod(self.remaining, 3600)
                mins, secs = divmod(rem, 60)
                self.time_var.set(f"{hrs:02}:{mins:02}:{secs:02}")
                self.remaining -= 1
                self.root.after(1000, self.countdown)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()