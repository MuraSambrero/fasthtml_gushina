from fasthtml.core import P, Script, Html, Link, Div, Template, Style, to_xml
from fasthtml.components import show, Zero_md
from fasthtml.common import *

app, rt = fast_app()

with open('_readme.txt') as f:
    lesson_content = f.read()

def render_local_md(md, css = ''):
    css_template = Template(Style(css), data_append=True)
    return Zero_md(css_template, Script(md, type="text/markdown"))

zeromd_headers = [Script(type="module", src="https://cdn.jsdelivr.net/npm/zero-md@3?register")]

lesson_content_html = render_local_md(lesson_content)




@rt("/")
def get():
    return Html(*zeromd_headers, lesson_content_html)

serve()