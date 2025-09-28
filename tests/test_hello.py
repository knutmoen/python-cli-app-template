import pytest
from mycli.operations import hello


def test_hello_with_name(capsys):
    hello.run(["Knut"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Knut!"


def test_hello_without_name(capsys):
    hello.run([])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
