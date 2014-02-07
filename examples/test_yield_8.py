import pytest

@pytest.yield_fixture
def passwd():
    print ("\nsetup before yield")
    f = open("/etc/passwd")
    yield f.readlines()
    print ("teardown after yield")
    f.close()

def test_has_lines(passwd):
    print ("test called")
    assert passwd
