import ply.lex as lex
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
    '''bundletype : IDENTIFIER'''


def p_bundleid(p):
    '''bundleid : IDENTIFIER'''


def p_bundlebody(p):
    '''bundlebody : LEFT_BRACE bundle_decl RIGHT_BRACE'''


def p_bundle_decl(p):
    '''bundle_decl :
                   | bundlestatements'''


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
                    | promiser PROMISE_ARROW rval constraints_decl'''


def p_promiser(p):
    '''promiser : QUOTED_STRING'''


def p_constraints_decl(p):
    '''constraints_decl :
                        | constraints'''


def p_constraints(p):
    '''constraints : constraint
                   | constraint COMMA constraints'''


def p_constraint(p):
    '''constraint : constraint_id HASH_ROCKET rval'''


def p_constraint_id(p):
    '''constraint_id : IDENTIFIER'''


##### Body #####

def p_body(p):
    '''body : BODY bodytype bodyid arglist bodybody'''


def p_bodytype(p):
    '''bodytype : IDENTIFIER'''


def p_bodyid(p):
    '''bodyid : IDENTIFIER'''


def p_bodybody(p):
    '''bodybody : LEFT_BRACE inner_bodybody RIGHT_BRACE'''


def p_inner_bodybody(p):
    '''inner_bodybody :
                      | bodyattribs'''


def p_bodyattribs(p):
    '''bodyattribs : bodyattrib
                   | bodyattrib bodyattribs'''


def p_bodyattrib(p):
    '''bodyattrib : classguard
                  | selection SEMICOLON'''


def p_selection(p):
    '''selection : selection_id HASH_ROCKET rval'''


def p_selection_id(p):
    '''selection_id : IDENTIFIER'''


##### Promise #####

def p_promise(p):
    '''promise : PROMISE promisetype promiseid arglist bodybody'''


def p_promisetype(p):
    '''promisetype : IDENTIFIER'''


def p_promiseid(p):
    '''promiseid : IDENTIFIER'''


##### Argument list #####

def p_arglist(p):
    '''arglist :
               | LEFT_PAR RIGHT_PAR
               | LEFT_PAR arglist_items RIGHT_PAR
               | LEFT_PAR arglist_items COMMA RIGHT_PAR'''


def p_arglist_items(p):
    '''arglist_items : arglist_item
                     | arglist_items COMMA arglist_item'''


def p_arglist_item(p):
    '''arglist_item : IDENTIFIER'''


##### List #####

def p_list(p):
    '''list : LEFT_BRACE RIGHT_BRACE
            | LEFT_BRACE list_items RIGHT_BRACE
            | LEFT_BRACE list_items COMMA RIGHT_BRACE'''


def p_list_items(p):
    '''list_items : list_item
                  | list_items COMMA list_item'''


def p_list_item(p):
    '''list_item : IDENTIFIER
                 | QUOTED_STRING
                 | NAKED_VAR
                 | usefunction'''


##### Function #####

def p_usefunction(p):
    '''usefunction : function_id farglist'''


def p_function_id(p):
    '''function_id : IDENTIFIER
                   | NAKED_VAR'''

def p_farglist(p):
    '''farglist : LEFT_PAR RIGHT_PAR
                | LEFT_PAR farglist_items RIGHT_PAR
                | LEFT_PAR farglist_items COMMA RIGHT_PAR'''

def p_farglist_items(p):
    '''farglist_items : farglist_item
                      | farglist_items COMMA farglist_item'''


def p_farglist_item(p):
    '''farglist_item : IDENTIFIER
                     | QUOTED_STRING
                     | NAKED_VAR
                     | usefunction'''


##### Common #####

def p_classguard(p):
    '''classguard : CLASS_GUARD'''


def p_rval(p):
    '''rval : IDENTIFIER
            | QUOTED_STRING
            | NAKED_VAR
            | list
            | usefunction'''


def p_error(p):
    print("Parser error")


def print_debug(p):
    print("Parse:")
    print("\t", end="")
    first = True
    for e in reversed(p.slice):
        if first:
            first = False
        else:
            print(" -> ", end="")
        if isinstance(e, lex.LexToken):
            print("'%s'" % e.value, end="")
        else:
            print(e, end="")
    print()


cf_parser = yacc.yacc()


def parse(data, debug=0):
    cf_parser.error = 0
    p = cf_parser.parse(data, debug=debug)
    if cf_parser.error:
        return None
    return p
