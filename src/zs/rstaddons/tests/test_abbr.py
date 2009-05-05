import unittest
import sys

from docutils.writers.html4css1 import HTMLTranslator
from docutils.writers.html4css1 import Writer as HTMLWriter
from docutils.core import publish_parts

from zs.rstaddons import abbr

class Translator(HTMLTranslator, abbr.AbbrHTMLTranslatorMixin):
    pass

class Writer(HTMLWriter):
    def __init__(self, *args, **kwargs):
        HTMLWriter.__init__(self, *args, **kwargs)
        self.translator_class = Translator

def render(text):
    return publish_parts(source=text, writer=Writer(), settings_overrides={
        'initial_header_level': 2,
        'input_encoding': 'utf-8',
        'output_encoding': 'utf-8',
    })['body']

class BasicTests(unittest.TestCase):
    def test_html(self):
        input = ':abbr:`TOC <table of contents>`'
        self.assertEquals('<p><abbr title="table of contents">TOC</abbr></p>\n', render(input))

    def test_quotes(self):
        input = ':abbr:`TOC <"table of contents">`'
        output = '<p><abbr title="&quot;table of contents&quot;">TOC</abbr></p>\n'
        self.assertEquals(output, render(input))
