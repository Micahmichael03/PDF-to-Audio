# import pyttsx3
# import PyPDF2
# import pdfplumber

# file = 'AI.pdf'
# file = open(file, 'rb')

# reader = PyPDF2.PdfReader(file)
# pages = len(reader.pages)
# with pdfplumber.open(file) as pdf:
#     for i in range(7, pages):
#         page = pdf.pages[i]
#         text = page.extract_text()
#         print(text)

# speaker = pyttsx3.init()
# speaker.save_to_file(text, 'C:/Users/Admin/Documents/AI with Python/pdf-audiobooks/output.mp3')
# speaker.runAndWait() 
# file.close()