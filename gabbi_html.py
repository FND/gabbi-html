from lxml import html
from gabbi.handlers import ResponseHandler


def gabbi_response_handlers():
    return [HTMLResponseHandler]


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
