from fpdf import FPDF

class FileManager:
    """
    Responsable de guardar contenido en archivos TXT o PDF.
    """

    def save_txt(self, filename: str, content: str):
        if not filename.endswith(".txt"):
            filename += ".txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    def save_pdf(self, filename: str, content: str):
        if not filename.endswith(".pdf"):
            filename += ".pdf"

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        for line in content.split("\n"):
            pdf.multi_cell(0, 10, line)

        pdf.output(filename)
