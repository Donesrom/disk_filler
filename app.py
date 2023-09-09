import os
import random
import string
import tkinter as tk
from tkinter import filedialog

def generate_dummy_file(directory, filename, size_mb):
    # Generate a random dummy file with the specified size
    filepath = os.path.join(directory, filename)
    with open(filepath, 'wb') as file:
        file.write(b''.join(random.choice(string.ascii_letters).encode() for _ in range(size_mb * 1024 * 1024)))

def create_file():
    filename = filename_entry.get()
    size_mb = int(size_entry.get())
    generate_dummy_file(target_directory, filename, size_mb)
    status_label.config(text=f"File '{filename}' ({size_mb} MB) created in {target_directory}.")
    filename_entry.delete(0, tk.END)
    size_entry.delete(0, tk.END)

def select_directory():
    global target_directory
    target_directory = filedialog.askdirectory()

app = tk.Tk()
app.title("Disk Space Filler")

target_directory = ""

select_button = tk.Button(app, text="Select Target Directory", command=select_directory)
select_button.pack()

filename_label = tk.Label(app, text="Enter Filename:")
filename_label.pack()
filename_entry = tk.Entry(app)
filename_entry.pack()

size_label = tk.Label(app, text="Enter File Size (MB):")
size_label.pack()
size_entry = tk.Entry(app)
size_entry.pack()

create_button = tk.Button(app, text="Create File", command=create_file)
create_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()

