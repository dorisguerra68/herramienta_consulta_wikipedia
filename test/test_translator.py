from unittest.mock import patch
from src.translator.translator_client import TranslatorClient

@patch("src.translator.translator_client.GoogleTranslator")
def test_translate_text_short(mock_google):
    # Arrange
    instance = mock_google.return_value
    instance.translate.return_value = "Hola mundo"

    client = TranslatorClient()

    # Act
    result = client.translate_text(
        text="Hello world",
        source_language="en",
        target_language="es"
    )

    # Assert
    instance.translate.assert_called()  # ya no usamos assert_called_once
    assert result == "Hola mundo"


@patch("src.translator.translator_client.GoogleTranslator")
def test_translate_text_long(mock_google):
    # Arrange
    
    instance = mock_google.return_value
    instance.translate.return_value = "parte"

    long_text = "a" * 12000  # más de 5000 chars → debe dividir en 3 partes

    client = TranslatorClient()

    # Act
    result = client.translate_text(
        text=long_text,
        source_language="en",
        target_language="es"
    )

    # Assert
    assert instance.translate.call_count == 3
    assert result.count("parte") == 3
