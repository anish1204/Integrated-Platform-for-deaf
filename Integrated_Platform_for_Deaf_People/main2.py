import tkinter as tk
import subprocess


def run_python_file():
    python_file_path = "/Users/Anish/Desktop/Integrated_Platform_for_Deaf_People/Integrated_Platform_for_Deaf_People/MajorProj/inference_classify.py" 
    try:
        subprocess.run(["python", python_file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")

def run_python_file1():
    #C:\Users\Anish\Desktop\Integrated_Platform_for_Deaf_People\Integrated_Platform_for_Deaf_People\mp2.0\two-way-sign-language-translator\main.py
    python_file_path = "/Users/Anish/Desktop/Integrated_Platform_for_Deaf_People/Integrated_Platform_for_Deaf_People/mp2.0/two-way-sign-language-translator/main.py"  
    try:
        subprocess.run(["python", python_file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")


root = tk.Tk()
root.title("Integrated Platform for Deaf People")


root.configure(bg="orange")


window_width = 600  
window_height = 400  
root.geometry(f"{window_width}x{window_height}")
root.resizable(width=False, height=False)


heading_label = tk.Label(root, text="Integrated Platform for Deaf People", font=("Helvetica", 16, "bold"), fg="black", bg="white")
heading_label.pack(pady=100)


button1 = tk.Button(root, text="Hand Recognition", command=run_python_file)
button1.pack(pady=10)

button2 = tk.Button(root, text="Text-to-Sign & Voice-to-Sign", command=run_python_file1)
button2.pack(pady=10)


root.mainloop()
