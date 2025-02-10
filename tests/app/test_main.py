from app.main import get_prompt
import pytest
from unittest.mock import mock_open, patch
from pathlib import Path

def test_get_prompt_none():
    assert get_prompt() is None
    assert get_prompt(None) is None

def test_get_prompt_file_exists():
    mock_file_content = "This is a test prompt.\n"
    fake_prompt_dir = Path("/fake/path")
    with patch('app.main.PROMPT_DIR_PATH', fake_prompt_dir):
        with patch("app.main.open", mock_open(read_data=mock_file_content)) as mocked_file:
            prompt = get_prompt("prompt.txt")
            mocked_file.assert_called_once_with(fake_prompt_dir / "prompt.txt")
            assert prompt == "This is a test prompt."
