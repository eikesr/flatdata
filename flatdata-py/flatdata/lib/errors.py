"""
 Copyright (c) 2017 HERE Europe B.V.
 See the LICENSE file in the root of this project for license details.
"""

import difflib


class SchemaMismatchError(RuntimeError):
    """
    Schema mismatch: archive does not match software expectations.
    """

    def __init__(self, name, expected_schema, actual_schema):
        diff = '\n'.join([l for l in difflib.unified_diff(expected_schema, actual_schema)])
        message = "Schema mismatch for resource {name}. Expected: \n{expected}\n\nActual:{actual}\n\nDiff:{diff}"
        RuntimeError.__init__(self,
                              message.format(name=name,
                                             expected=expected_schema,
                                             actual=actual_schema, diff=diff))


class CorruptArchiveError(RuntimeError):
    """
    Corrupt archive error: missing resource files or schemas, incorrect archive signature etc.
    """


class CorruptResourceError(CorruptArchiveError):
    """
    Resource is corrupt and cannot be opened.
    """


class MissingResourceError(KeyError, CorruptArchiveError):
    """
    Resource or schema is missing.
    """
    def __init__(self, key):
        super().__init__("Resource {key} not found".format(key=key))


class ResourceReadOnlyError(RuntimeError):
    """
    Resource is read only and cannot be written to.
    """


class MissingFieldError(RuntimeError):
    def __init__(self, key, name):
        super().__init__(f'Missing "{key}" is required for "{name}"')


class UnknownFieldError(RuntimeError):
    def __init__(self, key, name):
        super().__init__(f'Field "{key}" is not specified for "{name}"')

class FileExistsError(RuntimeError):
    def __init__(self, key):
        super().__init__(f'File "{key}" exists already')

class DirExistsError(RuntimeError):
    def __init__(self, path):
        super().__init__(f'Directory "{path}" exists already')

class UnknownStructureError(RuntimeError):
    def __init__(self, name):
        super().__init__(f'"{name}" structure is not part of the multivector')

class IndexWriterError(RuntimeError):
    def __init__(self, error_str="Error initializing IndexWritter Class"):
        super().__init__(f'{error_str}')

class ArchivePathNotProvidedError(RuntimeError):
    def __init__(self):
        super().__init__("File path is not provided")

class MissingResourceName(RuntimeError):
    def __init__(self):
        super().__init__("Resource name is not provided")

class FileNameNotProvided(RuntimeError):
    def __init__(self):
        super().__init__("File name is not provided")

class ResourceAlreadySetError(RuntimeError):
    def __init__(self):
        super().__init__("Resource is already set")

class UnknownResourceError(RuntimeError):
    def __init__(self, name):
        super().__init__(f"Resource {name} is not part of provided schema")
