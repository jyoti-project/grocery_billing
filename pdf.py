from fpdf import FPDF
 
 
# save FPDF() class into a
# variable pdf
pdf = FPDF()
 
# Add a page
pdf.add_page()


# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 26)
 
# create a cell
pdf.cell(0,6, txt = "Grocery",ln=1,align='C')
 
pdf.set_font("Arial", size = 10)
# add another cell
pdf.cell(0,9, txt = "Pawan Nagar, Nashik",ln=1,align='C')

pdf.cell(0,0, txt = "Mobile:9146737940",ln=1,align='C')

pdf.cell(0,5, txt = "",ln=1,align='R')
pdf.cell(0,5, txt = "",ln=1,align='R')
pdf.cell(0,5, txt = "",ln=1,align='R')
pdf.cell(0,5, txt = "",ln=1,align='R')
pdf.set_left_margin(30)
pdf.cell(0,5, txt = "Bill No:",ln=1,align='L')
pdf.cell(0,5, txt = "Name:",ln=1,align='L')
pdf.cell(0,5, txt = "Phone No:",ln=1,align='L')
pdf.cell(0,5, txt = "",ln=1,align='R')

data = [['Product','Qty','Price'],
['dakfldhkflbsfoklsbjfbkfb','Smith',34],
['Mary','Ramos',45],[
'Carlson','Banks',19]
]

epw = pdf.w - 2*pdf.l_margin    
col_width = epw/3
th = pdf.font_size
pdf.set_left_margin(30)
for row in data:
   for datum in row:
       # Enter data in colums
       pdf.cell(col_width, 2*th, str(datum), border=1,align='B')
   pdf.ln(2*th)




# save the pdf with name .pdf
pdf.output("D:\Grocery Billing System\mypdf.pdf") 