import camelot
file = "Actilife.pdf"
 
tables = camelot.read_pdf(file, pages = "1-end")
print(tables)