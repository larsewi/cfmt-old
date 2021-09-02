import sys
from cf_syntax import *
from logger import Logger
import ply.yacc as yacc
import cf_lex

tokens = cf_lex.tokens

##### Policy #####


def p_policy(p):
    """policy :
              | blocks"""
    Policy(p)


def p_blocks(p):
    """blocks : block
              | block blocks"""
    Blocks(p)


def p_block(p):
    """block : bundle
             | body
             | promise
             | comment
             | macro"""
    Block(p)


##### Bundle #####


def p_bundle(p):
    """bundle : BUNDLE bundletype bundleid arglist bundlebody"""
    Bundle(p)


def p_bundletype(p):
    """bundletype : IDENTIFIER"""
    BundleType(p)


def p_bundleid(p):
    """bundleid : IDENTIFIER"""
    BundleID(p)


def p_bundlebody(p):
    """bundlebody : LEFT_BRACE RIGHT_BRACE
                  | LEFT_BRACE bundlestatements RIGHT_BRACE"""
    BundleBody(p)


def p_bundlestatements(p):
    """bundlestatements : bundlestatement
                        | bundlestatement bundlestatements"""
    BundleStatements(p)


def p_bundlestatement(p):
    """bundlestatement : promise_guard
                       | promise_guard classpromises"""
    BundleStatement(p)


def p_promise_guard(p):
    """promise_guard : PROMISE_GUARD"""
    PromiseGuard(p)


def p_classpromises(p):
    """classpromises : classpromise
                     | classpromise classpromises"""
    ClassPromises(p)


def p_classpromise(p):
    """classpromise : classguard
                    | promise_line SEMICOLON"""
    ClassPromise(p)


def p_promise_line(p):
    """promise_line : promiser
                    | promiser constraints
                    | promiser PROMISE_ARROW rval constraints"""
    PromiseLine(p)


def p_promiser(p):
    """promiser : QUOTED_STRING"""
    Promiser(p)



def p_constraints(p):
    """constraints : constraint
                   | constraint COMMA constraints"""
    Constraints(p)


def p_constraint(p):
    """constraint : constraint_id HASH_ROCKET rval"""
    Constraint(p)


def p_constraint_id(p):
    """constraint_id : IDENTIFIER"""
    ConstraintID(p)


##### Body #####


def p_body(p):
    """body : BODY bodytype bodyid arglist bodybody"""
    Body(p)


def p_bodytype(p):
    """bodytype : IDENTIFIER"""
    BodyType(p)


def p_bodyid(p):
    """bodyid : IDENTIFIER"""
    BodyID(p)


def p_bodybody(p):
    """bodybody : LEFT_BRACE RIGHT_BRACE
                | LEFT_BRACE bodyattribs RIGHT_BRACE"""
    BodyBody(p)


def p_bodyattribs(p):
    """bodyattribs : bodyattrib
                   | bodyattrib bodyattribs"""
    BodyAttribs(p)


def p_bodyattrib(p):
    """bodyattrib : classguard
                  | selection SEMICOLON"""
    BodyAttrib(p)


def p_selection(p):
    """selection : selection_id HASH_ROCKET rval"""
    Selection(p)


def p_selection_id(p):
    """selection_id : IDENTIFIER"""
    SelectionID(p)


##### Promise #####


def p_promise(p):
    """promise : PROMISE promisetype promiseid arglist bodybody"""
    Promise(p)


def p_promisetype(p):
    """promisetype : IDENTIFIER"""
    PromiseType(p)


def p_promiseid(p):
    """promiseid : IDENTIFIER"""
    PromiseID(p)


##### Argument list #####


def p_arglist(p):
    """arglist :
               | LEFT_PAR RIGHT_PAR
               | LEFT_PAR arglist_items RIGHT_PAR
               | LEFT_PAR arglist_items COMMA RIGHT_PAR"""
    ArgList(p)


def p_arglist_items(p):
    """arglist_items : arglist_item
                     | arglist_items COMMA arglist_item"""
    ArgListItems(p)


def p_arglist_item(p):
    """arglist_item : IDENTIFIER"""
    ArgListItem(p)


##### List #####


def p_list(p):
    """list : LEFT_BRACE RIGHT_BRACE
            | LEFT_BRACE list_items RIGHT_BRACE
            | LEFT_BRACE list_items COMMA RIGHT_BRACE"""
    List(p)


def p_list_items(p):
    """list_items : list_item
                  | list_items COMMA list_item"""
    ListItems(p)


def p_list_item(p):
    """list_item : IDENTIFIER
                 | QUOTED_STRING
                 | NAKED_VAR
                 | function"""
    ListItem(p)


##### Function #####


def p_function(p):
    """function : function_id fn_arglist"""
    Function(p)


def p_function_id(p):
    """function_id : IDENTIFIER
                   | NAKED_VAR"""
    FunctionID(p)


def p_fn_arglist(p):
    """fn_arglist : LEFT_PAR RIGHT_PAR
                | LEFT_PAR fn_arglist_items RIGHT_PAR
                | LEFT_PAR fn_arglist_items COMMA RIGHT_PAR"""
    FnArgList(p)


def p_fn_arglist_items(p):
    """fn_arglist_items : fn_arglist_item
                        | fn_arglist_items COMMA fn_arglist_item"""
    FnArgListItems(p)


def p_fn_arglist_item(p):
    """fn_arglist_item : IDENTIFIER
                       | QUOTED_STRING
                       | NAKED_VAR
                       | function"""
    FnArgListItem(p)


##### Common #####


def p_classguard(p):
    """classguard : CLASS_GUARD"""
    ClassGuard(p)


def p_rval(p):
    """rval : IDENTIFIER
            | QUOTED_STRING
            | NAKED_VAR
            | list
            | function"""
    RVal(p)


# Comments or Macros
def p_cms(p):
    """cms :
           | cm
           | cm cms"""
    CMS(p)


# Comment or Macro
def p_cm(p):
    """cm : comment
          | macro"""
    CM(p)


def p_comment(p):
    """comment : COMMENT"""
    Comment(p)


def p_macro(p):
    """macro : MACRO"""
    Macro(p)


def p_error(p):
    logger = Logger()
    logger.log_error("Parser error: There are sytax errors in policy file")
    logger.log_debug(p)
    sys.exit(1)


cf_parser = yacc.yacc()


def parse_policy(data, debug=0):
    cf_parser.error = 0
    p = cf_parser.parse(data, debug=debug, tracking=True)
    if cf_parser.error:
        return None
    return p
