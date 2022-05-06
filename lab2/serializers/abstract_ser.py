class Serializer:

    def dump(self, item: any, filename: str):
        file = open(filename, 'w')
        file.write(self.dumps(item))

    def dumps(self, item: any) -> str:
        pass

    def load(self, filename: str):
        file = open(filename, 'r')
        return self.loads(file.read())

    def loads(self, string: str) -> any:
        pass
