class AIClient:
    """
    Cliente responsable de comunicarse con el modelo de IA para enriquecer texto.
    El modelo se inyecta desde fuera para facilitar pruebas y desacoplar dependencias.
    """

    def __init__(self, model):
        self.model = model

    def enrich_text(self, text: str) -> str:
        """
        Envía el texto al modelo de IA y devuelve una versión enriquecida.
        """
        prompt = (
            "Enriquece el siguiente texto manteniendo el significado original, "
            "mejorando claridad, estructura y profundidad:\n\n"
            f"{text}"
        )

        response = self.model.generate_content(prompt)
        return response.text
