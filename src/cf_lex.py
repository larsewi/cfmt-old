import ply.lex as lex

keywords = (
    "BUNDLE",
    "BODY",
    "PROMISE",
)

tokens = keywords + (
    "COMMA",
    "SEMICOLON",
    "LEFT_BRACE",
    "RIGHT_BRACE",
    "LEFT_PAR",
    "RIGHT_PAR",
    "COMMENT",
    "MACRO",
    "IDENTIFIER",
    "SYMBOL",
    "HASH_ROCKET",
    "PROMISE_ARROW",
    "QUOTED_STRING",
    "CLASS_GUARD",
    "VAR_CLASS",
    "PROMISE_GUARD",
    "NAKED_VAR",
)

# Keywords
t_BUNDLE = r"bundle"
t_BODY = r"body"
t_PROMISE = r"promise"

# Tokens
t_COMMA = r","
t_SEMICOLON = r";"
t_LEFT_BRACE = r"{"
t_RIGHT_BRACE = r"}"
t_LEFT_PAR = r"[(]"
t_RIGHT_PAR = r"[)]"
t_COMMENT = r"[#][^\n]*"
t_MACRO = r"@.*"
t_IDENTIFIER = r"[a-zA-Z0-9_\200-\377]+"
t_SYMBOL = r"[a-zA-Z0-9_\200-\377]+[:][a-zA-Z0-9_\200-\377]+"
t_HASH_ROCKET = r"=>"
t_PROMISE_ARROW = r"->"
t_QUOTED_STRING = r"\"((\\(.|\n))|[^\"\\])*\"|\'((\\(.|\n))|[^\'\\])*\'|`[^`]*`"
t_CLASS_GUARD = r"[.|&!()a-zA-Z0-9_\200-\377:][\t .|&!()a-zA-Z0-9_\200-\377:]*::"
t_VAR_CLASS = r"(\"[^\"\0]*\"|\'[^\'\0]*\')::"
t_PROMISE_GUARD = r"[a-zA-Z_]+:"
t_NAKED_VAR = r"[$@][(][a-zA-Z0-9_\[\]\200-\377.:]+[)]|[$@][{][a-zA-Z0-9_\[\]\200-\377.:]+[}]|[$@][(][a-zA-Z0-9_\200-\377.:]+[\[][a-zA-Z0-9_$(){}\200-\377.:]+[\]]+[)]|[$@][{][a-zA-Z0-9_\200-\377.:]+[\[][a-zA-Z0-9_$(){}\200-\377.:]+[\]]+[}]"


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()