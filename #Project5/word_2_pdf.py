import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert as docx_to_pdf
from pdf2docx import Converter
import os

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Word or PDF files", "*.docx *.pdf")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def convert_file():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file.")
        return

    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == ".docx":
            docx_to_pdf(file_path)
            messagebox.showinfo("Success", "Converted DOCX to PDF!")
        elif ext == ".pdf":
            save_path = filedialog.asksaveasfilename(defaultextension=".docx",
                                                     filetypes=[("Word files", "*.docx")])
            if not save_path:
                return
            cv = Converter(file_path)
            cv.convert(save_path)
            cv.close()
            messagebox.showinfo("Success", "Converted PDF to DOCX!")
        else:
            messagebox.showerror("Invalid", "Unsupported file format.")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed:\n{e}")

# === GUI Setup ===
app = tk.Tk()
app.title("Word ⇄ PDF Converter")
app.geometry("400x150")
app.resizable(False, False)

tk.Label(app, text="Select Word or PDF file:").pack(pady=5)

file_entry = tk.Entry(app, width=50)
file_entry.pack(pady=5)

browse_btn = tk.Button(app, text="Browse", command=select_file)
browse_btn.pack(pady=5)

convert_btn = tk.Button(app, text="Convert", command=convert_file)
convert_btn.pack(pady=10)

app.mainloop()
