# Import the pyttsx3 library for text-to-speech and PyPDF2 library for PDF manipulation
import pyttsx3
import PyPDF2

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Open the PDF file in binary mode and create a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(open("AI.pdf", "rb"))
text = ""

# Iterate through the pages of the PDF (starting from page 6) and extract text
for page_number in range(6, pdfReader.numPages):
    page = pdfReader.getPage(page_number)
    text += page.extractText()

    # Speak the extracted text using the text-to-speech engine
    speaker.say(text)
    speaker.runAndWait()

# Stop the text-to-speech engine
speaker.stop()

# Save the spoken text to an MP3 file
speaker.save_to_file(text, "output.mp3")
speaker.runAndWait()

# Additional commented-out lines for reference or debugging:
# print(pdfReader.numPages)  # Print the total number of pages in the PDF
# speaker.say(f'The number of pages in the PDF is {pdfReader.numPages} pages.')  # Speak the number of pages
# speaker.runAndWait()
