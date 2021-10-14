# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band, Guitarist, Bassist, Drummer



def test_version():
    assert __version__ == '0.1.0'


def test_band_name():
    nirvana = Band("Nirvana", [])

    assert nirvana.name == "Nirvana"


def test_band_str():
    nirvana = Band("Nirvana", [])
    actual = str(nirvana)
    expected = "The band Nirvana"
    assert actual == expected


def test_band_repr():
    doo = Band("doo", [2])
    actual = repr(doo)
    expected = "Band instance. name=doo, members=[2]"
    assert actual == expected


def test_guitarist_str():
    joan = Guitarist("Joan Jett")
    actual = str(joan)
    expected = "My name is Joan Jett and I play guitar"
    assert actual == expected


def test_guitarist_repr():
    joan = Guitarist("Joan Jett")
    actual = repr(joan)
    expected = "Guitarist instance. Name = Joan Jett"
    assert actual == expected


def test_drummer_str():
    sheila = Drummer("Sheila E.")
    actual = str(sheila)
    expected = "My name is Sheila E. and I play drums"
    assert actual == expected


def test_drummer_repr():
    sheila = Drummer("Sheila E.")
    actual = repr(sheila)
    expected = "Drummer instance. Name = Sheila E."
    assert actual == expected


def test_bassist_str():
    meshell = Bassist("Meshell Ndegeocello")
    actual = str(meshell)
    expected = "My name is Meshell Ndegeocello and I play bass"
    assert actual == expected


def test_bassist_repr():
    meshell = Bassist("Meshell Ndegeocello")
    actual = repr(meshell)
    expected = "Bassist instance. Name = Meshell Ndegeocello"
    assert actual == expected


def test_guitarist():
    jimi = Guitarist("Jimi Hendrix")
    assert jimi.name == "Jimi Hendrix"
    assert jimi.get_instrument() == "guitar"


def test_bassist():
    flea = Bassist("Flea")
    assert flea.name == "Flea"
    assert flea.get_instrument() == "bass"


def test_drummer():
    ginger = Drummer("Ginger Baker")
    assert ginger.name == "Ginger Baker"
    assert ginger.get_instrument() == "drums"
