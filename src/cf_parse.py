import ply.yacc as yacc
import cf_lex

tokens = cf_lex.tokens

# ***** Policy *****

def p_policy(p):
    '''policy :
              | blocks'''


def p_blocks(p):
    '''blocks : block
              | block blocks'''


def p_block(p):
    '''block : bundle
             | body
             | promise'''


# ***** Bundle *****

def p_bundle(p):
    '''bundle : BUNDLE bundletype bundleid arglist bundlebody'''


def p_bundletype(p):
    '''bundletype : SYMBOL'''


def p_bundleid(p):
    '''bundleid : SYMBOL'''


def p_bundlebody(p):
    '''bundlebody : bodybegin bundlestatements bodyend'''


def p_bundlestatements(p):
    '''bundlestatements : bundlestatement
                        | bundlestatement bundlestatements'''


def p_bundlestatement(p):
    '''bundlestatement : promiseguard promiselines'''


def p_promiseguard(p):
    '''promiseguard : PROMISE_GUARD'''


def p_promiselines(p):
    '''promiselines :
                    | promiseline
                    | promiseline promiselines'''


# ***** Body *****

def p_body(p):
    '''body : BODY bodytype bodyid arglist bodybody'''


# ***** Promise ****

def p_promise(p):
    '''promise : PROMISE promisetype promiseid arglist bodybody'''


# ***** Argument list *****

def p_arglist(p):
    '''arglist : arglistbegin arglistitems arglistend'''

def p_arglist_begin(p):
    '''arglistbegin : LEFT_PAR'''

def p_arglist_items(p):
    '''arglistitems : arglistitem
                     | arglistitem COMMA
                     | arglistitem COMMA arglistitems'''

def p_arglist_item(p):
    '''arglistitem : IDENTIFIER'''

def p_arglist_end(p):
    '''arglistend : RIGHT_PAR'''


# ***** Common *****
def p_body_begin(p):
    '''bodybegin : LEFT_BRACE'''

def p_body_end(p):
    '''bodyend : RIGHT_BRACE'''


bparser = yacc.yacc()


def parse(data, debug=0):
    bparser.error = 0
    p = bparser.parse(data, debug=debug)
    if bparser.error:
        return None
    return p
