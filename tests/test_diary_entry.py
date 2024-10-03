from lib.diary_entry import DiaryEntry
import pytest


d = DiaryEntry("My diary", "Today I went to the park and read a book")

def test_normal_formatting():
    assert d.format() == "My diary: Today I went to the park and read a book"

def test_count_words():
    assert d.count_words() == 10

def test_reading_time_normal_wpm():
    assert d.reading_time(10) == 1

def test_reading_time_abnormal_wpm():
    with pytest.raises(Exception) as e:
        result = d.reading_time(-1)
    assert str(e.value) == "Cannot have reading speed <= 0"

def test_reading_chunk():
   assert d.reading_chunk(1, 5) == "Today I went to the" 

