class InputValidator:
    SUPPORTED_LANGUAGES = {"es", "en", "fr", "de", "it", "pt"}

    @staticmethod
    def validate_topic(topic: str) -> str:
        topic = topic.strip()
        if not topic:
            raise ValueError("El tema no puede estar vacío")
        return topic

    @staticmethod
    def validate_language(language: str) -> str:
        lang = language.strip().lower()
        if lang not in InputValidator.SUPPORTED_LANGUAGES:
            raise ValueError(f"Idioma no soportado: {lang}")
        return lang

    @staticmethod
    def validate_format(fmt: str) -> str:
        fmt = fmt.strip().lower()
        if fmt not in {"txt", "pdf"}:
            raise ValueError("El formato es inválido. Usa txt o pdf")
        return fmt

    @staticmethod
    def validate_filename(name: str) -> str:
        name = name.strip()
        if not name:
            raise ValueError("El nombre del archivo no puede estar vacío.")
        return name
