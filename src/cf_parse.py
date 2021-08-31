import sys
from logger import Logger
import ply.yacc as yacc
import cf_lex

tokens = cf_lex.tokens

##### Policy #####


def p_policy(p):
    """policy :
              | blocks"""
    if len(p) == 1:
        pretty("", p)
    else:
        p[0] = p[1]


def p_blocks(p):
    """blocks : block
              | block blocks"""
    if len(p) == 2:
        pretty("%s", p)
    else:
        pretty("%s\n\n%s", p)


def p_block(p):
    """block : bundle
             | body
             | promise"""
    pretty("%s", p)


##### Bundle #####


def p_bundle(p):
    """bundle : BUNDLE bundletype bundleid arglist bundlebody"""
    pretty("%s %s %s%s\n%s", p)


def p_bundletype(p):
    """bundletype : IDENTIFIER"""
    pretty("%s", p)


def p_bundleid(p):
    """bundleid : IDENTIFIER"""
    pretty("%s", p)


def p_bundlebody(p):
    """bundlebody : LEFT_BRACE bundle_decl RIGHT_BRACE"""
    pretty("%s\n%s\n%s", p)


def p_bundle_decl(p):
    """bundle_decl :
                   | bundlestatements"""
    if len(p) == 1:
        pretty("", p)
    else:
        pretty("%s", p)


def p_bundlestatements(p):
    """bundlestatements : bundlestatement
                        | bundlestatement bundlestatements"""
    if len(p) == 2:
        pretty("%s", p)
    else:
        pretty("%s\n%s", p)


def p_bundlestatement(p):
    """bundlestatement : promise_guard classpromises_decl"""
    pretty("%s\n%s", p)


def p_promise_guard(p):
    """promise_guard : PROMISE_GUARD"""
    pretty("  %s", p)


def p_classpromises_decl(p):
    """classpromises_decl :
                          | classpromises"""
    if len(p) == 1:
        pretty("", p)
    else:
        pretty("%s", p)


def p_classpromises(p):
    """classpromises : classpromise
                     | classpromise classpromises"""
    if len(p) == 2:
        pretty("%s", p)
    else:
        pretty("%s\n%s", p)


def p_classpromise(p):
    """classpromise : classguard
                    | promise_decl"""
    pretty("%s", p)


def p_promise_decl(p):
    """promise_decl : promise_line SEMICOLON"""
    pretty("%s%s", p)


def p_promise_line(p):
    """promise_line : promiser constraints_decl
                    | promiser PROMISE_ARROW rval constraints_decl"""
    if len(p) == 3:
        pretty("%s%s", p)
    else:
        pretty("%s %s %s%s", p)


def p_promiser(p):
    """promiser : QUOTED_STRING"""
    pretty("      %s", p)


def p_constraints_decl(p):
    """constraints_decl :
                        | constraints"""
    if len(p) == 1:
        pretty("", p)
    else:
        pretty("%s", p)


def p_constraints(p):
    """constraints : constraint
                   | constraint COMMA constraints"""
    if len(p) == 2:
        pretty("%s", p)
    else:
        pretty("%s%s %s", p)


def p_constraint(p):
    """constraint : constraint_id HASH_ROCKET rval"""
    pretty("%s %s %s", p)


def p_constraint_id(p):
    """constraint_id : IDENTIFIER"""
    pretty("%s", p)


##### Body #####


def p_body(p):
    """body : BODY bodytype bodyid arglist bodybody"""
    pretty("%s %s %s%s\n%s", p)


def p_bodytype(p):
    """bodytype : IDENTIFIER"""
    pretty("%s", p)


def p_bodyid(p):
    """bodyid : IDENTIFIER"""
    pretty("%s", p)


def p_bodybody(p):
    """bodybody : LEFT_BRACE inner_bodybody RIGHT_BRACE"""
    pretty("%s\n%s\n%s", p)


def p_inner_bodybody(p):
    """inner_bodybody :
                      | bodyattribs"""
    if len(p) == 1:
        pretty("", p)
    else:
        pretty("%s", p)


def p_bodyattribs(p):
    """bodyattribs : bodyattrib
                   | bodyattrib bodyattribs"""
    if len(p) == 2:
        pretty("%s", p)
    else:
        pretty("%s\n%s", p)


