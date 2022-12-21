import datetime
from tcw.utils import (contest_by_name, random_name,
    expires_time, md_to_html)


def test_md_convert():
    txt = "# test header"
    html = md_to_html(txt)
    assert html == "<h1>test header</h1>"

    txt = " - test item"
    html = md_to_html(txt)
    assert html == "<ul>\n<li>test item</li>\n</ul>"


def test_random_name():
    name1 = random_name(16)
    assert len(name1) == 16

    name2 = random_name(24)
    assert len(name2) == 24

    name3 = random_name(24)
    assert name2 != name3


def test_future_time():
    now = datetime.datetime.utcnow()
    then = expires_time(12)
    assert then == (now + datetime.timedelta(hours=12)).replace(
        second=0, microsecond=0)
