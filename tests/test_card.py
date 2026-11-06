from src.models.card import Card
import pytest

@pytest.fixture
def carta_teste():
    carta01 = Card("Little Sadi", "OP11-063", "A Fist of Divine Speed - OP11", "Character", "Normal")

    return carta01

def test_nome(carta_teste):
    assert carta_teste.name == "Little Sadi", "O nome desta carta é: Little Sadi."

def test_codigo(carta_teste):
    assert carta_teste.card_code == "OP11-063", "Esta carta pertence ao código: OP11-063."

def test_collection(carta_teste):
    assert carta_teste.collection == "A Fist of Divine Speed - OP11", "Esta carta pertence a coleção: A Fist of Divine Speed - OP11"

def test_card_type(carta_teste):
    assert carta_teste.card_type == "Character", "Esta carta é do tipo: Character."

def test_rarity(carta_teste):
    assert carta_teste.rarity == "Normal", "Esta carta pertence à raridade: Normal" 







