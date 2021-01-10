from SRC.mock import User
from unittest.mock import patch, MagicMock

def test_return_available_funds():
    faccount1 = MagicMock()
    faccount1.get_balance.return_value = 50
    faccount2 = MagicMock()
    faccount2.get_balance.return_value = 40
    user = User("kowalski",35,[faccount1, faccount2])
    assert user.return_available_funds()==90
