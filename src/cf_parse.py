import ply.yacc as yacc
import cf_lex

tokens = cf_lex.tokens

##### Policy #####

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


##### Bundle #####

def p_bundle(p):
    '''bundle : BUNDLE bundletype bundleid arglist bundlebody'''


def p_bundletype(p):
    '''bundletype : SYMBOL'''


def p_bundleid(p):
    '''bundleid : SYMBOL'''


def p_bundlebody(p):
    '''bundlebody : LEFT_BRACE bundle_decl RIGHT_BRACE'''


def p_bundle_decl(p):
    '''bundle_decl :
                   | bundle_statements'''


def p_bundlestatements(p):
    '''bundlestatements : bundlestatement
                        | bundlestatement bundlestatements'''


def p_bundlestatement(p):
    '''bundlestatement : promise_guard classpromises_decl'''


def p_promise_guard(p):
    '''promise_guard : PROMISE_GUARD'''


def p_classpromises_decl(p):
    '''classpromises_decl :
                          | classpromises'''


def p_classpromises(p):
    '''classpromises : classpromise
                     | classpromise classpromises'''


def p_classpromise(p):
    '''classpromise : classguard
                    | promise_decl'''


def p_promise_decl(p):
    '''promise_decl : promise_line SEMICOLON'''


def p_promise_line(p):
    '''promise_line : promiser constraints_decl
                    | promiser promise_arrow rval constraints_decl'''


def p_promiser(p):
    '''promiser : QUOTED_STRING'''


def p_constraints_decl(p):
    '''constraints_decl :
                        | constraints'''


def p_constraints(p):
    '''constraints : constraint
                   | constraint separator constraints'''


def p_constraint(p):
    '''constraint : constraint_id hash_rocket rval'''


def p_constraint_id(p):
    '''constraint_id : IDENTIFIER'''


##### Body #####

def p_body(p):
    '''body : BODY bodytype bodyid arglist bodybody'''


##### Promise #####

def p_promise(p):
    '''promise : PROMISE promisetype promiseid arglist bodybody'''


##### Argument list #####

def p_arglist(p):
    '''arglist :
               | LEFT_PAR RIGHT_PAR
               | LEFT_PAR arglist_items RIGHT_PAR
               | LEFT_PAR arglist_items COMMA RIGHT_PAR'''


def p_arglist_items(p):
    '''arglist_items : arglist_item
                     | arglist_item COMMA
                     | arglist_item COMMA arglist_items'''


def p_arglist_item(p):
    '''arglist_item : IDENTIFIER'''


##### List #####

def p_list(p):
    '''list : LEFT_BRACE RIGHT_BRACE
            | LEFT_BRACE list_items RIGHT_BRACE
            | LEFT_BRACE list_items COMMA RIGHT_BRACE'''


def p_list_items(p):
    '''list_items : list_item
                  | list_item COMMA list_items'''


def p_list_item(p):
    '''list_item : IDENTIFIER
                 | QUOTED_STRING
                 | NAKED_VAR
                 | usefunction'''



##### Common #####

def p_rval(p):
    '''rval : IDENTIFIER
            | QUOTED_STRING
            | NAKED_VAR
            | list
            | usefunction'''



def p_error(p):
    print("Error")


bparser = yacc.yacc()


def parse(data, debug=0):
    bparser.error = 0
    p = bparser.parse(data, debug=debug)
    if bparser.error:
        return None
    return p
