from unittest.mock import MagicMock
from src.ai_client.ai_client import AIClient

def test_enrich_text():
    # Arrange: creamos un modelo falso (mock)
    mock_model = MagicMock()

    # Simulamos la respuesta del modelo
    mock_response = MagicMock()
    mock_response.text = "Texto enriquecido"
    mock_model.generate_content.return_value = mock_response

    client = AIClient(model=mock_model)

    # Act: llamamos al método que queremos probar
    result = client.enrich_text("Texto original")

    # Assert: verificamos comportamiento
    mock_model.generate_content.assert_called_once()
    assert result == "Texto enriquecido"
