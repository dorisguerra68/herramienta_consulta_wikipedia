from unittest.mock import mock_open, patch, MagicMock
from src.file_manager.file_manager import FileManager

def test_save_txt_adds_extension_and_writes_file():
    fm = FileManager()

    with patch("builtins.open", mock_open()) as mocked_file:
        fm.save_txt("archivo", "contenido")

        mocked_file.assert_called_once_with("archivo.txt", "w", encoding="utf-8")
        mocked_file().write.assert_called_once_with("contenido")


def test_save_pdf_adds_extension_and_calls_fpdf_output():
    fm = FileManager()

    with patch("src.file_manager.file_manager.FPDF") as MockPDF:
        mock_pdf_instance = MagicMock()
        MockPDF.return_value = mock_pdf_instance

        fm.save_pdf("archivo", "linea1\nlinea2")

        MockPDF.assert_called_once()
        mock_pdf_instance.add_page.assert_called_once()
        mock_pdf_instance.output.assert_called_once_with("archivo.pdf")
