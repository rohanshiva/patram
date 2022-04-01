from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
import mistune


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, lang=None):
        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = html.HtmlFormatter()
            return highlight(code, lexer, formatter)
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"


markdown = mistune.create_markdown(renderer=HighlightRenderer())
