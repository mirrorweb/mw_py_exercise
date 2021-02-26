
def test_file():
    file = open('data/import_data.json', encoding="utf8")
    assert file.name == 'data/import_data.json'
