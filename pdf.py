import PyPDF2

def pdfreader(speak):
    file_path = input("Enter the path of the file")
    book = open(file_path,'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("Sir please enter the total number of pages i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfreader.getPage(pg)
    text = page.extract_text()
    speak(text)