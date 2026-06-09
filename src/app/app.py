from src.wikipedia_client.wikipedia_client import WikipediaClient

def get_user_input(message):
    return input(message)

def main():
    print("=== Herramienta de Consulta a Wikipedia ===")

    topic = get_user_input("Introduce un tema: ")

    client = WikipediaClient()
    result = client.get_article(topic)

    print("\n=== RESULTADO ===")
    print(f"Título: {result['title']}\n")

    print("Primeros 5 párrafos:\n")
    for i, p in enumerate(result["paragraphs"], start=1):
        print(f"{i}. {p}\n")

if __name__ == "__main__":
    main()
