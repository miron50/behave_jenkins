#!/usr/bin/python3

import argparse
import dump


def main():
    parser = argparse.ArgumentParser(prog='BDD_Task',
        description="""This is a script, that dumps all data,
that is available on TCP socket, untill server closes it's socket.
All data is read in chunks and written to output file""")
    parser.add_argument('-a', '--address',
                        help='Server address. Default is %s' % dump.DEFAULT_ADDRESS, type=str, default=dump.DEFAULT_ADDRESS)
    parser.add_argument('-p', '--port',
                        help='Server port to connect to and perform dump. Default is %d' % dump.DEFAULT_PORT, type=int, default=dump.DEFAULT_PORT)
    parser.add_argument('-o', '--output',
        required=True, help='Output file path', type=argparse.FileType('wb'))

    options = parser.parse_args()
    dump.from_port_to_file(options.address, options.port, options.output)


if __name__=='__main__':
    main()