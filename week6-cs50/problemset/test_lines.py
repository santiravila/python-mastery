import pytest
from lines import validate_cla, count_lines

def test_too_few_args():
    assert validate_cla(["lines.py"]) == "Too few command-line arguments"

def test_too_many_args():
    assert validate_cla(["lines.py", "code.py", "hello.py"]) == "Too many command-line arguments"

def test_wrong_extension():
    assert validate_cla(["lines.py", "image.png"]) == "Not a Python File"
    
def test_valid_input():
    assert validate_cla(["lines.py", "hello.py"]) is None

def test_file_found():
    with pytest.raises(FileNotFoundError):
        count_lines("non_existent_file.py") # found out pytest's 'tmp_path' is a more robust way to validate this 

def test_count():
    assert count_lines("hello.py") == 2
