import pytest
from project import course_select, week_select

def main():
    test_course_select()
    test_week_select()

def test_course_select(monkeypatch):

    test_cases=[
        ("CS50x","CS50x"),
        ("cs50 python ","CS50 Python"),
        ("",""),
        ("cat",None),
        ("dog",None)
    ]
    for input_value, expected_output in test_cases:
        monkeypatch.setattr("builtins.input",lambda _:input_value)
        if expected_output is None:
            with pytest.raises(TypeError):
                course_select()
        else:
            output=course_select()
            assert output==expected_output

def test_week_select(monkeypatch):

    test_cases=[
        ("12",12.0),
        ("0",0.0),
        ("cat",None),
    ]
    for input_value, expected_output in test_cases:
        monkeypatch.setattr("builtins.input",lambda _:input_value)
        if expected_output is None:
            with pytest.raises(ValueError):
                week_select()
        else:
            output=week_select()
            assert output==expected_output

