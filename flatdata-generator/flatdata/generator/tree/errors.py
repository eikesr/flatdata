'''
 Copyright (c) 2017 HERE Europe B.V.
 See the LICENSE file in the root of this project for license details.
'''


class FlatdataSyntaxError(RuntimeError):
    pass


class SymbolRedefinition(FlatdataSyntaxError):
    def __init__(self, duplicate, existing):
        super().__init__(
            "Symbol redefined: {duplicate} already exists at {existing}".format(
                duplicate=duplicate,
                existing=existing))


class CircularReferencing(FlatdataSyntaxError):
    def __init__(self, node, child):
        super().__init__(
            "Circular reference in schema: {node} -> {child}".format(
                node=node, child=child))


class MissingSymbol(FlatdataSyntaxError):
    def __init__(self, name, options, node):
        message = "Missing symbol \"{name}\" in {path}.".format(
            name=name, path=node.path)
        try:
            import Levenshtein
            options = sorted(
                [(Levenshtein.distance(name, option.split('.')[-1]), option)
                 for option in options],
                key=lambda x: x[0])
            if options:
                message += " Did you mean \"{options}\"?".format(
                    options=options[0][1])
        except ImportError:
            pass
        super().__init__(message)


class IncorrectReferenceType(FlatdataSyntaxError):
    def __init__(self, name, actual, expected):
        super().__init__(
            "{name} referring to incorrect type. Expected {expected}, actual {actual}".format(
                name=name, expected=expected, actual=actual))


class UnexpectedResourceType(FlatdataSyntaxError):
    def __init__(self, name):
        super().__init__(
            "Unexpected resource type: {name}".format(name=name))


class ParsingError(FlatdataSyntaxError):
    def __init__(self, pyparsing_error):
        super().__init__(
            self.create_message(pyparsing_error))

    @staticmethod
    def create_message(err):
        return "Failed to parse the schema. Details below:\n" \
               "  {line}\n" \
               "  {pointer}\n" \
               "  {message}".format(line=err.line, pointer=" " * (err.column - 1) + "^",
                                    message=str(err))


class InvalidWidthError(FlatdataSyntaxError):
    def __init__(self, width, flatdata_type):
        super().__init__(
            "Bit field of {width}bit width cannot fit in {type}".format(width=width,
                                                                        type=flatdata_type))


class InvalidSignError(FlatdataSyntaxError):
    def __init__(self, value):
        super().__init__(
            "Value has wrong sign: {value}".format(value=value))


class DuplicateEnumValueError(FlatdataSyntaxError):
    def __init__(self, enumeration_name, value):
        super().__init__(
            "Enumeration {enumeration_name} has duplicate entries for value {value}"
            .format(enumeration_name=enumeration_name, value=value))

class SparseEnumError(FlatdataSyntaxError):
    def __init__(self, enumeration_name, width):
        super().__init__(
            "Enumeration {enumeration_name} has too many undefined values (2^{width}), please restrict bit width, or define more"
            .format(enumeration_name=enumeration_name, width=width))

class InvalidEnumValueError(FlatdataSyntaxError):
    def __init__(self, enumeration_name, value):
        super().__init__(
            "Enumeration {enumeration_name} has not enough bits for value {value}"
            .format(enumeration_name=enumeration_name, value=value))


class InvalidStructInExplicitReference(FlatdataSyntaxError):
    def __init__(self, struct, resource):
        super().__init__(
            "Struct '{struct}' referenced, but not appearing in resource '{resource}'"
            .format(struct=struct, resource=resource))


class InvalidEnumWidthError(FlatdataSyntaxError):
    def __init__(self, enumeration_name, width, provided_width):
        super().__init__(
            "Enumeration {enumeration_name} has {width} bits, but field specified {provided_width} bits"
            .format(enumeration_name=enumeration_name, width=width, provided_width=provided_width))


class InvalidConstantValueError(FlatdataSyntaxError):
    def __init__(self, name, value):
        super().__init__(
            "Constant {name} has not enough bits for value {value}"
            .format(name=name, value=value))

class InvalidConstReference(FlatdataSyntaxError):
    def __init__(self, name, type):
        super().__init__(
            "Referenced constant {name} has wrong type {type}"
            .format(name=name, type=type))

class InvalidConstValueReference(FlatdataSyntaxError):
    def __init__(self, name, bits):
        super().__init__(
            "Referenced constant {name} value does not fit into {bits} bits"
            .format(name=name, bits=bits))

class DuplicateInvalidValueReference(FlatdataSyntaxError):
    def __init__(self, name, constants):
        super().__init__(
            "Multiple optional annotations {constants} for field {name}"
        .format(name=name, constants=constants))

class InvalidRangeName(FlatdataSyntaxError):
    def __init__(self, name):
        super().__init__(
            "@range name {name} is already in use for a field"
            .format(name=name))

class InvalidRangeReference(FlatdataSyntaxError):
    def __init__(self, name):
        super().__init__(
            "Structs with @range can only be used in vectors: {name}"
            .format(name=name))

class OptionalRange(FlatdataSyntaxError):
    def __init__(self, name):
        super().__init__(
            "@range cannot be combined with @optional, store empty ranges instead: {name}"
            .format(name=name))