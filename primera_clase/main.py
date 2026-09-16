# Proyecto 01
# Generar automáticamente PDFs con Python
# Generando archivo PDF del presupuesto del proyecto con Python
from fpdf import FPDF
from datetime import date

# Crear un objeto PDF con una clase propia para poder definir header y footer
class PDFPresupuesto(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Presupuesto de Proyecto", ln=True, align="C")
        self.set_font("Arial", "I", 10)
        self.cell(0, 8, f"Generado el {date.today().strftime('%d/%m/%Y')}", ln=True, align="C")
        self.ln(5)
        self.line(10, self.get_y(), 200, self.get_y())  # línea separadora
        self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")


# --- Datos ingresados por el usuario ---
nombre_proyecto = input("Ingrese el nombre del proyecto: ")
horas_estimadas = input("Ingrese las horas estimadas para el proyecto: ")
valor_hora = input("Ingrese el valor por hora: USD ")
plazo_estimado = input("Ingrese el plazo estimado para el proyecto: ")

# Conversión de tipos para poder operar matemáticamente
precio_total = int(horas_estimadas) * float(valor_hora)

# --- Construcción del PDF ---
pdf = PDFPresupuesto()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Tabla de datos: cada fila es una etiqueta + un valor
filas = [
    ("Nombre del Proyecto:", nombre_proyecto),
    ("Horas estimadas:", f"{horas_estimadas} hs"),
    ("Valor por hora:", f"USD {valor_hora}"),
    ("Plazo estimado:", plazo_estimado),
]

for etiqueta, valor in filas:
    pdf.set_font("Arial", "B", 12)
    pdf.cell(60, 10, etiqueta, border=0)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, valor, ln=True)

pdf.ln(5)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(8)

# Precio total destacado
pdf.set_font("Arial", "B", 14)
pdf.set_text_color(0, 102, 51)  # verde
pdf.cell(0, 10, f"Precio Total: USD {precio_total:.2f}", ln=True)
pdf.set_text_color(0, 0, 0)  # vuelve a negro por si agregás más texto después

# nombre del archivo PDF
pdf.output("presupuesto_proyecto.pdf")
print("PDF generado correctamente: presupuesto_proyecto.pdf")