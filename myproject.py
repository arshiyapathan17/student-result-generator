import tkinter as tk
from tkinter import messagebox
import mysql.connector

#......DATABASE CONNECTION .........
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_db"
)
cur = con.cursor()

#////////////////////FUNCTIONS //////////////////

# ............ GRADE FUNCTION ........
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

# ............. RESULT FUNCTION .........
def generate_result():
    try:
        name = entry_name.get().strip()
        roll = entry_roll.get().strip()

        if not name or not roll:
            messagebox.showerror("Error", "Name and Roll are required")
            return

        python = float(entry_python.get())
        java = float(entry_java.get())
        php = float(entry_php.get())

        if not all(0 <= m <= 100 for m in (python, java, php)):
            messagebox.showerror("Error", "Marks must be between 0 and 100")
            return

        total = python + java + php
        avg = total / 3
        grade = calculate_grade(avg)

# ----- SAVE TO DATABASE -----
        cur.execute(
            "INSERT INTO results (name, roll, python, java, php, total, average, grade) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (name, roll, python, java, php, total, avg, grade)
        )
        con.commit()

#----- SHOW RESULT -----
        lbl_name.config(text=name)
        lbl_roll.config(text=roll)
        lbl_total.config(text=total)
        lbl_avg.config(text=f"{avg:.2f}")
        lbl_grade.config(
            text=grade,
            fg="#198754" if grade != "Fail" else "#dc3545"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter valid numeric marks")

# ---------- MAIN WINDOW ---------------------
root = tk.Tk()
root.title("Student Result System")
root.geometry("520x650")
root.resizable(False, False)
root.configure(bg="#e0bad7")
root.state("zoomed")

# ................. HEADER............
tk.Label(
    root,
    text="Student Result Generator",
    font=("Segoe UI", 20, "bold"),
    bg="#592941",
    fg="white",
    pady=14
).pack(fill="x")

# TAKING  INPUT FROM USER .................
input_frame = tk.Frame(root, bg="#f8f9fa", padx=30, pady=25)
input_frame.pack(pady=18)

def create_label(text, row):
    tk.Label(
        input_frame,
        text=text,
        bg="#f8f9fa",
        font=("Segoe UI", 11, "bold"),
        width=15,
        anchor="w"
    ).grid(row=row, column=0, pady=6)

def create_entry(row):
    e = tk.Entry(input_frame, width=25, font=("Segoe UI", 11))
    e.grid(row=row, column=1)
    return e

create_label("Student Name", 0)
entry_name = create_entry(0)

create_label("Roll Number", 1)
entry_roll = create_entry(1)

create_label("Python", 2)
entry_python = create_entry(2)

create_label("Java", 3)
entry_java = create_entry(3)

create_label("PHP", 4)
entry_php = create_entry(4)

# ................. BUTTON ....................
tk.Button(
    root,
    text="Generate Result",
    bg="#592941",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    width=24,
    activebackground="#198754",
    command=generate_result
).pack(pady=12)

# ..........RESULT .........
result_frame = tk.Frame(
    root,
    bg="white",
    bd=3,
    relief="ridge",
    padx=35,
    pady=20,
    width=380
)
result_frame.pack(pady=20)
result_frame.pack_propagate(False)

label_font = ("Segoe UI", 11, "bold")
value_font = ("Segoe UI", 11)

# result_label function

def result_label(text, row):
    tk.Label(
        result_frame,
        text=text,
        bg="white",
        font=label_font,
        width=15,
        anchor="w"
    ).grid(row=row, column=0, pady=7)

#result value function ...    

def result_value(row, font=value_font, color="black"):
    lbl = tk.Label(
        result_frame,
        bg="white",
        font=font,
        fg=color,
        width=18,
        anchor="w"
    )
    lbl.grid(row=row, column=1, pady=7)
    return lbl

result_label("Name :", 0)
lbl_name = result_value(0)

result_label("Roll No :", 1)
lbl_roll = result_value(1)

result_label("Total Marks :", 2)
lbl_total = result_value(2, ("Segoe UI", 12, "bold"), "#0d6efd")

result_label("Average :", 3)
lbl_avg = result_value(3, ("Segoe UI", 12, "bold"), "#198754")

result_label("Grade :", 4)
lbl_grade = result_value(4, ("Segoe UI", 18, "bold"))

root.mainloop()
