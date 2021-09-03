from logger import Logger


class PrettyPrinter:
    _MAX_COL = 80
    logger = Logger()

    def __init__(self, lexer):
        self._indent = ""
        self._strlst = [""]
        self._lexer = lexer
        self.pretty_print()

    def print(self, s):
        assert "\n" not in s

        if not self._strlst[-1]:
            self._strlst[-1] = self._indent
        if s:
            self._strlst[-1] += s

    def println(self, s=""):
        assert "\n" not in s

        if s:
            self._strlst[-1] += s
        self._strlst.append("")

    def print_no_indent(self, s=""):
        assert "\n" not in s

        if s:
            self._strlst[-1] += s

    def get_cursor(self):
        row = len(self._strlst)
        col = len(self._strlst[-1])
        return (row, col)

    def truncate_to(self, cursor):
        row, col = cursor
        self._strlst = self._strlst[:row]
        self._strlst[-1] = self._strlst[-1][:col]

    def align(self, spaces):
        self._strlst[-1] += " " * spaces

    def indent(self):
        assert len(self._indent) % 2 == 0
        self._indent += "  "

    def dedent(self):
        assert len(self._indent) >= 2
        assert len(self._indent) % 2 == 0
        self._indent = self._indent[:-2]

    def should_wrap(self, pluss=0):
        col = len(self._strlst[-1])
        return col + pluss > self._MAX_COL

    def __str__(self):
        return "\n".join(self._strlst)

    def pretty_print(self):
        for token in self._lexer:
            if token.type == "BUNDLE":
                self.print(token.value)
                self.p_bundle()

            elif token.type == "BODY":
                self.print(token.value)
                self.p_body()

            elif token.type == "PROMISE":
                self.print(token.value)
                self.p_promise()

            elif token.type == "COMMENT":
                self.println(token.value)

            elif token.type == "MACRO":
                self.println(token.value)

            else:
                self.logger.log_error("Error !!!!!")
                break


    def p_bundle(self):
        stash = []

        token = self._lexer.token()
        while token.type in ("COMMENT", "MACRO"):
            if token.type == "COMMENT":
                stash.append(token)
            else:
                self.println()
                self.print_no_indent(token.value)
                self.println()
            token = self._lexer.token()

    def p_body(self):
        pass

    def p_promise(self):
        pass
