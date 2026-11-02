from src.models.card import Card


def test_cartas():
    carta01 = Card("Little Sadi", "OP11-063", "A Fist of Divine Speed - OP11", "Character", "Normal", "Inglês", "Studio Vigor Co., Ltd", "Normal Art")
    assert carta01.name == "Little Sadi" 
    assert carta01.card_code == "OP11-063"
    assert carta01.collection == "A Fist of Divine Speed - OP11"
    assert carta01.card_type == "Character"
    assert carta01.rarity == "Normal"
    assert carta01.language == "Inglês"
    assert carta01.artist == "Studio Vigor Co., Ltd"
    assert carta01.art_version == "Normal Art"











