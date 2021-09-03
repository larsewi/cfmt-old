import sys
import ply.lex as lex
from logger import Logger

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
    "COMMENT",
    "MACRO",
)


def t_BUNDLE(t):
    r"bundle\s"
    t.lexpos -= 1
    t.value = t.value[:-1]
    log_token(t)
    return t


def t_BODY(t):
    r"body\s"
    t.lexpos -= 1
    t.value = t.value[:-1]
    log_token(t)
    return t


def t_PROMISE(t):
    r"promise"
    t.lexpos -= 1
    t.value = t.value[:-1]
    log_token(t)
    return t


def t_QUOTED_STRING(t):
    r"\"((\\(.|\n))|[^\"\\])*\"|\'((\\(.|\n))|[^\'\\])*\'|`[^`]*`"
    log_token(t)
    return t


def t_CLASS_GUARD(t):
    r"[.|&!()a-zA-Z0-9_\200-\377:][\t .|&!()a-zA-Z0-9_\200-\377:]*::"
    log_token(t)
    return t


def t_PROMISE_GUARD(t):
    r"[a-zA-Z_]+:"
    log_token(t)
    return t


def t_HASH_ROCKET(t):
    r"=>"
    log_token(t)
    return t


def t_PROMISE_ARROW(t):
    r"->"
    log_token(t)
    return t


def t_NAKED_VAR(t):
    r"[$@][(][a-zA-Z0-9_\[\]\200-\377.:]+[)]|[$@][{][a-zA-Z0-9_\[\]\200-\377.:]+[}]|[$@][(][a-zA-Z0-9_\200-\377.:]+[\[][a-zA-Z0-9_$(){}\200-\377.:]+[\]]+[)]|[$@][{][a-zA-Z0-9_\200-\377.:]+[\[][a-zA-Z0-9_$(){}\200-\377.:]+[\]]+[}]"
    log_token(t)
    return t


def t_COMMA(t):
    r","
    log_token(t)
    return t


def t_SEMICOLON(t):
    r";"
    log_token(t)
    return t


def t_LEFT_BRACE(t):
    r"{"
    log_token(t)
    return t


def t_RIGHT_BRACE(t):
    r"}"
    log_token(t)
    return t


def t_LEFT_PAR(t):
    r"[(]"
    log_token(t)
    return t


def t_RIGHT_PAR(t):
    r"[)]"
    log_token(t)
    return t


def t_COMMENT(t):
    r"[#][^\n]*"
    #r"([#][^\n]*)(\n[ \t]*[#][^\n]*)*"
    #t.value = re.sub(r"\n[ \t]*[#]", "\n#", t.value)
    log_token(t)
    return t


def t_MACRO(t):
    r"@.*"
    log_token(t)
    return t


# Some tokens above are subsets of IDENTIFIER
def t_IDENTIFIER(t):
    r"[a-zA-Z0-9_\200-\377]+(\:[a-zA-Z0-9_\200-\377]+)?"
    log_token(t)
    return t


# Ignore whitespace
t_ignore = " \t"


# Count line numbers, but discard newline tokens
def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    logger = Logger()
    logger.log_error("Lexer error: Illegal character '%s' on line '%s'" % (t.value[0], t.lineno))
    sys.exit(1)
#    t.lexer.skip(1)


def log_token(t):
    logger = Logger()
    logger.log_debug("Token:")
    logger.log_debug("\tType: %s" % t.type)
    logger.log_debug("\tValue: '%s'" % t.value)
    logger.log_debug("\tLine no: %s" % t.lineno)


lexer = lex.lex()

if __name__ == "__main__":
    lex.runmain(lexer)
