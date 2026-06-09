
import pytest
from unittest.mock import patch, Mock

from src.wikipedia_client.wikipedia_client import WikipediaClient

# HTML falso para simular Wikipedia
FAKE_HTML = """
<html>
    <body>
        <h1>Python</h1>
        <p>Primer párrafo.</p>
        <p>Segundo párrafo.</p>
        <p>Tercer párrafo.</p>
        <p>Cuarto párrafo.</p>
        <p>Quinto párrafo.</p>
        <p>Sexto párrafo (no debería aparecer).</p>
    </body>
</html>
"""


@patch("requests.get")
def test_get_article_success(mock_get):
    # simular respuesta HTTP 200
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = FAKE_HTML
    mock_get.return_value = mock_response

    client = WikipediaClient()
    result = client.get_article("Python")

    assert result["title"] == "Python"
    assert len(result["paragraphs"]) == 5
    assert result["paragraphs"][0] == "Primer párrafo."


@patch("requests.get")
def test_get_article_http_error(mock_get):
    # simular error HTTP
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    client = WikipediaClient()

    with pytest.raises(Exception):
        client.get_article("Python")


def test_normalized_topic():
    client = WikipediaClient()
    assert client.normalized_topic("hola mundo") == "hola_mundo"
