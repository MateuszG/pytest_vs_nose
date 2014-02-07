import pytest

@pytest.yield_fixture
def passwd():
    with open("/etc/passwd") as f:
        yield f.readlines()

def test_has_lines(passwd):
    assert len(passwd) >= 1
