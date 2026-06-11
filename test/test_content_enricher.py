from unittest.mock import MagicMock
from src.content_enricher.content_enricher import ContentEnricher


def test_enrich_calls_ai_client():
    mock_ai_client = MagicMock()
    mock_ai_client.enrich.return_value = "Texto enriquecido"

    enricher = ContentEnricher(ai_client=mock_ai_client)

    result = enricher.enrich("Texto original")

    mock_ai_client.enrich.assert_called_once_with("Texto original")
    assert result == "Texto enriquecido"


def test_enrich_handles_404_error():
    mock_ai_client = MagicMock()
    mock_ai_client.enrich.side_effect = Exception("404 Model not found")

    enricher = ContentEnricher(ai_client=mock_ai_client)

    result = enricher.enrich("Texto original")

    assert "[Error 404 - ContentEnricher]" in result
    assert "modelo de IA solicitado no existe" in result


def test_enrich_handles_503_error():
    mock_ai_client = MagicMock()
    mock_ai_client.enrich.side_effect = Exception("503 Service Unavailable")

    enricher = ContentEnricher(ai_client=mock_ai_client)

    result = enricher.enrich("Texto original")

    assert "[Error 503 - ContentEnricher]" in result
    assert "servidores de Google están saturados" in result


def test_enrich_handles_unexpected_error():
    mock_ai_client = MagicMock()
    mock_ai_client.enrich.side_effect = Exception("Error inesperado")

    enricher = ContentEnricher(ai_client=mock_ai_client)

    result = enricher.enrich("Texto original")

    assert "[Error Inesperado - ContentEnricher]" in result
    assert "Error inesperado" in result
