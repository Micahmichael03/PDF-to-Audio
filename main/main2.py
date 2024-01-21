import pyttsx3
import PyPDF2

book = open("AI.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)  # Use len(pdfReader.pages) to get the number of pages.
print(pages)

speaker = pyttsx3.init()
text = ""  # Initialize an empty string to store the text from the PDF.
for page in pdfReader.pages:
    text += page.extract_text()  # Extract text from each page and add it to the text variable.


speaker.say(text)  # Speak the text.
speaker.runAndWait()
book.close()  # Close the PDF file when done.