def p_bodyattrib(p):
    """bodyattrib : classguard
                  | selection SEMICOLON"""
    if len(p) == 2:
        pretty("%s", p)
    else:
        pretty("%s%s", p)


def p_selection(p):
    """selection : selection_id HASH_ROCKET rval"""
    pretty("%s %s %s", p)


def p_selection_id(p):
    """selection_id : IDENTIFIER"""
    pretty("%s", p)


##### Promise #####


def p_promise(p):
    """promise : PROMISE promisetype promiseid arglist bodybody"""
    pretty("%s %s %s%s\n%s")


def p_promisetype(p):
    """promisetype : IDENTIFIER"""
    pretty("%s", p)


def p_promiseid(p):
    """promiseid : IDENTIFIER"""
    pretty("%s", p)


##### Argument list #####


def p_arglist(p):
    """arglist :
               | LEFT_PAR RIGHT_PAR
               | LEFT_PAR arglist_items RIGHT_PAR
               | LEFT_PAR arglist_items COMMA RIGHT_PAR"""
    if len(p) == 1:
        pretty("", p)
    elif len(p) == 3:
        pretty("%s%s", p)
    elif len(p) == 4:
        pretty("%s%s%s", p)
    else:
        pretty("%s%s%s%s", p)


def p_arglist_items(p):
    """arglist_items : arglist_item
                     | arglist_items COMMA arglist_item"""
    if len(p) == 2:
        pretty("%s", p)
    else:
        pretty("%s%s %s", p)


def p_arglist_item(p):
    """arglist_item : IDENTIFIER"""
    pretty("%s", p)


##### List #####


def p_list(p):
    """list : LEFT_BRACE RIGHT_BRACE
            | LEFT_BRACE list_items RIGHT_BRACE
            | LEFT_BRACE list_items COMMA RIGHT_BRACE"""
    if len(p) == 3:
        pretty("%s%s", p)
    elif len(p) == 4:
        pretty("%s%s%s", p)
    elif len(p) == 5:
        pretty("%s%s%s%s", p)


def p_list_items(p):
    """list_items : list_item
                  | list_items COMMA list_item"""
    if len(p) == 2:
        pretty("%s", p)
    else:
        pretty("%s%s %s", p)


def p_list_item(p):
    """list_item : IDENTIFIER
                 | QUOTED_STRING
                 | NAKED_VAR
                 | usefunction"""
    pretty("%s", p)


##### Function #####


def p_usefunction(p):
    """usefunction : function_id farglist"""
    pretty("%s%s", p)


def p_function_id(p):
    """function_id : IDENTIFIER
                   | NAKED_VAR"""
    pretty("%s", p)


def p_farglist(p):
    """farglist : LEFT_PAR RIGHT_PAR
                | LEFT_PAR farglist_items RIGHT_PAR
                | LEFT_PAR farglist_items COMMA RIGHT_PAR"""
    if len(p) == 3:
        pretty("%s%s", p)
    if len(p) == 4:
        pretty("%s%s%s", p)
    else:
        pretty("%s%s%s%s", p)


def p_farglist_items(p):
    """farglist_items : farglist_item
                      | farglist_items COMMA farglist_item"""
    if len(p) == 2:
        pretty("%s", p)
    else:
        pretty("%s%s %s", p)


def p_farglist_item(p):
    """farglist_item : IDENTIFIER
                     | QUOTED_STRING
                     | NAKED_VAR
                     | usefunction"""
    pretty("%s", p)


##### Common #####


def p_classguard(p):
    """classguard : CLASS_GUARD"""
    pretty("    %s", p)


def p_rval(p):
    """rval : IDENTIFIER
            | QUOTED_STRING
            | NAKED_VAR
            | list
            | usefunction"""
    pretty("%s", p)


def p_comments(p):
    """comments :
                | comment
                | comment comments"""


def p_comment(p):
    """comment : COMMENT"""


def p_error(p):
    logger = Logger()
    logger.log_error("Parser error: There are sytax errors in policy file")
    logger.log_debug(p)
    sys.exit(1)


def pretty(fstr, p):
    if len(p) > 1:
        p[0] = fstr % tuple(p[1:])
    else:
        p[0] = fstr


cf_parser = yacc.yacc()


def parse_policy(data, debug=0):
    cf_parser.error = 0
    p = cf_parser.parse(data, debug=debug)
    if cf_parser.error:
        return None
    return p
