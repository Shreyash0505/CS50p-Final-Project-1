# test_voice_assistant.py
import pytest
from unittest.mock import Mock
from voice_assistant import speak, get_github, get_chrome, today_date, joke



# Example test case for the speak function
def test_speak(capsys):
    speak('Hello')
    captured = capsys.readouterr()
    assert captured.out == ''


# Example test case for the get_github function
def test_get_github(monkeypatch):
    # Define the mock function for webbrowser.get
    def mock_get(url):
        # Check that the function is called with the correct URL
        assert url == 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        return Mock()

    # Replace webbrowser.get with the mock function
    monkeypatch.setattr("webbrowser.get", mock_get)

    # Call the function being tested
    get_github()


# Example test case for the get_chrome function
def test_get_chrome(monkeypatch):
    def mock_os_startfile(path):
        assert path == "C:/Program Files/Google/Chrome/Application/chrome.exe"
        return

    monkeypatch.setattr("os.startfile", mock_os_startfile)
    get_chrome()


# Example test case for the today_date function
def test_today_date(capsys):
    today_date()
    captured = capsys.readouterr()
    assert captured.out == "" 

# Example test case for the joke function
def test_joke(capsys):
    joke()
    captured = capsys.readouterr()
    assert "" in captured.out


