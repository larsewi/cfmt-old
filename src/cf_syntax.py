from abc import ABC, abstractmethod
from pretty_printer import PrettyPrinter
from logger import Logger


class Syntax(ABC):
    logger = Logger()
    pp = PrettyPrinter()
    indent = 0
    INDENT_SIZE = 2

    def __init__(self, p):
        self._lineno = p.lineno(0)
        self._linespan = p.linespan(0)
        self._lexpos = p.lexpos(0)
        self._lexspan = p.lexspan(0)
        self._children = p[1:]
        p[0] = self

    def pretty(self, pp):
        pass

    def collect(self, *symbols):
        result = []
        for child in self._children:
            if isinstance(child, str):
                # Don't collect tokens
                pass
            elif isinstance(child, symbols):
                result.append(child)
            else:
                result += child.collect(symbols)
        return result

    def log_syntax_tree(self):
        Syntax.logger.log_debug(" " * Syntax.indent + "<%s>" % self.__class__.__name__)
        Syntax.indent += Syntax.INDENT_SIZE
        for child in self._children:
            if isinstance(child, Syntax):
                child.log_syntax_tree()
        Syntax.indent -= Syntax.INDENT_SIZE
        Syntax.logger.log_debug(" " * Syntax.indent + "</%s>" % self.__class__.__name__)


##### Policy #####


class Policy(Syntax):
    def pretty(self, pp):
        nonterms = self.collect(Bundle, Body, Promise, Comment, Macro)

        last = None
        for cur in nonterms:
            if not (
                last is None
                or isinstance(last, Comment)
                and cur._lineno - last._lineno == 1
            ):
                pp.println()

            cur.pretty(pp)
            pp.println()
            last = cur


class Blocks(Syntax):
    pass


class Block(Syntax):
    pass


##### Bundle #####


class Bundle(Syntax):
    def pretty(self, pp):
        stash = []
        bundlekeyword, bundletype, bundleid, arglist, bundlebody = self._children

        bundlekeyword.pretty(pp)
        stash += bundlekeyword.collect(Comment, Macro)

        pp.print(" ")

        bundletype.pretty(pp)
        bundletype.collect(Comment, Macro)

        pp.print(" ")

        bundleid.pretty(pp)
        bundleid.collect(Comment, Macro)

        arglist.pretty(pp)

        pp.println()

        bundlebody.pretty(pp)


class BundleKeyword(Syntax):
    def pretty(self, pp):
        bundlekeyword, = self._children
        pp.print(bundlekeyword)


class BundleType(Syntax):
    def pretty(self, pp):
        bundletype, = self._children
        pp.print(bundletype)


class BundleID(Syntax):
    def pretty(self, pp):
        bundleid, = self._children
        pp.print(bundleid)


class BundleBody(Syntax):
    def pretty(self, pp):
        pass


class BundleStatements(Syntax):
    def pretty(self, pp):
        pass


class BundleStatement(Syntax):
    def pretty(self, pp):
        pass


class PromiseGuard(Syntax):
    def pretty(self, pp):
        pass


class ClassPromises(Syntax):
    def pretty(self, pp):
        pass


class ClassPromise(Syntax):
    def pretty(self, pp):
        pass


class PromiseLine(Syntax):
    def pretty(self, pp):
        pass


class Promiser(Syntax):
    def pretty(self, pp):
        pass


class Constraints(Syntax):
    def pretty(self, pp):
        pass


class Constraint(Syntax):
    def pretty(self, pp):
        pass


class ConstraintID(Syntax):
    def pretty(self, pp):
        pass


##### Body #####


class Body(Syntax):
    def pretty(self, pp):
        pass


class BodyType(Syntax):
    def pretty(self, pp):
        pass


class BodyID(Syntax):
    def pretty(self, pp):
        pass


class BodyBody(Syntax):
    def pretty(self, pp):
        pass


class BodyAttribs(Syntax):
    def pretty(self, pp):
        pass


class BodyAttrib(Syntax):
    def pretty(self, pp):
        pass


class Selection(Syntax):
    def pretty(self, pp):
        pass


class SelectionID(Syntax):
    def pretty(self, pp):
        pass


##### Promise #####


class Promise(Syntax):
    def pretty(self, pp):
        pass


class PromiseType(Syntax):
    def pretty(self, pp):
        pass


class PromiseID(Syntax):
    def pretty(self, pp):
        pass


##### Argument List #####


class ArgList(Syntax):
    def pretty(self, pp):
        pass


class ArgListItems(Syntax):
    def pretty(self, pp):
        pass


class ArgListItem(Syntax):
    def pretty(self, pp):
        pass


##### List #####


class List(Syntax):
    def pretty(self, pp):
        pass


class ListItems(Syntax):
    def pretty(self, pp):
        pass


class ListItem(Syntax):
    def pretty(self, pp):
        pass


##### Function #####


class Function(Syntax):
    def pretty(self, pp):
        pass


class FunctionID(Syntax):
    def pretty(self, pp):
        pass


class FnArgList(Syntax):
    def pretty(self, pp):
        pass


class FnArgListItems(Syntax):
    def pretty(self, pp):
        pass


class FnArgListItem(Syntax):
    def pretty(self, pp):
        pass


##### Common #####


class ClassGuard(Syntax):
    def pretty(self, pp):
        pass


class RVal(Syntax):
    def pretty(self, pp):
        pass


class CommentsAndMacros(Syntax):
    pass


class Comment(Syntax):
    def pretty(self, pp):
        comment, = self._children
        pp.print(comment)


class Macro(Syntax):
    def pretty(self, pp):
        pass


class LeftPar(Syntax):
    def pretty(self, pp):
        leftpar, = self._children
        pp.print(leftpar)


class RightPar(Syntax):
    def pretty(self, pp):
        rightpar, = self._children
        pp.print(rightpar)


class Comma(Syntax):
    def pretty(self, pp):
        comma, = self._children
        pp.print(comma)
