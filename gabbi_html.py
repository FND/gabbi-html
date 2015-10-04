import re

import gabbi.case

from lxml import html
from gabbi.handlers import ResponseHandler


def gabbi_response_handlers():
    return [HTMLResponseHandler]


def replace_response_html(self, message):
    """
    replaces a CSS selector with the corresponding value from the previous request
    """

    def _css_replacer(match):
        selector = match.group("arg")

        doc = html.fromstring(self.prior.output)
        nodes = doc.cssselect(selector)
        assert len(nodes) == 1 # TODO: proper error message

        return nodes[0].text # XXX: too simplistic

    regex = re.compile(self._replacer_regex("RESPONSE_HTML")) # TODO: precalculate once
    return regex.sub(_css_replacer, message)


# monkey-patch gabbi to include custom replacer
gabbi.case.REPLACERS += ["RESPONSE_HTML"]
gabbi.case.HTTPTestCase._response_html_replace = replace_response_html


class HTMLResponseHandler(ResponseHandler):

    test_key_suffix = "html"
    test_key_value = {}

    def preprocess(self, test):
        self.doc = html.fromstring(test.output)

    def action(self, test, item, value):
        try: # count
            count = int(value)
        except ValueError: # content
            count = None

        nodes = self.doc.cssselect(item)
        if count:
            test.assertEqual(len(nodes), count)
        else:
            test.assertEqual(len(nodes), 1,
                    "content checks must not target more than a single element")
            test.assertEqual(nodes[0].text.strip(), value,
                    "unexpected element contents")
