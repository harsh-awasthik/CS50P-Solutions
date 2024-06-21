from seasons import time_to_dob
import pytest

def test_seasons():
    with pytest.raises(SystemExit):
        time_to_dob("cat")

