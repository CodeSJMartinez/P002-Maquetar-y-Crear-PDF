from fpdf import FPDF

# Style configuration dictionary for easy modification
style_config = {
    'header': {
        'logo_path': 'img/logo.png',
        'logo_width': 33,
        'title_text': 'Guía para Donar Ropa a Boa Vida',
        'title_font': ('Arial', 'B', 16),
        'title_fill_color': (0, 31, 63),
        'title_text_color': (255, 255, 255)
    },
    'footer': {
        'font': ('Arial', 'I', 10),
        'text_color': (128,)
    },
    'chapter': {
        'title_font': ('Arial', 'B', 14),
        'title_fill_color': (230, 230, 250),
        'title_text_color': (0, 31, 63),
        'body_font': ('Arial', '', 12),
        'body_text_color': (50, 50, 50),
        'sub_point_color': (0, 31, 63)
    }
}

class PDF(FPDF):
    def __init__(self, style):
        super().__init__()
        self.style = style
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(left=10, top=30, right=10)

    def header(self):
        # Only display the header on the first page
        if self.page_no() == 1:
            # Center the temporary logo image at the top of the page
            logo_path = self.style['header']['logo_path']
            logo_width = self.style['header']['logo_width']
            self.image(logo_path, x=(self.w - logo_width) / 2, y=15, w=logo_width)
            self.ln(20)

            # Title configuration
            title_text = self.style['header']['title_text']
            title_font = self.style['header']['title_font']
            title_fill_color = self.style['header']['title_fill_color']
            title_text_color = self.style['header']['title_text_color']

            self.set_fill_color(*title_fill_color)
            self.set_text_color(*title_text_color)
            self.set_font(*title_font)
            self.cell(0, 12, title_text, 0, 1, 'C', fill=True)
            self.ln(5)

    def footer(self):
        self.set_y(-20)
        footer_font = self.style['footer']['font']
        footer_text_color = self.style['footer']['text_color']
        self.set_font(*footer_font)
        self.set_text_color(*footer_text_color)

        page_text = 'https://boavida.org/servizo-de-recollida-e-transporte/ - Página {}'.format(self.page_no())
        self.cell(0, 10, page_text, 0, 0, 'C')

    def chapter_title(self, title):
        # Chapter title configuration
        title_font = self.style['chapter']['title_font']
        title_fill_color = self.style['chapter']['title_fill_color']
        title_text_color = self.style['chapter']['title_text_color']

        self.set_fill_color(*title_fill_color)
        self.set_text_color(*title_text_color)
        self.set_font(*title_font)
        self.cell(0, 10, title, 0, 1, 'L', fill=True)
        self.ln(2)

    def chapter_body(self, body, image_path=None):
        # Body text configuration
        body_font = self.style['chapter']['body_font']
        body_text_color = self.style['chapter']['body_text_color']
        sub_point_color = self.style['chapter']['sub_point_color']

        self.set_font(*body_font)
        self.set_text_color(*body_text_color)

        text_width = 0.62 * self.w
        image_width = 0.20 * self.w
        image_height = 0

        x_initial = self.get_x()
        y_initial = self.get_y()

        if image_path:
            self.set_xy(x_initial + text_width + 10, y_initial)
            self.image(image_path, x=self.get_x(), y=self.get_y(), w=image_width)
            image_height = self.get_y() + (image_width * (3 / 2))

        self.set_xy(x_initial, y_initial)
        lines = body.split('\n')

        for line in lines:
            self.set_x(x_initial)
            if ':' in line:
                self.set_font('Arial', 'B', 12)
                self.multi_cell(text_width, 10, line, align='L')
            else:
                self.set_x(x_initial + 5)
                self.set_font('Arial', '', 12)
                self.set_text_color(*sub_point_color)
                self.cell(5, 6, '-', ln=0, align='L')
                self.set_text_color(*body_text_color)
                self.multi_cell(text_width - 5, 6, line, align='L')  #origin -5, 8

        final_y_position = max(self.get_y(), image_height)
        self.set_y(final_y_position + 4)

        self.cell(0, 0, '', 'T', 1, 'C')
        self.ln(4)


# Create a PDF document
pdf = PDF(style_config)
pdf.add_page()

