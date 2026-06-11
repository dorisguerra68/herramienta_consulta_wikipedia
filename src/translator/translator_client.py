from deep_translator import GoogleTranslator
import time

class TranslatorClient:

    def __init__(self):
        pass

    def translate_text(self, text: str, source_language: str, target_language: str):
        MAX_CHARS = 5000
        RETRIES = 5
        WAIT_SECONDS = 2

        def translate_chunk(chunk):
            for attempt in range(RETRIES):
                try:
                    return GoogleTranslator(
                        source=source_language,
                        target=target_language
                    ).translate(chunk)

                except Exception as e:
                    error_msg = str(e)

                    # Errores típicos de saturación
                    if "503" in error_msg or "403" in error_msg:
                        print(f"⚠️ Servidor saturado (intento {attempt+1}/{RETRIES}). Reintentando...")
                        time.sleep(WAIT_SECONDS)
                        continue

                    # Otros errores inesperados
                    print(f"❌ Error inesperado al traducir: {e}")
                    return chunk  # devolvemos el texto original para no romper el flujo

            print("❌ No se pudo traducir después de varios intentos.")
            return chunk

        # Si el texto es corto
        if len(text) <= MAX_CHARS:
            return translate_chunk(text)

        # Si es largo → dividir en partes
        translated_parts = []
        start = 0

        while start < len(text):
            end = start + MAX_CHARS
            chunk = text[start:end]
            translated_parts.append(translate_chunk(chunk))
            start = end

        return "\n".join(translated_parts)
