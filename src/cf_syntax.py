from abc import ABC, abstractmethod
from logger import Logger


class Syntax(ABC):
    indent = 0
    INDENT_SIZE = 2

    def __init__(self, p):
        self._logger = Logger()
        self._children = p

    @abstractmethod
    def pretty(self):
        pass

    def log_syntax_tree(self):
        self._logger.log_debug(" " * Syntax.indent + "<%s>" % self.__class__.__name__)
        Syntax.indent += Syntax.INDENT_SIZE
        for child in self._children:
            if isinstance(child, Syntax):
                child.log_syntax_tree()
        Syntax.indent -= Syntax.INDENT_SIZE
        self._logger.log_debug(" " * Syntax.indent + "</%s>" % self.__class__.__name__)


##### Policy #####


class Policy(Syntax):
    def pretty(self):
        pass


class Blocks(Syntax):
    def pretty(self):
        pass


class Block(Syntax):
    def pretty(self):
        pass


##### Bundle #####


class Bundle(Syntax):
    def pretty(self):
        pass


class BundleType(Syntax):
    def pretty(self):
        pass


class BundleID(Syntax):
    def pretty(self):
        pass


class BundleBody(Syntax):
    def pretty(self):
        pass


class BundleStatements(Syntax):
    def pretty(self):
        pass


class BundleStatement(Syntax):
    def pretty(self):
        pass


class PromiseGuard(Syntax):
    def pretty(self):
        pass


class ClassPromises(Syntax):
    def pretty(self):
        pass

class ClassPromise(Syntax):
    def pretty(self):
        pass


class PromiseLine(Syntax):
    def pretty(self):
        pass


class Promiser(Syntax):
    def pretty(self):
        pass


class Constraints(Syntax):
    def pretty(self):
        pass


class Constraint(Syntax):
    def pretty(self):
        pass


class ConstraintID(Syntax):
    def pretty(self):
        pass


##### Body #####


class Body(Syntax):
    def pretty(self):
        pass


class BodyType(Syntax):
    def pretty(self):
        pass


class BodyID(Syntax):
    def pretty(self):
        pass


class BodyBody(Syntax):
    def pretty(self):
        pass


class BodyAttribs(Syntax):
    def pretty(self):
        pass


class BodyAttrib(Syntax):
    def pretty(self):
        pass


class Selection(Syntax):
    def pretty(self):
        pass


class SelectionID(Syntax):
    def pretty(self):
        pass


##### Promise #####


class Promise(Syntax):
    def pretty(self):
        pass


class PromiseType(Syntax):
    def pretty(self):
        pass


class PromiseID(Syntax):
    def pretty(self):
        pass


##### Argument List #####


class ArgList(Syntax):
    def pretty(self):
        pass


class ArgListItems(Syntax):
    def pretty(self):
        pass


class ArgListItem(Syntax):
    def pretty(self):
        pass


##### List #####


class List(Syntax):
    def pretty(self):
        pass


class ListItems(Syntax):
    def pretty(self):
        pass


class ListItem(Syntax):
    def pretty(self):
        pass


##### Function #####


class Function(Syntax):
    def pretty(self):
        pass


class FunctionID(Syntax):
    def pretty(self):
        pass


class FnArgList(Syntax):
    def pretty(self):
        pass


class FnArgListItems(Syntax):
    def pretty(self):
        pass


class FnArgListItem(Syntax):
    def pretty(self):
        pass


##### Common #####


class ClassGuard(Syntax):
    def pretty(self):
        pass


class RVal(Syntax):
    def pretty(self):
        pass


class Comment(Syntax):
    def pretty(self):
        pass
