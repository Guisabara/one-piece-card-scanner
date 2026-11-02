from src.models.card import Card
import pytest

# Desabilitando a função para teste individual de cada atributos:
#def test_cartas(carta_teste):
#    assert carta_teste.name == "Little Sadi" 
#    assert carta_teste.card_code == "OP11-063"
#    assert carta_teste.collection == "A Fist of Divine Speed - OP11"
#    assert carta_teste.card_type == "Character"
#    assert carta_teste.rarity == "Normal"
#    assert carta_teste.language == "Inglês"
#    assert carta_teste.artist == "Studio Vigor Co., Ltd"
#    assert carta_teste.art_version == "Normal Art"
#
    

@pytest.fixture
def carta_teste():
    carta01 = Card("Little Sadi", "OP11-063", "A Fist of Divine Speed - OP11", "Character", "Normal", "Inglês", "Studio Vigor Co., Ltd", "Normal Art")

    return carta01

def test_nome(carta_teste):
    assert carta_teste.name == "Little Sadi", "O nome desta carta é: Little Sadi."

def test_codigo(carta_teste):
    assert carta_teste.card_code == "OP11-063", "Esta carta pertence ao código: OP11-063."

def test_collection(carta_teste):
    assert carta_teste.collection == "A Fist of Divine Speed - OP11", "Esta carta pertence a coleção: A Fist of Divine Speed - OP11"

def test_card_type(carta_teste):
    assert carta_teste.card_type == "Character", "Está carta é do tipo: Character."

def test_rarity(carta_teste):
    assert carta_teste.rarity == "Normal", "Está carta pertence à raridade: Normal" 

def test_language(carta_teste):
    assert carta_teste.language == "Inglês", "A linguagem desta carta é: Inglês (US)."

def test_artist(carta_teste):
    assert carta_teste.artist == "Studio Vigor Co., Ltd", "O artista dseta carta é: Studio Vigor Co., Ltd"

def test_art_version(carta_teste):
    assert carta_teste.art_version == "Normal Art", "Está carta é versão base, Normal Art."






