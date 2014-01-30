# content of conftest.py
import smtplib


def smtp():
    return smtplib.SMTP("merlinux.eu")


# content of test_module.py
def test_ehlo():
    response = smtp()
    print smtp, smtp()
    response = response.ehlo()
    assert response[0] == 250
    assert "merlinux" in response[1]
    assert 0  # for demo purposes


def test_noop():
    response = smtp()
    print smtp, smtp()
    response = response.ehlo()
    assert response[0] == 250
    assert 0  # for demo purposes
