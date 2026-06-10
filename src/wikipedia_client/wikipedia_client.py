import requests
from bs4 import BeautifulSoup


class WikipediaClient:
    BASE_URL = "https://es.wikipedia.org/wiki/"

    def __init__(self):
        pass

    def get_article(self, topic: str) -> dict:
        normalized = self.normalized_topic(topic)
        url = self._build_url(normalized)

        html = self.download_html(url)
        soup = BeautifulSoup(html, "html.parser")

        title = self.extract_title(soup)
        paragraphs = self.extract_paragraphs(soup)

        return {
            "title": title,
            "paragraphs": paragraphs
        }

    def normalized_topic(self, topic: str) -> str:
        return topic.strip().replace(" ", "_")

    def _build_url(self, normalized: str) -> str:
        return f"{self.BASE_URL}{normalized}"

    def download_html(self, url: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error al acceder a Wikipedia: {response.status_code}")

        return response.text

    def extract_title(self, soup: BeautifulSoup) -> str:
        h1 = soup.find(id="firstHeading") or soup.find("h1")
        if not h1:
            raise Exception("No se encontró el título del artículo.")
        return h1.text.strip()

    def extract_paragraphs(self, soup: BeautifulSoup) -> list:
        paragraphs = []

        content_div = soup.find(class_="mw-parser-output")
        p_tags = content_div.find_all("p", recursive=False) if content_div else soup.find_all("p")

        for p in p_tags:
            text = p.get_text(strip=True)

            if text:
                paragraphs.append(text)

            if len(paragraphs) == 5:
                break

        if not paragraphs:
            raise Exception("No se encontraron párrafos válidos en el artículo.")

        return paragraphs