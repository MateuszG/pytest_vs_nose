import sys


def test_myoutput(capsys):
    print ("hello")
    sys.stderr.write("world\n")
    out, err = capsys.readouterr()

    assert out == "hello\n"
    assert err == "world\n"

    print "next"
    out, err = capsys.readouterr()
  
    assert out == "next\n"

