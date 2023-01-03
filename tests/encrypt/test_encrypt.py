import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("ALECTOR", -1) == "ROTCELA"
    assert encrypt_message("ALECTOR", 3) == "ELA_ROTC"
    assert encrypt_message("ALECTOR", 4) == "ROT_CELA"
    with pytest.raises(TypeError):
        encrypt_message("AABBCC", "123")
    with pytest.raises(TypeError):
        encrypt_message(121, 2)


if __name__ == "__main__":
    print(encrypt_message("ALECTOR", 4))
