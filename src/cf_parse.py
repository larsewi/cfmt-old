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
    p[0] = Policy(p[1:])


def p_blocks(p):
    """blocks : block
              | block blocks"""
    p[0] = Blocks(p[1:])


def p_block(p):
    """block : bundle
             | body
             | promise
             | comment"""
    p[0] = Block(p[1:])


##### Bundle #####


def p_bundle(p):
    """bundle : BUNDLE bundletype bundleid arglist bundlebody"""
    p[0] = Bundle(p[1:])


def p_bundletype(p):
    """bundletype : IDENTIFIER"""
    p[0] = BundleType(p[1:])


def p_bundleid(p):
    """bundleid : IDENTIFIER"""
    p[0] = BundleID(p[1:])


def p_bundlebody(p):
    """bundlebody : LEFT_BRACE RIGHT_BRACE
                  | LEFT_BRACE bundlestatements RIGHT_BRACE"""
    p[0] = BundleBody(p[1:])


def p_bundlestatements(p):
    """bundlestatements : bundlestatement
                        | bundlestatement bundlestatements"""
    p[0] = BundleStatements(p[1:])


def p_bundlestatement(p):
    """bundlestatement : promise_guard
                       | promise_guard classpromises"""
    p[0] = BundleStatement(p[1:])


def p_promise_guard(p):
    """promise_guard : PROMISE_GUARD"""
    p[0] = PromiseGuard(p[1:])


def p_classpromises(p):
    """classpromises : classpromise
                     | classpromise classpromises"""
    p[0] = ClassPromises(p[1:])


def p_classpromise(p):
    """classpromise : classguard
                    | promise_line SEMICOLON"""
    p[0] = ClassPromise(p[1:])


def p_promise_line(p):
    """promise_line : promiser
                    | promiser constraints
                    | promiser PROMISE_ARROW rval constraints"""
    p[0] = PromiseLine(p[1:])


def p_promiser(p):
    """promiser : QUOTED_STRING"""
    p[0] = Promiser(p[1:])



def p_constraints(p):
    """constraints : constraint
                   | constraint COMMA constraints"""
    p[0] = Constraints(p[1:])


def p_constraint(p):
    """constraint : constraint_id HASH_ROCKET rval"""
    p[0] = Constraint(p[1:])


def p_constraint_id(p):
    """constraint_id : IDENTIFIER"""
    p[0] = ConstraintID(p[1:])


##### Body #####


def p_body(p):
    """body : BODY bodytype bodyid arglist bodybody"""
    p[0] = Body(p[1:])


def p_bodytype(p):
    """bodytype : IDENTIFIER"""
    p[0] = BodyType(p[1:])


def p_bodyid(p):
    """bodyid : IDENTIFIER"""
    p[0] = BodyID(p[1:])


def p_bodybody(p):
    """bodybody : LEFT_BRACE RIGHT_BRACE
                | LEFT_BRACE bodyattribs RIGHT_BRACE"""
    p[0] = BodyBody(p[1:])


def p_bodyattribs(p):
    """bodyattribs : bodyattrib
                   | bodyattrib bodyattribs"""
    p[0] = BodyAttribs(p[1:])


def p_bodyattrib(p):
    """bodyattrib : classguard
                  | selection SEMICOLON"""
    p[0] = BodyAttrib(p[1:])


def p_selection(p):
    """selection : selection_id HASH_ROCKET rval"""
    p[0] = Selection(p[1:])


def p_selection_id(p):
    """selection_id : IDENTIFIER"""
    p[0] = SelectionID(p[1:])


##### Promise #####


def p_promise(p):
    """promise : PROMISE promisetype promiseid arglist bodybody"""
    p[0] = Promise(p[1:])


def p_promisetype(p):
    """promisetype : IDENTIFIER"""
    p[0] = PromiseType(p[1:])


def p_promiseid(p):
    """promiseid : IDENTIFIER"""
    p[0] = PromiseID(p[1:])


##### Argument list #####


def p_arglist(p):
    """arglist :
               | LEFT_PAR RIGHT_PAR
               | LEFT_PAR arglist_items RIGHT_PAR
               | LEFT_PAR arglist_items COMMA RIGHT_PAR"""
    p[0] = ArgList(p[1:])


def p_arglist_items(p):
    """arglist_items : arglist_item
                     | arglist_items COMMA arglist_item"""
    p[0] = ArgListItems(p[1:])


def p_arglist_item(p):
    """arglist_item : IDENTIFIER"""
    p[0] = ArgListItem(p[1:])


##### List #####


def p_list(p):
    """list : LEFT_BRACE RIGHT_BRACE
            | LEFT_BRACE list_items RIGHT_BRACE
            | LEFT_BRACE list_items COMMA RIGHT_BRACE"""
    p[0] = List(p[1:])


def p_list_items(p):
    """list_items : list_item
                  | list_items COMMA list_item"""
    p[0] = ListItems(p[1:])


def p_list_item(p):
    """list_item : IDENTIFIER
                 | QUOTED_STRING
                 | NAKED_VAR
                 | function"""
    p[0] = ListItem(p[1:])


##### Function #####


def p_function(p):
    """function : function_id fn_arglist"""
    p[0] = Function(p[1:])


def p_function_id(p):
    """function_id : IDENTIFIER
                   | NAKED_VAR"""
    p[0] = FunctionID(p[1:])


def p_fn_arglist(p):
    """fn_arglist : LEFT_PAR RIGHT_PAR
                | LEFT_PAR fn_arglist_items RIGHT_PAR
                | LEFT_PAR fn_arglist_items COMMA RIGHT_PAR"""
    p[0] = FnArgList(p[1:])


def p_fn_arglist_items(p):
    """fn_arglist_items : fn_arglist_item
                        | fn_arglist_items COMMA fn_arglist_item"""
    p[0] = FnArgListItems(p[1:])


def p_fn_arglist_item(p):
    """fn_arglist_item : IDENTIFIER
                       | QUOTED_STRING
                       | NAKED_VAR
                       | function"""
    p[0] = FnArgListItem(p[1:])


##### Common #####


def p_classguard(p):
    """classguard : CLASS_GUARD"""
    p[0] = ClassGuard(p[1:])


def p_rval(p):
    """rval : IDENTIFIER
            | QUOTED_STRING
            | NAKED_VAR
            | list
            | function"""
    p[0] = RVal(p[1:])


def p_comment(p):
    """comment : COMMENT"""
    p[0] = Comment(p[1:])


def p_error(p):
    logger = Logger()
    logger.log_error("Parser error: There are sytax errors in policy file")
    logger.log_debug(p)
    sys.exit(1)


cf_parser = yacc.yacc()


def parse_policy(data, debug=0):
    cf_parser.error = 0
    p = cf_parser.parse(data, debug=debug)
    if cf_parser.error:
        return None
    return p
