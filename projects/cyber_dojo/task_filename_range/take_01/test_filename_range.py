import pytest

from filename_range import FilenameRange
from conftest import FILENAME_RANGE_TESTS


class TestFilenameRange:
    @pytest.mark.parametrize('filename, expected', [
        (filename, expected) for filename, expected in FILENAME_RANGE_TESTS.items()
        ])
    def test_filename_range(self, filename, expected):
        result = FilenameRange.filename_range(filename)
        assert result == expected
