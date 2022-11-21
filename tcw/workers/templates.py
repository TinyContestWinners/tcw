TEXT_TEMPLATE = '''
Your contest has finished!

CONTEST TITLE:
--------------
- {{ contest.title }}

{% if winners -%}
WINNERS:
--------
{%- for name in winners %}
{{ loop.index }}. {{ name }}
{%- endfor %}
{% else %}
Sorry... there were no winners?
{%- endif %}

STATISTICS:
-----------
- max entrants: {{ contest.max_entrants }}
- winners: {{ contest.winners }}
- total sign ups: {{ contest.entrants | length }}
- expired: {{ contest.expires }} UTC

Remember, You are responsible for contacting the winners.
THANK YOU!
'''


HTML_TEMPLATE = '''
<html>
<head>
<title>tinycontestwinners contest results!</title>
</head>
<body>

</body>
</html>
'''
