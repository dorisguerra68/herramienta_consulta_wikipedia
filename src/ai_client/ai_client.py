from google.genai import Client


class AIClient:
    def __init__(self, api_key: str):
        self.client = Client(api_key=api_key)

    def enrich(self, text: str) -> str:
        prompt = (
            "Actúa como un editor experto. Enriquece el siguiente texto de Wikipedia. "
            "Mejora su claridad, estructura y profundidad:\n\n"
            f"{text}"
        )

        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text if response.text else "No se pudo generar el contenido."

        except Exception as e:
            # Reenviamos el error hacia arriba para que ContentEnricher lo procese
            raise e