"""
This adds the :abbr: role to ReST to allow abbreviations.
"""

import re

from docutils import nodes
from docutils.parsers.rst import roles
from docutils.writers.html4css1 import HTMLTranslator


RE_ABBR = re.compile(r'^(.*)\s*<(.*)>$')

def abbr_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    nodes = []
    msgs = []
    mo = RE_ABBR.search(text)
    if mo is None:
        msgs.append(inliner.reporter.error('The abbr-role has the format :abbr:`text <title>`'))
    else:
        title = mo.group(2).rstrip().lstrip()
        text = mo.group(1).rstrip().lstrip()
        nodes = [abbr(rawtext, text, title, **options)]
    return nodes, msgs


class abbr(nodes.TextElement):
    def __init__(self, rawtext, text, title, **options):
        nodes.TextElement.__init__(self, rawtext, text, **options)
        self['title'] = title

class AbbrHTMLTranslatorMixin(object):
    """
    This mixin provides all the methods required by the nodevisitor for 
    providing the :abbr: role.
    """
    def visit_abbr(self, node):
        self.body.append(self.starttag(node, 'abbr', '', title=node['title']))

    def depart_abbr(self, node):
        self.body.append('</abbr>')

roles.register_canonical_role('abbr', abbr_role)
