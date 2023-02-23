import pytest

from display import Display


class TestItem:
    @pytest.mark.parametrize('msg', [
        'Hello world',
        '',
        None,
        ])
    def test_display_msg(self, msg):
        display = Display()
        display.msg = msg
        result = display.msg
        assert result == msg
