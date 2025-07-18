import pandas as pd
from fpdf import FPDF

df = pd.read_csv('data.csv')

total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
max_sales = df['Sales'].max()
max_sales_person = df.loc[df['Sales'].idxmax(), 'Name']

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Sales Report", ln=True, align='C')

pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(0, 10, f"Total Sales: {total_sales}", ln=True)
pdf.cell(0, 10, f"Average Sales: {average_sales:.2f}", ln=True)
pdf.cell(0, 10, f"Top Salesperson: {max_sales_person} ({max_sales})", ln=True)

pdf.ln(10)

pdf.set_font("Arial", 'B', 12)
pdf.cell(40, 10, "Name", border=1)
pdf.cell(40, 10, "Sales", border=1)
pdf.cell(40, 10, "Region", border=1)
pdf.ln()

pdf.set_font("Arial", size=12)
for index, row in df.iterrows():
    pdf.cell(40, 10, str(row['Name']), border=1)
    pdf.cell(40, 10, str(row['Sales']), border=1)
    pdf.cell(40, 10, str(row['Region']), border=1)
    pdf.ln()

pdf.output("sales_report.pdf")

print("PDF report generated: sales_report.pdf")
