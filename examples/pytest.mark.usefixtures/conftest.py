import pytest; import tempfile; import os

@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp() # '/tmp/tmpKUnnz2'
    os.chdir(newpath)
