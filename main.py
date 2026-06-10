from dotenv import load_dotenv
import os

from src.ai_client.ai_client import AIClient
from src.wikipedia_client.wikipedia_client import WikipediaClient
from src.content_enricher.content_enricher import ContentEnricher
from src.translator.translator_client import TranslatorClient
from src.file_manager.file_manager import FileManager
from src.validator.input_validator import InputValidator

# --- Cargar API KEY ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or ""

def main():
    print("\n== Herramienta de Consulta Wikipedia ===\n")

    # Inicio, entrada del usuario
    topic = InputValidator.validate_topic(input("Introduce el tema a consultar: "))
    language = InputValidator.validate_language(input("En qué idioma (es/en/fr/de/it/pt): "))

    # Instancias
    ai_client = AIClient(api_key)
    wiki = WikipediaClient()
    enricher = ContentEnricher(ai_client)
    translator = TranslatorClient()
    file_manager = FileManager()

    # Obtener los datos de Wikipedia
    article = wiki.get_article(topic)
    raw_text = "\n".join(article["paragraphs"])
    print("\n--- Contenido original ---\n")
    print(raw_text)

    # Preguntar si quiere enriquecer
    enrich_choice = input("\n¿Quieres enriquecer el contenido? (s/n): ").strip().lower()
    if enrich_choice == "s":
        enriched_text = enricher.enrich(raw_text)
        print("\n--- Contenido enriquecido ---\n")
        print(enriched_text)
    else:
        enriched_text = raw_text

    # Preguntar si quiere traducir
    translate_choice = input("\n¿Quieres traducir el contenido? (s/n): ").strip().lower()
    if translate_choice == "s":
        final_language = InputValidator.validate_language(
            input("¿A qué idioma quieres traducir? (es/en/fr/de/it/pt): ")
        )
        final_text = translator.translate_text(enriched_text, language, final_language)
        print("\n--- Contenido traducido ---\n")
        print(final_text)
    else:
        final_text = enriched_text

    # Preguntar si quiere guardar
    save_choice = input("\n¿Quieres guardar el archivo? (s/n): ").strip().lower()
    if save_choice == "s":
        fmt = InputValidator.validate_format(input("Formato (txt/pdf): "))
        filename = InputValidator.validate_filename(input("Nombre del archivo: "))

        if fmt == "txt":
            file_manager.save_txt(filename, final_text)
        else:
            file_manager.save_pdf(filename, final_text)

        print("\n✔ Contenido guardado.\n")
    else:
        print("\nNo se guardó ningún contenido.\n")


if __name__ == "__main__":
    main()
