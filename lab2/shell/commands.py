from shell.argparse import ArgParser
from serializers.factory import *


def get_creator(filename: str) -> (SerializerCreator, None):
    filetype = filename.lower().split('.')[-1]
    creators = {
        'json': JSONSerializerCreator,
        'yaml': YAMLSerializerCreator,
        'toml': TOMLSerializerCreator
    }
    return creators.get(filetype, None)


def dump(obj, filename: str) -> any:
    creator = get_creator(filename)
    if creator is None:
        return None
    serialz = creator().create_serializer()
    serialz.dump(obj, filename)
    obj = serialz.load(filename)
    print('Object dumped successfully')
    return obj


def load(filename: str) -> any:
    creator = get_creator(filename)
    if creator is None:
        return None
    serialz = creator().create_serializer()
    item = serialz.load(filename)

    print('Object loaded')
    return item


dump_to, load_from = ArgParser.get_arguments()


def convert_one_to_another():
    global obj
    if load_from is not None:
        obj = load(''.join(load_from))

    if dump_to is not None:
        dump(obj, ''.join(dump_to))
