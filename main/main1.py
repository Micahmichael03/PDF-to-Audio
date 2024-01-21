import pyttsx3
import PyPDF2

# Open the PDF file
with open("AI.pdf", "rb") as book:
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)  # Use len to get the number of pages
    print(pages)

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Say "Hello World"
speaker.say("Hello World")
speaker.runAndWait()
