from fpdf import FPDF

from Charts import CreateChart


#wykres =CreateChart
wykres = CreateChart.add_new()
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)
pdf.cell(40,10,txt = "to jest plik pdf", ln=2, align='C')
pdf.image(wykres,0,30)
pdf.output("nowypdf.pdf")
