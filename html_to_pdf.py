import pdfkit
path_wkhtmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_file(r'C:\Users\ADMIN\PycharmProjects\scrapping\test.html','out.pdf',configuration=config)

