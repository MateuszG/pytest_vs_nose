import pytest; import tempfile; import os


@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp() # '/tmp/tmpKUnnz2'
    os.chdir(newpath)


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")
        assert os.listdir(os.getcwd()) == ['myfile']

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
