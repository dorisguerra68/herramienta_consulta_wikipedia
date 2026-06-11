# src/content_enricher/content_enricher.py
from src.ai_client.ai_client import AIClient


class ContentEnricher:
    def __init__(self, ai_client: AIClient):
        self.ai_client = ai_client

    def enrich(self, text: str) -> str:
        try:
            # Intentamos llamar al cliente de IA
            return self.ai_client.enrich(text)

        except Exception as e:
            error_msg = str(e)

            # --- Gestión del Error 404 (Modelo no encontrado) ---
            if "404" in error_msg:
                return (
                    "\n[Error 404 - ContentEnricher]: El modelo de IA solicitado no existe o "
                    "no está disponible en esta versión de la API. Por favor, verifica el nombre "
                    "del modelo en ai_client.py (ej. usa 'gemini-2.5-flash')."
                )

            # --- Gestión del Error 503 (Servidor Saturado) ---
            elif "503" in error_msg:
                return (
                    "\n[Error 503 - ContentEnricher]: Los servidores de Google están saturados en "
                    "este momento. Por favor, inténtalo de nuevo en unos minutos."
                )

            # --- Cualquier otro error inesperado ---
            else:
                return f"\n[Error Inesperado - ContentEnricher]: {error_msg}"