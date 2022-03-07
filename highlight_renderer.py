from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import html
import mistune


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, lang=None):
        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = html.HtmlFormatter(style="default")
            return highlight(code, lexer, formatter)
        else:
            lexer = guess_lexer(code)
            formatter = html.HtmlFormatter(style="bw")
            return highlight(code, lexer, formatter)

    def codespan(self, code):
        return (
            "<span><code class='inline-code'>" + mistune.escape(code) + "</code></span>"
        )

markdown = mistune.create_markdown(renderer=HighlightRenderer())
