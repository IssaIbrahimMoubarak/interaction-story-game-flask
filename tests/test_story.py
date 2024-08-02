import unittest
from unittest.mock import patch
from src.story import navigate_node

class TestStory(unittest.TestCase):
    @patch('builtins.input', side_effect=["1", "1"])
    def test_navigate_node(self, mock_input):
        nodes = {
            "start": {
                "text": "start text",
                "choices": {"1": "next"}
            },
            "next": {
                "text": "next text",
                "choices": {"1": "end"}
            },
            "end": {
                "text": "end text",
                "choices": {}
            }
        }
        navigate_node("start", nodes)

if __name__ == '__main__':
    unittest.main()
