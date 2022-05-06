import argparse


class ArgParser:
    @staticmethod
    def parse_arguments():
        argument_parser = argparse.ArgumentParser(description="Simple console util ")
        argument_parser.add_argument('-l', '--load', dest='load', nargs='+', help='load object from file')
        argument_parser.add_argument('-d', '--dump', dest='dump', nargs='+', help='dump object to file')
        argument_parser.add_argument('-c', '--convert', dest='convert', nargs='?', default=None, help='json,yaml,toml')
        return argument_parser.parse_args()

    @staticmethod
    def get_arguments():
        arguments = ArgParser.parse_arguments()
        if arguments.convert is not None:
            return arguments.dump, arguments.load

    @staticmethod
    def dump_to() -> list[str]:
        arguments = ArgParser.parse_arguments()
        return arguments.dump

    @staticmethod
    def load_from() -> list[str]:
        arguments = ArgParser.parse_arguments()
        return arguments.load
