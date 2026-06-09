class ContentEnricher:
    """
    Orquestador que usa AIClient para enriquecer contenido.
    """

    def __init__(self, ai_client):
        self.ai_client = ai_client

    def enrich(self, text: str) -> str:
        """
        Enriquecer texto usando el cliente de IA.
        """
        enriched_text = self.ai_client.enrich_text(text)
        return enriched_text
