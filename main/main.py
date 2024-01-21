import pyttsx3
import PyPDF2

book = open("AI.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)  # Use len(pdfReader.pages) to get the number of pages.
print(pages)

page_number = 7  # Choose the page number you want to extract.
page = pdfReader.pages[page_number]  # Get the specified page of the PDF.

text = ""  # Initialize an empty string to store the text from the PDF.
for element in page:
    if isinstance(element, PyPDF2.generic.TextStringObject):
        text += element

speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()

#book.close()  # Close the PDF file when done.
