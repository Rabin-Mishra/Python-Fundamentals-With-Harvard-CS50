import os
from tkinter import Tk, filedialog
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from PyPDF2 import PdfMerger

# Function to convert .docx file to PDF using ReportLab


def convert_docx_to_pdf(docx_file, output_pdf):
    doc = Document(docx_file)
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter  # Size of the page

    # Set the font and size for the PDF
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.black)

    y_position = height - 40  # Start from the top of the page

    # Loop through paragraphs in the docx file
    for para in doc.paragraphs:
        if y_position < 40:  # If the text is going out of the page, create a new page
            c.showPage()  # Starts a new page
            c.setFont("Helvetica", 10)
            y_position = height - 40

        # Handle unsupported characters by replacing them with simpler characters
        # Replace en dash and em dash
        para_text = para.text.replace('\u2013', '-').replace('\u2014', '--')
        para_text = para_text.replace('\u2018', "'").replace(
            '\u2019', "'")  # Replace smart quotes
        para_text = para_text.replace('\u201C', '"').replace(
            '\u201D', '"')  # Replace smart quotes with double quotes

        c.drawString(40, y_position, para_text)
        y_position -= 12  # Move down for the next line

    c.save()  # Save the PDF

# Function to convert multiple .docx files and merge them into one PDF


def convert_and_merge_docs(docx_files, output_pdf):
    pdfs = []

    # Convert each .docx file to a PDF and store the output
    for docx_file in docx_files:
        temp_pdf = f"temp_{os.path.basename(docx_file)}.pdf"
        convert_docx_to_pdf(docx_file, temp_pdf)
        pdfs.append(temp_pdf)

    # Merge PDFs using PyPDF2
    merger = PdfMerger()

    for pdf_file in pdfs:
        merger.append(pdf_file)
        os.remove(pdf_file)  # Clean up temporary files

    # Write the merged output to the final PDF
    merger.write(output_pdf)
    merger.close()

# Function to open file dialog and select .docx files


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
