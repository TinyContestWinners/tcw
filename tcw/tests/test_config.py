from tcw.config import Development, Production


def test_devel_cfg():
    assert Development.DEBUG is True
    assert Development.TESTING is True


def test_production_cfg():
    assert Production.DEBUG is False
    assert Production.TESTING is False
