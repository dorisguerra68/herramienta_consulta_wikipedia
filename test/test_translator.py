from unittest.mock import patch
from src.translator.translator_client import TranslatorClient

@patch("src.translator.translator_client.GoogleTranslator")
def test_translate_text(mock_google):
    # Arrange
    instance = mock_google.return_value
    instance.translate.return_value = "Hola mundo"

    # Act
    client = TranslatorClient()
    result = client.translate_text(
        text="Hello world",
        source_language="en",
        target_language="es"
    )

    # Assert
    instance.translate.assert_called_once_with("Hello world")
    assert result == "Hola mundo"
