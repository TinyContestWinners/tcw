import string
import secrets
import datetime
import markdown


def random_name(length=24):
    """
    create random name for contests. a mix of alphanum chars.

    args:
        - int name length
    returns:
        - str
    """

    letters = string.ascii_letters
    digits = string.digits
    alphabet = letters + digits
    name = ''

    while len(name) < length:
        name += secrets.choice(alphabet)

    return name


def expires_time(hours=1.0):
    """
    get a datetime object x number of hours in the future.

    args:
        - float hours into the future
    returns:
        - datateime object, None on  error
    """

    later = None
    try:
        now = datetime.datetime.utcnow().replace(second=0, microsecond=0)
        later = now + datetime.timedelta(hours=hours)
    except:
        pass

    return later


def md_to_html(txt):
    """
    Convert markdown text to HTML.

    args:
        - str (markdown text)
    returns:
        str (html text)
    """

    try:
        html = markdown.markdown(txt)
        return html
    except:
        return txt
