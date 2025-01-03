import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document
import fitz  # PyMuPDF
import os


def select_pdf():
    filepath = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    pdf_path_var.set(filepath)


def save_docx():
    filepath = filedialog.asksaveasfilename(
        title="Save DOCX File",
        defaultextension=".docx",
        filetypes=[("Word Files", "*.docx")]
    )
    docx_path_var.set(filepath)


def convert_pdf_to_docx():
    pdf_path = pdf_path_var.get()
    docx_path = docx_path_var.get()

    if not pdf_path or not os.path.exists(pdf_path):
        messagebox.showerror("Error", "Please select a valid PDF file.")
        return

    if not docx_path:
        messagebox.showerror(
            "Error", "Please specify a save location for the DOCX file.")
        return

    try:
        doc = Document()
        pdf_document = fitz.open(pdf_path)

        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text = page.get_text("text")
            doc.add_paragraph(text)

        doc.save(docx_path)
        messagebox.showinfo("Success", "PDF successfully converted to DOCX.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def create_gui():
    root = tk.Tk()
    root.title("PDF to DOCX Converter")

    global pdf_path_var, docx_path_var
    pdf_path_var = tk.StringVar()
    docx_path_var = tk.StringVar()

    # PDF Selection
    tk.Label(root, text="Select PDF File:").grid(
        row=0, column=0, padx=10, pady=10, sticky="w")
    tk.Entry(root, textvariable=pdf_path_var, width=50).grid(
        row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=select_pdf).grid(
        row=0, column=2, padx=10, pady=10)

    # DOCX Save Location
    tk.Label(root, text="Save DOCX File As:").grid(
        row=1, column=0, padx=10, pady=10, sticky="w")
    tk.Entry(root, textvariable=docx_path_var, width=50).grid(
        row=1, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=save_docx).grid(
        row=1, column=2, padx=10, pady=10)

    # Convert Button
    tk.Button(root, text="Convert", command=convert_pdf_to_docx,
              bg="green", fg="white").grid(row=2, column=1, pady=20)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
