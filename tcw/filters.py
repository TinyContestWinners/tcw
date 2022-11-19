import markdown


def md_to_html(txt):
    """
    Convert text to markdown
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