# Add content to the PDF
content = {
    "1. Revisión del Armario": {
        "text": [
            "Clasificación Inicial:",
            "Dedica tiempo a revisar todo tu armario.",
            "Separa la ropa que ya no usas en dos pilas; 'Para donar' y 'Para revisar más tarde'.",
            "Revisa cada prenda en busca de daños como manchas, agujeros o desgaste.",
            "Frecuencia de Uso:",
            "Considera cuánto tiempo ha pasado desde la última vez que usaste la prenda.",
            "Si no la has usado en más de un año, es un buen candidato para donar.",
        ],
        "image": "img/imagen01.jpeg"  # Add your image path here
    },
    "2. Calidad de la Prenda": {
        "text": [
            "Estado General:",
            "Examina cada prenda para asegurarte de que está en buen estado.",
            "Verifica que no haya agujeros, manchas permanentes, o decoloración significativa.",
            "Integridad de Costuras y Cierres:",
            "Asegúrate de que las costuras no estén desgastadas ni deshilachadas.",
            "Prueba los cierres, botones y cremalleras para ver si funcionan correctamente.",
            "Olor y Limpieza:",
            "Todas las prendas deben estar limpias y sin olores fuertes.",
            "Revisa los bolsillos y, si es posible, lava la ropa antes de donarla para que llegue en óptimas condiciones."
        ],
    },
    "3. Criterios de Selección por Tipo de Prenda": {
        "text": [
            "Ropa Usada en Buen Estado:",
            "Ideal para donar si está libre de daños y bien cuidada.",
            "La selección podría incluir ropa para hombres, mujeres y niños.",
            "Ropa Nueva Sin Estrenar:",
            "Perfecta para donar, especialmente si no planeas usarla.",
            "Asegúrate de que la prenda esté completa, con etiquetas si es posible.",
            "Ropa de Temporada:",
            "Considera las estaciones, donar ropa de invierno en otoño o ropa de verano en primavera es útil para quienes la necesiten."
        ],
        "image": "img/Ropa.jpeg"  
    },
    "4. Qué No Donar": {
        "text": [
            "Prendas en Mal Estado:",
            "Ropa con roturas grandes, manchas imposibles de quitar, o decoloración evidente.",
            "Calcetines dañados y ropa interior usados.",
            "Ropa Irreparable:",
            "Si el arreglo de la prenda costaría más que su valor, es mejor no donarla.",
            "Ropa que No es Adecuada:",
            "Artículos extremadamente personalizados o prendas con daños estructurales graves, que no pueden ser reparadas fácilmente."
        ],
    },
    "5. Preparación de la Donación": {
        "text": [
            "Organiza la Ropa:",
            "Dobla y clasifica las prendas por tipo y estación.",
            "Utiliza cajas o bolsas resistentes para el transporte.",
            "Comunicación con Boa Vida:",
            "Llama o visita Boa Vida para conocer sus necesidades actuales y confirmar horarios de recepción de donaciones."
        ],
        "image": "img/imagen02.jpeg"  # Add your image path here
    },
    "6. Beneficios de Donar a Boa Vida": {
        "text": [
            "Impacto Ambiental:",
            "Contribuyes a reducir el desperdicio textil y el impacto ambiental al dar una segunda vida a la ropa.",
            "Apoyo a la Comunidad:",
            "Ayudas a proporcionar ropa de calidad a precios accesibles para quienes la necesiten.",
            "Valor Social:",
            "Participas en una iniciativa que fomenta la sostenibilidad y la responsabilidad social."
        ],
    },
    "7. Notas Finales": {
        "text": [
            "Consumo Responsable:",
            "Reflexiona sobre tus hábitos de compra para reducir la acumulación de ropa en el futuro.",
            "Considera opciones sostenibles como la compra de segunda mano o la reutilización creativa de prendas.",
            "Cada prenda cuenta, cada gesto importa; reduce, recicla, ¡vamos a donar!",
        ],
        "image": "img/qrcode.png"    
    },
}

# Add chapters to the PDF
for title, details in content.items():
    pdf.chapter_title(title)
    pdf.chapter_body('\n'.join(details["text"]), image_path=details.get("image"))

# Save the PDF 
pdf_output = 'pdf/Guía-para-donar-ropa-a-Boa-Vida.pdf'
pdf.output(pdf_output)

pdf_output
