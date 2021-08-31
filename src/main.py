import argparse
import sys
from logger import Logger
from cf_parse import parse_policy


def main():
    args = parse_arguments()

    logger = Logger()
    logger.set_debug(args.debug)
    logger.set_inform(not args.quiet)

    reformatted = 0
    exit_code = 0
    for filename in args.file:
        file = open(filename)
        in_data = file.read()
        out_data = parse_policy(in_data)

        if args.check:
            if in_data != out_data:
                reformatted += 1
                exit_code = 1
                logger.log_inform("Would reformat '%s'" % filename)
            continue

        if args.print:
            print(out_data)
            continue

        if args.confirm:
            if input("Reformat %s? [Y/n]:" % filename) not in ("Y", "y"):
                continue

        if in_data != out_data:
            reformatted += 1
            logger.log_inform("Reformatted '%s'" % filename)
            # TODO: write output to file

    logger.log_inform("%d file(s) %sreformatted" % (reformatted, "would be " if args.check else ""))

    sys.exit(exit_code)


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
