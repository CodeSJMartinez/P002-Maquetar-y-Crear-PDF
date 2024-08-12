Este código de Python se encarga de crear un documento PDF que sirve como guía para donar ropa a la organización "Boa Vida". Utiliza la biblioteca fpdf para generar el PDF.

Corresponde a un ejemplo completo de cómo usar la biblioteca fpdf en Python para crear un documento PDF con un formato personalizado, incluyendo encabezados, pies de página, títulos de capítulos, cuerpos de texto, e imágenes.

Para que este programa funcione correctamente, necesitarás asegurarte de tener instalado Python en tu sistema y también instalar algunas bibliotecas adicionales. Aquí te guío paso a paso sobre lo que debes hacer:

## 1. Instalar Python
Asegúrate de tener Python instalado en tu sistema. Puedes verificar esto abriendo una terminal o línea de comandos (cmd) y escribiendo:

bash
```
python --version
```
Si no tienes Python instalado, puedes descargarlo e instalarlo desde python.org.

## 2. Instalar la biblioteca fpdf
La biblioteca fpdf es necesaria para generar los PDFs. Para instalarla, usa el siguiente comando en la línea de comandos:

bash
```
pip install fpdf
```

## 3. Instalar otras bibliotecas necesarias
Si decides usar otros formatos de imagen como PNG o JPEG, es posible que necesites instalar bibliotecas adicionales para manejar estos formatos. Sin embargo, el fpdf se encarga de la mayoría de los casos de uso sin necesidad de librerías extra para este tipo de imagen.

## 4. Crear Directorios para Almacenar Imágenes y PDF
Asegúrate de tener los directorios correctos para almacenar las imágenes y el PDF generado. Puedes crear estos directorios manualmente:

bash
``` 
mkdir img
mkdir pdf
```

Coloca las imágenes necesarias (como img/logo.png y img/imagen01.jpeg) dentro del directorio img.

## 5. Verificar el Código
Asegúrate de que el código que estás ejecutando se encuentra en un archivo .py. Por ejemplo, podrías llamarlo generar_pdf.py.

## 6. Ejecutar el Programa
Finalmente, ejecuta el script en tu terminal o línea de comandos desde el directorio donde se encuentra el archivo .py:

bash
``` 
python generar_pdf.py
```

Esto generará un PDF en el directorio pdf con el nombre Guía-para-donar-ropa-a-Boa-Vida.pdf, si el código se ejecuta correctamente.

Resumen de Comandos
Aquí tienes un resumen rápido de los comandos que necesitas ejecutar en el CMD para que el programa funcione:

bash
``` 
pip install fpdf
mkdir img
mkdir pdf
```

Asegúrate de ajustar cualquier ruta de archivo o imagen en el código para que apunten a las ubicaciones correctas en tu sistema.

# Explicación Paso a Paso

Vamos a descomponerlo y entender cada parte:

## 1. Importar la Biblioteca Necesaria

python
``` 
from fpdf import FPDF
```

*from fpdf import FPDF:* Estamos importando la clase FPDF desde el módulo fpdf. Esta clase nos permite crear documentos PDF.

## 2. Configuración del Estilo
python
```
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
```

*Diccionario style_config:* Es una estructura que almacena las configuraciones de estilo para diferentes partes del PDF, como el encabezado (header), el pie de página (footer), y los capítulos (chapter).

*header:* Define la imagen del logo, el texto del título, la fuente, y los colores de fondo y de texto para el encabezado.

*footer:* Establece la fuente y el color del texto para el pie de página.

*chapter:* Configura la fuente, el color del título y del cuerpo del texto para los capítulos.

## 3. Clase PDF Personalizada
python
``` 
class PDF(FPDF):
    def __init__(self, style):
        super().__init__()
        self.style = style
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(left=10, top=30, right=10)
```

*Clase PDF:* Esta clase hereda de FPDF y se usa para personalizar la forma en que se crea el PDF.

*__init__:* Inicializa la clase y establece las configuraciones básicas.

*super().__init__():* Llama al constructor de la clase padre (FPDF) para inicializar correctamente.

*self.style = style:* Almacena el estilo pasado como argumento.

*self.set_auto_page_break(auto=True, margin=20):* Configura un salto de página automático con un margen de 20 unidades.

*self.set_margins(left=10, top=30, right=10):* Establece los márgenes del documento.

