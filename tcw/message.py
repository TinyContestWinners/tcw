import jinja2
from email.message import EmailMessage

class TCWMessage:
    """
    Create email message for a finished contest
    """

    def __init__(self, *args, **kwargs):
        self.contest = None
        self.mail_from = 'notifications@tinycontestwinners.com'
        self.message = None
        self.html = False
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

        if self.contest is None:
            raise Exception('Contest object required')


    def get_message(self):
        self.message = EmailMessage()
        self.message['From'] = self.mail_from
        self.message['To'] = self.contest.email
        if self.contest.final:
            self.message['Subject'] = 'Your tinycontestwinners contest results'
        else:
            self.message['Subject'] = 'Your tinycontestwinners contest has started'

        self._add_text_msg()
        if self.html is True:
            self._add_html_msg()

        return self.message


    def _add_text_msg(self):
        """
        Add plain text info to the email message
        """

        template = '''
{%- if contest.final %}
{%- set winners = contest.final.split("|") %}
Your contest has finished!
{%- else %}
Your contest has been created!
{%- endif %}

CONTEST TITLE:
  - {{ contest.title }}

{% if winners -%}
WINNERS:
 {%- for name in winners %}
  {{ loop.index }}. {{ name }}
 {%- endfor %}
{%- endif %}

STATISTICS:
  - max entrants: {{ contest.max_entrants }}
  - winners: {{ contest.winners }}
  - total sign ups: {{ contest.entrants | length }}
  - expires: {{ contest.expires }} UTC
  {%- if not winners %}
  - signup: https://tinycontestwinners.com/signup?name={{ contest.name }}
  {% endif -%}

THANK YOU!
{%- if winners %}
You are responsible for contacting the winners.
{% endif -%}
        '''

        msg = jinja2.Template(template).render(contest=self.contest)
        self.message.set_content(msg.strip())


    def _add_html_msg(self):
        """
        Add HTML formatted text into the email message
        """

        template = '''
<html>
  <head>
    <title>tinycontestwinners contest results!</title>
  </head>
  <body>

  </body>
</html>
        '''

        msg = jinja2.Template(template).render(contest=self.contest)
        self.message.add_alternative(msg.strip())
