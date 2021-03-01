from flatdata.generator.engine import Engine
from common import DictResourceStorage, INSTANCE_TEST_SCHEMA, RESOURCE_PAYLOAD, ARCHIVE_SIGNATURE_PAYLOAD


def test_create_empty_archive():
    module = Engine(INSTANCE_TEST_SCHEMA).render_python_module()
    dict_storage = DictResourceStorage()
    builder = module.backward_compatibility_ArchiveBuilder(dict_storage)
    # is setting some dict fine for setting a struture, or
    # should we require it to be the specific class?
    #builder.set("resource", {"a": 0, "b": 0, "c": 0, "d": 0})

    # do we need something like a finish/close method?
    # if we do, should we try to make it work with python's
    # `with ... as archive_builder:` syntax?
    #builder.finish()
    class dummy:
        def __init__(self):
            self.a = -0x1
            self.b=0x01234567
            self.c=-0x28
            self.d=0

    builder.set_resource(dummy())
