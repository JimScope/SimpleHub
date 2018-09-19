#  simple_hub.py
#
#  Copyright 2018  Jimmy A. Pérez Díaz
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import glob
from gfm import gfmdef load_file(the_file):
    with open(the_file, 'r') as data:
        return data.read()


def render(text):
    return gfm.markdown(text)


def html_template(text, css='"simple_dark.css"'):
    html = """
    <!DOCTYPE HTML>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width,initial-scale=1">
            <title>SimpleHub(Alpha)</title>
            <link rel="stylesheet" type="text/css" media="all" href=""" + css + """/>
        </head>
        <body>""" + text + """</body>
    </html>"""
    return html


def export_html(file_html, filename):
    with open(filename, 'w') as document:
        document.write(file_html)


lista_md = glob.glob('*.md')
for i in lista_md:
    md_rendered = render(load_file(i))
    export_html(html_template(md_rendered), i.replace('.md', '.html'))

