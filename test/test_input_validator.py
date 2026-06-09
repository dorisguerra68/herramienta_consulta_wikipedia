import pytest
from src.validator.input_validator import InputValidator


# -----------------------------
# validate_topic
# -----------------------------
def test_validate_topic_ok():
    assert InputValidator.validate_topic(" Python ") == "Python"


def test_validate_topic_empty():
    with pytest.raises(ValueError):
        InputValidator.validate_topic("   ")


# -----------------------------
# validate_language
# -----------------------------
def test_validate_language_ok():
    assert InputValidator.validate_language(" ES ") == "es"


def test_validate_language_invalid():
    with pytest.raises(ValueError):
        InputValidator.validate_language("jp")


# -----------------------------
# validate_format
# -----------------------------
def test_validate_format_ok_txt():
    assert InputValidator.validate_format(" TXT ") == "txt"


def test_validate_format_ok_pdf():
    assert InputValidator.validate_format(" pdf ") == "pdf"


def test_validate_format_invalid():
    with pytest.raises(ValueError):
        InputValidator.validate_format("docx")


# -----------------------------
# validate_filename
# -----------------------------
def test_validate_filename_ok():
    assert InputValidator.validate_filename(" archivo ") == "archivo"


def test_validate_filename_empty():
    with pytest.raises(ValueError):
        InputValidator.validate_filename("   ")
