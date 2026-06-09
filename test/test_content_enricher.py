from unittest.mock import MagicMock
from src.content_enricher.content_enricher import ContentEnricher

def test_enrich_calls_ai_client():
    # Arrange: creamos un AIClient falso
    mock_ai_client = MagicMock()
    mock_ai_client.enrich_text.return_value = "Texto enriquecido"

    enricher = ContentEnricher(ai_client=mock_ai_client)

    # Act: llamamos al método enrich
    result = enricher.enrich("Texto original")

    # Assert: verificamos comportamiento
    mock_ai_client.enrich_text.assert_called_once_with("Texto original")
    assert result == "Texto enriquecido"