## 4. Método header
python
```
def header(self):
    if self.page_no() == 1:
        logo_path = self.style['header']['logo_path']
        logo_width = self.style['header']['logo_width']
        self.image(logo_path, x=(self.w - logo_width) / 2, y=15, w=logo_width)
        self.ln(20)

        title_text = self.style['header']['title_text']
        title_font = self.style['header']['title_font']
        title_fill_color = self.style['header']['title_fill_color']
        title_text_color = self.style['header']['title_text_color']

        self.set_fill_color(*title_fill_color)
        self.set_text_color(*title_text_color)
        self.set_font(*title_font)
        self.cell(0, 12, title_text, 0, 1, 'C', fill=True)
        self.ln(5)
```

*header(self):* Este método define el contenido del encabezado de la primera página.

*if self.page_no() == 1:* Verifica si la página actual es la primera. Si es así, agrega el logo y el título.

*self.image(...):* Inserta una imagen (el logo) en el encabezado.

*self.cell(...):* Crea una celda que contiene el título con un fondo de color (fill=True).

## 5. Método footer
python
``` 
def footer(self):
    self.set_y(-20)
    footer_font = self.style['footer']['font']
    footer_text_color = self.style['footer']['text_color']
    self.set_font(*footer_font)
    self.set_text_color(*footer_text_color)

    page_text = 'https://boavida.org/servizo-de-recollida-e-transporte/ - Página {}'.format(self.page_no())
    self.cell(0, 10, page_text, 0, 0, 'C')
```

*footer(self):* Define el contenido del pie de página.

*self.set_y(-20):* Coloca el cursor de escritura a 20 unidades desde el final de la página.

*self.cell(...):* Crea una celda que contiene el texto del pie de página y el número de página actual.

## 6. Método chapter_title
python
```
def chapter_title(self, title):
    title_font = self.style['chapter']['title_font']
    title_fill_color = self.style['chapter']['title_fill_color']
    title_text_color = self.style['chapter']['title_text_color']

    self.set_fill_color(*title_fill_color)
    self.set_text_color(*title_text_color)
    self.set_font(*title_font)
    self.cell(0, 10, title, 0, 1, 'L', fill=True)
    self.ln(2)
```

*chapter_title(self, title):* Añade un título de capítulo al PDF.

*self.cell(...):* Crea una celda que contiene el título del capítulo con un fondo de color.

## 7. Método chapter_body
python
``` 
def chapter_body(self, body, image_path=None):
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
            self.multi_cell(text_width - 5, 6, line, align='L')

    final_y_position = max(self.get_y(), image_height)
    self.set_y(final_y_position + 4)

    self.cell(0, 0, '', 'T', 1, 'C')
    self.ln(4)
```

*chapter_body(self, body, image_path=None):* Agrega el contenido de un capítulo.

*self.multi_cell(...):* Escribe varias líneas de texto. Se usa para el cuerpo del texto y para los puntos destacados.

*if image_path::* Si se proporciona una ruta de imagen, la inserta al lado del texto.

*self.set_xy(x_initial, y_initial):* Asegura que el texto y la imagen comiencen en la posición inicial definida.

## 8. Crear un Documento PDF
python
```
pdf = PDF(style_config)
pdf.add_page()
```

*pdf = PDF(style_config):* Crea una instancia de la clase PDF con la configuración de estilo definida.

*pdf.add_page():* Añade una nueva página al documento PDF.

## 9. Añadir Contenido al PDF
python
```
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
        "image": "img/imagen01.jpeg"
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
    ...
}

for title, details in content.items():
    pdf.chapter_title(title)
    pdf.chapter_body('\n'.join(details["text"]), image_path=details.get("image"))
```
    
*content*: Un diccionario que contiene los títulos de los capítulos y el texto asociado a cada uno, junto con las imágenes opcionales.

*for title, details in content.items():*: Itera sobre el contenido para agregar cada capítulo al PDF.

*pdf.chapter_title(title)*: Añade el título de cada capítulo.

*pdf.chapter_body(...)*: Añade el texto y la imagen de cada capítulo.

## 10. Guardar el PDF
python
```
pdf_output = 'pdf/Guía-para-donar-ropa-a-Boa-Vida.pdf'
pdf.output(pdf_output)
```

*pdf_output = 'pdf/Guía-para-donar-ropa-a-Boa-Vida.pdf':* Define la ruta donde se guardará el PDF.

*pdf.output(pdf_output):* Genera y guarda el PDF en la ruta especificada.

