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

    @abstractmethod
    def pretty(self, pp):
        pass

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
        for child in self._children:
            child.pretty(pp)


class Blocks(Syntax):
    def pretty(self, pp):
        for child in self._children:
            child.pretty(pp)


class Block(Syntax):
    def pretty(self, pp):
        for child in self._children:
            print(child._lineno)


##### Bundle #####


class Bundle(Syntax):
    def pretty(self, pp):
        pass


class BundleType(Syntax):
    def pretty(self, pp):
        pass


class BundleID(Syntax):
    def pretty(self, pp):
        pass


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


# Comments or Macros
class CMS(Syntax):
    def pretty(self, pp):
        pass


# Comment or Macro
class CM(Syntax):
    def pretty(self, pp):
        pass


class Comment(Syntax):
    def pretty(self, pp):
        pass


class Macro(Syntax):
    def pretty(self, pp):
        pass
