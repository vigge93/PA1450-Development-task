from program.backend import file_reader, process_file, get_attributes, get_data, ext_check, insert_values_to_datapoints_table, insert_values_to_attribute_table, access_db, close_db, initialize_database
import os
import tempfile


def test_file_reader():
    """Test file reader."""
    # Given
    a = "data.csv"

    # When
    res1 = file_reader(a)
    res2 = file_reader(a)

    # Then
    assert type(res1) == list
    assert type(res2) != int


def test_file_upload():
    """Test file upload."""
    # Given
    a = "data.csv"
    b = tempfile.NamedTemporaryFile(prefix="test", suffix=".img")

    # When
    res1 = process_file(a)
    res2 = process_file(a)
    res3 = process_file(b.name)

    # Then
    assert type(res1) == str
    assert res2 == "File uploaded succesfully!"
    assert res3 == "File is not in the correct format"

    # Removes the file the file
    b.close()


def test_access_db():
    """Test access database."""
    # When
    res1 = access_db()

    # Then
    assert os.path.isfile('instance\weather_data.db')


def test_initialize_database():
    """Test initialize database."""
    # Given
    db = access_db()
    c = db.cursor()
    # When
    table = initialize_database()
    names = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for name in names:
        res1 = name[0]
    # Then
    assert res1 == 'Datapoints'


def test_get_attributes():
    """Test get attributes."""
    # When
    res1 = get_attributes()

    # Then
    assert type(res1) == list


def test_get_data():
    """Test get data."""
    # Given
    dic1 = {"timeArgument": ["01"],
            "timeIntervallType": "MONTH", "Argument": "nederbordsmangd"}
    dic2 = {"timeArgument": ["2020-01-01", "2020-01-02"],
            "timeIntervallType": "TIME_INTERVALL", "Argument": "nederbordsmangd"}
    # When
    res1 = get_data(dic1)
    res2 = get_data(dic2)

    # Then
    assert type(res1) == list
    assert type(res2) == list


def test_ext_check():
    """Test extension check."""
    # Given
    a = "data.csv"

    # When
    res1 = ext_check(a)

    # Then
    assert res1


def test_close_db():
    """Test close database."""
    # Given
    db = access_db()
    is_closed = False

    # When
    close_db(db)
    try:
        res1 = db.cursor()
    except:
        is_closed = True 
    # Then
    assert is_closed
