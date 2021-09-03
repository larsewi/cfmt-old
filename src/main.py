import argparse
from pretty_printer import PrettyPrinter
from logger import Logger
from cf_lex import lexer


def main():
    args = parse_arguments()

    logger = Logger()
    logger.set_debug(args.debug)
    logger.set_inform(not args.quiet)

    for filename in args.file:
        file = open(filename)
        data = file.read()
        lexer.input(data)
        pretty = PrettyPrinter(lexer)
        print(pretty)

def parse_arguments():
    arg_parser = argparse.ArgumentParser(
        description="Simple CFEngine policy formatting tool",
        epilog="Jeez Louise ...",
    )
    arg_parser.add_argument(
        "-d", "--debug", help="enable debug messages", action="store_true"
    )
    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument(
        "-q", "--quiet", help="don't emit non error messages", action="store_true"
    )
    group.add_argument(
        "-r",
        "--confirm",
        help="request confirmation before formatting a file", action="store_true"
    )
    arg_parser.add_argument(
        "-c", "--check", help="check if files need formatting", action="store_true"
    )
    arg_parser.add_argument(
        "-p",
        "--print",
        help="write formatted file to standard output", action="store_true"
    )
    arg_parser.add_argument("file", help="path to input files", type=str, nargs="*")
    return arg_parser.parse_args()


if __name__ == "__main__":
    main()
