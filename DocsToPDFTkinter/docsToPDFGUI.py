import os
from tkinter import Tk, filedialog
from docx import Document
from fpdf import FPDF
from PyPDF2 import PdfMerger

# Function to convert a .docx file to PDF


def convert_docx_to_pdf(docx_file, output_pdf):
    doc = Document(docx_file)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set font for PDF, use a font that supports more characters (e.g., Arial Unicode MS)
    pdf.add_font('ArialUnicode', '', 'C:/Windows/Fonts/arialuni.ttf',
                 uni=True)  # Path to Arial Unicode font
    pdf.set_font("ArialUnicode", size=12)

    # Loop through paragraphs in the docx file
    for para in doc.paragraphs:
        # Handle unsupported characters by replacing them (optional)
        # Replace en dash and em dash with normal dash
        para_text = para.text.replace('\u2013', '-').replace('\u2014', '--')
        pdf.multi_cell(0, 10, para_text)

    pdf.output(output_pdf)

# Function to convert multiple .docx files and merge them into one PDF


def convert_and_merge_docs(docx_files, output_pdf):
    pdfs = []

    # Convert each docx file to a PDF and store it in the list
    for docx_file in docx_files:
        temp_pdf = f"temp_{os.path.basename(docx_file)}.pdf"
        convert_docx_to_pdf(docx_file, temp_pdf)
        pdfs.append(temp_pdf)

    # Use PdfMerger to merge PDFs
    merger = PdfMerger()

    for pdf_file in pdfs:
        merger.append(pdf_file)
        os.remove(pdf_file)  # Remove temporary PDF files after merging

    # Write the merged output
    merger.write(output_pdf)
    merger.close()

# Function to open file dialog and select files


def select_files():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(
        title="Select .docx files", filetypes=[("Word Documents", "*.docx")])
    return list(file_paths)

# Main function to start the process


def main():
    # Select the .docx files using a GUI
    docx_files = select_files()

    if docx_files:
        output_pdf = "merged_output.pdf"
        convert_and_merge_docs(docx_files, output_pdf)
        print(f"PDF successfully created and saved as {output_pdf}")
    else:
        print("No files selected!")


# Run the program
if __name__ == "__main__":
    main()
