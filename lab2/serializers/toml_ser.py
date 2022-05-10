import toml
from serializers.abstract_ser import Serializer
from serializers import packer


class TOMLSerializer(Serializer):

    def dumps(self, obj):
        return toml.dumps(packer.pack(obj))

    def loads(self, path):
        return packer.unpack(toml.loads(path))
