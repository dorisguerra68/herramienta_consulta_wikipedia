from unittest.mock import MagicMock, patch
from src.ai_client.ai_client import AIClient



@patch('src.ai_client.ai_client.Client')
def test_enrich_text(mock_client_class):
    # --- Arrange (Preparar) ---
    # 1. Creamos una instancia falsa del Cliente de Google
    mock_client_instance = MagicMock()
    # 2. llamar la instancia falsa
    mock_client_class.return_value = mock_client_instance

    # 3. Simulamos la  respuesta de Gemini: client.models.generate_content()
    mock_response = MagicMock()
    mock_response.text = "Texto enriquecido por IA"
    mock_client_instance.models.generate_content.return_value = mock_response

    # Inicializamos nuestro AIClient pasándole una clave cualquiera (ya que está mockeado)
    ai_client = AIClient(api_key="fake_api_key")

    # --- Act (Actuar) ---
    # Llamamos
    resultado = ai_client.enrich("Texto original de Wikipedia")

    # --- Assert (Afirmar/Verificar) ---
    # Verificamos que el resultado sea el texto que simulamos
    assert resultado == "Texto enriquecido por IA"

    # Opcional: Verificamos que realmente se haya llamado al método de la IA una vez
    mock_client_instance.models.generate_content.assert_called_once()