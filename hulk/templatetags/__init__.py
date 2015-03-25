from django_jinja import library
import jinja2
import re

def as_table(content):
    template = jinja2.Template(
    '''
    <table>
    {% for k,v in content.items() %}
    <tr><td></td><td>{{v}}</td></tr>
    {% endfor %}
    </table>
    ''')
    return template.render(content=content)

def as_link(content):
    template = jinja2.Template('<a href="{{content}}">{{content}}</a>')
    return template.render(content=content)

def as_positives(content):
    template = jinja2.Template(
    '''
    <table>
    {% for k,v in content.items() %}
    <tr><td class="search_positive">...{{v[0]}}...</td></tr>
    {% endfor %}
    </table>
    ''')
    return template.render(content=content)


@library.filter
def prettyprint(content, label):
    """
    """
    if label == 'positives':
        return as_positives(content)
    elif isinstance(content, list):
        return ', '.join(str(x).capitalize() for x in content)
    elif isinstance(content, dict):
        return as_table(content)
    elif isinstance(content, str):
        if content.startswith('http'):
            return as_link(content)
        elif content.startswith('s3://'):
            match = re.match('s3://(.*?)/(.*)', content)
            if match:
                content = 'https://%s.s3.amazonaws.com/%s' % match.groups()
            return as_link(content)
        else:
            return content
    else:
        return content
