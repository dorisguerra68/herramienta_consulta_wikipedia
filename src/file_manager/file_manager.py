import os
from fpdf import FPDF


class FileManager:
    """
    Responsable de guardar contenido en archivos TXT o PDF.
    """

    def save_txt(self, filename: str, content: str):

        if not filename.endswith(".txt"):
            filename += ".txt"

        output_dir = os.path.join(
            os.getcwd(),
            "output"
        )

        os.makedirs(
            output_dir,
            exist_ok=True
        )

        ruta = os.path.join(
            output_dir,
            filename
        )

        with open(ruta, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"TXT guardado en: {ruta}")

        return ruta
# doc. pdf
    class PdfService(FPDF):

        def __init__(self):
            super().__init__()

            # Raíz del proyecto
            base_dir = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)
                )
            )

            # Carpeta de fuentes
            font_dir = os.path.join(
                base_dir,
                "src",
                "fonts",
                "dejavu.ttf"
            )

            print("BASE_DIR:", base_dir)
            print("FONT_DIR:", font_dir)

            # Verificaciones
            regular_font = os.path.join(
                font_dir,
                "DejaVuSans.ttf"
            )

            bold_font = os.path.join(
                font_dir,
                "DejaVuSans-Bold.ttf"
            )

            print("Fuente regular existe:", os.path.exists(regular_font))
            print("Fuente bold existe:", os.path.exists(bold_font))

            if not os.path.exists(regular_font):
                raise FileNotFoundError(
                    f"No se encontró: {regular_font}"
                )

            if not os.path.exists(bold_font):
                raise FileNotFoundError(
                    f"No se encontró: {bold_font}"
                )

            # Registrar fuentes
            self.add_font(
                "DejaVu",
                "",
                regular_font
            )

            self.add_font(
                "DejaVu",
                "B",
                bold_font
            )

            # Configuración PDF
            self.set_margins(left=20, top=20, right=20)
            self.set_auto_page_break(auto=True, margin=20)

            self.COLOR_TEXTO = (40, 40, 40)
            self.COLOR_TITULO = (0, 0, 0)

            self.add_page()
            self.set_font("DejaVu", size=14)

        # -------------------------
        # ENCABEZADO
        # -------------------------

        def header(self):
            pass

        # -------------------------
        # PIE DE PÁGINA
        # -------------------------

        def footer(self):
            pass

        # -------------------------
        # TÍTULO
        # -------------------------

        def add_title(self, title: str):
            self.set_font("DejaVu", "B", 20)
            self.set_text_color(*self.COLOR_TITULO)

            self.cell(
                0,
                12,
                title,
                align="C"
            )

            self.ln(15)

        # -------------------------
        # PÁRRAFOS
        # -------------------------

        def add_paragraph(self, text: str):
            self.set_font("DejaVu", "", 13)
            self.set_text_color(*self.COLOR_TEXTO)

            self.multi_cell(
                0,
                8,
                text
            )

            self.ln(5)

        # -------------------------
        # GUARDAR PDF
        # -------------------------

        def save_pdf(self, filename: str):

            if not filename.endswith(".pdf"):
                filename += ".pdf"

            output_dir = os.path.join(
                os.getcwd(),
                "output"
            )

            os.makedirs(
                output_dir,
                exist_ok=True
            )

            ruta = os.path.join(
                output_dir,
                filename
            )

            self.output(ruta)

            print(f"PDF guardado en: {ruta}")

            return ruta