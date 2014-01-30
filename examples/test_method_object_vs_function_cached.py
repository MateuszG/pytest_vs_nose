# # content of conftest.py
# import pytest
# import smtplib
# import unittest


# class ala(object):

#     @pytest.fixture(scope="module")
#     def smtp(self):
#         return smtplib.SMTP("merlinux.eu")
        


# inst_ala = ala()
# inst_ala_smtp = inst_ala.smtp()


# class TestAla(unittest.TestCase):

#     # content of test_module.py

#     def test_ehlo(self):
#         # inst_ala = ala()
#         # inst_ala_smtp = inst_ala.smtp()
#         # import pdb; pdb.set_trace()
#         response = inst_ala_smtp.ehlo()
#         print inst_ala.smtp
#         assert response[0] == 250
#         assert "merlinux" in response[1]
#         assert 0  # for demo purposes

#     def test_noop(self):
#         # inst_ala = ala()
#         # inst_ala_smtp = inst_ala.smtp()
#         response = inst_ala_smtp.noop()
#         print inst_ala.smtp
#         assert response[0] == 250
#         assert 0  # for demo purposes

# 0.13


# content of conftest.py
import pytest
import smtplib
import unittest


class ala(object):
    def smtp(self):
        return smtplib.SMTP("merlinux.eu")

inst_ala = ala()
inst_ala_smtp = inst_ala.smtp()
import sys


class TestAla(unittest.TestCase):

    # content of test_module.py

    def test_ehlo(self):
        # inst_ala = ala()
        # inst_ala_smtp = inst_ala.smtp()
        response = inst_ala_smtp.ehlo()
        print inst_ala_smtp.ehlo
        assert response[0] == 250
        assert "merlinux" in response[1]
        assert 0  # for demo purposes

    def test_noop(self):
        # inst_ala = ala()
        # inst_ala_smtp = inst_ala.smtp()
        response = inst_ala_smtp.noop()
        print inst_ala_smtp.noop
        assert response[0] == 250
        assert 0  # for demo purposes


    def test_myoutput(self, capsys): # or use "capfd" for fd-level
        # import pdb; pdb.set_trace()
        print ("hello")
        sys.stderr.write("world\n")
        out, err = capsys.readouterr()
        assert out == "hello\n"
        assert err == "world\n"
        print "next"
        out, err = capsys.readouterr()
        assert out == "next\n"

# 0.22