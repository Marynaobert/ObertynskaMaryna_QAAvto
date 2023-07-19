import pytest

@pytest.mark.check
def test_check_name (user):
    assert user.name == 'Maryna'
    

@pytest.mark.check
def test_check_second_name (user):
    assert user.second_name == 'Obertynska'
    