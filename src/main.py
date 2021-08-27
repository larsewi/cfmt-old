import argparse
import cf_parse


def main():
    config = parse_arguments()

    for filename in config.file:
        file = open(filename)
        contents = file.read()
        prog = cf_parse.parse(contents)
        print(prog)


def parse_arguments():
    arg_parser = argparse.ArgumentParser(
        description="Simple CFEngine policy formatting tool",
        epilog="Jeez Louise ...",
    )
    arg_parser.add_argument(
        "-d",
        "--debug",
        choices=["lexer", "parser", "printer"],
        help="enable different debug modes (intended for developers)",
    )
    arg_parser.add_argument("file", help="path to input files", type=str, nargs="*")
    return arg_parser.parse_args()


if __name__ == "__main__":
    main()
