import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = "You are underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        elif 25 <= bmi < 29.9:
            status = "You are overweight"
        else:
            status = "Obesity"


        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}\nHealth: {status}")
    except ValueError:
        messagebox.showerror("Input error", "Please make sure to enter a valid number!")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.configure(bg="#f0f8ff")


title_label = tk.Label(root, text="BMI Calculator", font=("Helvetica", 16, "bold"), bg="#f0f8ff")
title_label.pack(pady=10)

gender_label = tk.Label(root, text="Gender:", font=("Helvetica", 12), bg="#f0f8ff")
gender_label.pack(pady=5)

gender_var = tk.StringVar(value="Male")
gender_frame = tk.Frame(root, bg="#f0f8ff")
gender_frame.pack(pady=5)
male_radio = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="#f0f8ff")
female_radio = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="#f0f8ff")
male_radio.pack(side=tk.LEFT)
female_radio.pack(side=tk.LEFT)

height_label = tk.Label(root, text="Height (cm):", font=("Helvetica", 12), bg="#f0f8ff")
height_label.pack(pady=5)
height_entry = tk.Entry(root, font=("Helvetica", 12))
height_entry.pack(pady=5)

weight_label = tk.Label(root, text="Weight (kg):", font=("Helvetica", 12), bg="#f0f8ff")
weight_label.pack(pady=5)
weight_entry = tk.Entry(root, font=("Helvetica", 12))
weight_entry.pack(pady=5)


calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 12), bg="#4CAF50",
                             fg="white")
calculate_button.pack(pady=20)

root.mainloop()