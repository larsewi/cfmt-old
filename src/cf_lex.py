import ply.lex as lex

tokens = (
    "IDENTIFIER",
    "QUOTED_STRING",
    "CLASS_GUARD",
    "PROMISE_GUARD",
    "BUNDLE",
    "BODY",
    "PROMISE",
    "HASH_ROCKET",
    "PROMISE_ARROW",
    "NAKED_VAR",
    "COMMA",
    "SEMICOLON",
    "LEFT_BRACE",
    "RIGHT_BRACE",
    "LEFT_PAR",
    "RIGHT_PAR",
    #    "COMMENT",
    #    "MACRO",
)


def t_QUOTED_STRING(t):
    r"\"((\\(.|\n))|[^\"\\])*\"|\'((\\(.|\n))|[^\'\\])*\'|`[^`]*`"
    print_debug(t)
    return t


def t_CLASS_GUARD(t):
    r"[.|&!()a-zA-Z0-9_\200-\377:][\t .|&!()a-zA-Z0-9_\200-\377:]*::"
    print_debug(t)
    return t


def t_PROMISE_GUARD(t):
    r"[a-zA-Z_]+:"
    print_debug(t)
    return t


def t_BUNDLE(t):
    r"bundle"
    print_debug(t)
    return t


def t_BODY(t):
    r"body"
    print_debug(t)
    return t


def t_PROMISE(t):
    r"promise"
    print_debug(t)
    return t


def t_HASH_ROCKET(t):
    r"=>"
    print_debug(t)
    return t


def t_PROMISE_ARROW(t):
    r"->"
    print_debug(t)
    return t


def t_NAKED_VAR(t):
    r"[$@][(][a-zA-Z0-9_\[\]\200-\377.:]+[)]|[$@][{][a-zA-Z0-9_\[\]\200-\377.:]+[}]|[$@][(][a-zA-Z0-9_\200-\377.:]+[\[][a-zA-Z0-9_$(){}\200-\377.:]+[\]]+[)]|[$@][{][a-zA-Z0-9_\200-\377.:]+[\[][a-zA-Z0-9_$(){}\200-\377.:]+[\]]+[}]"
    print_debug(t)
    return t


def t_COMMA(t):
    r","
    print_debug(t)
    return t


def t_SEMICOLON(t):
    r";"
    print_debug(t)
    return t


def t_LEFT_BRACE(t):
    r"{"
    print_debug(t)
    return t


def t_RIGHT_BRACE(t):
    r"}"
    print_debug(t)
    return t


def t_LEFT_PAR(t):
    r"[(]"
    print_debug(t)
    return t


def t_RIGHT_PAR(t):
    r"[)]"
    print_debug(t)
    return t


# def t_COMMENT(t):
#     r"[#][^\n]*"
#     print_debug(t)
#     return t


# def t_MACRO(t):
#     r"@.*"
#     print_debug(t)
#     return t


# Must be last, since many of the tokens above are subsets of identifier
def t_IDENTIFIER(t):
    r"[a-zA-Z0-9_\200-\377]+"
    print_debug(t)
    return t


# Ignore whitespace
t_ignore = " \t"


# Count line numbers, but discard newline tokens
def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Lexer: Illegal character '%s'" % t.value[0])
    print(t)
    t.lexer.skip(1)


def print_debug(t):
    print("Token:")
    print("\tType: %s" % t.type)
    print("\tValue: '%s'" % t.value)
    print("\tLine no: %s" % t.lineno)


lexer = lex.lex()

if __name__ == "__main__":
    lex.runmain(lexer)
