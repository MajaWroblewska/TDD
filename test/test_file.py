from SRC.file import get_data, get_avg
from unittest.mock import patch, MagicMock

def test_get_avd():
    fake_file= MagicMock()
    fake_file.return_value = '987654321'
    with patch('SRC.file.get_data', fake_file):
        assert get_avg(3)==5.0 # średnia z całego (987654321) a nie z 3 cyfr
        assert get_avg(8)==5.0 #!!!!!!!!!!!!!!!!!!!mok zastępuje całe ciało funcji


# def test_get_avd():
#     fake_file= MagicMock(return_value = '987654321')  # przy funkcjach
#     with patch('SRC.file.get_data', fake_file):
#         assert get_avg(3)==8.0
