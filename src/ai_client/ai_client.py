from google.genai import Client

class AIClient:
    """
    Cliente responsable de comunicarse con el modelo de IA para enriquecer texto.
    """

    def __init__(self, api_key: str):
        # Creamos el cliente oficial de Gemini
        self.client = Client(api_key=api_key)

    def enrich_text(self, text: str) -> str:
        """
        Envía el texto al modelo de IA y devuelve una versión enriquecida.
        """
        prompt = (
            "Enriquece el siguiente texto manteniendo el significado original, "
            "mejorando claridad, estructura y profundidad:\n\n"
            f"{text}"
        )

        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text
