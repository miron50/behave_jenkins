import subprocess
import datetime
import sys
import os
from pathlib import Path

import __main__

from behave import *

args =[]


@given("Type '{serv_addr}' as Server Address")
def step_impl(context, serv_addr):
    context.serv_addr = str(serv_addr)
    args.append("-a")
    args.append(str(serv_addr))


@given("Type '{serv_port}' as Server Port")
def step_impl(context, serv_port):
    context.serv_port = str(serv_port)
    args.append("-p")
    args.append(str(serv_port))


@given("Type '{Path_to_output_file}' as output file")
def step_impl(context, Path_to_output_file):
    context.PATH = Path_to_output_file
    args.append("-o")
    args.append(str(Path_to_output_file))


@when("Launch client")
def step_impl(context):
    server_address = ""
    try:
        server_address = " -a " + context.serv_addr
    except:
        pass

    server_port = ""
    try:
        server_port = " -p " + context.serv_port
    except:
        pass

    path_to_file = ""
    try:
        path_to_file = " -o \"" + context.PATH + "\""
    except:
        pass
    launch_str = "python __main__.py" + server_address + server_port + path_to_file

    try:
        context.proc = subprocess.Popen(launch_str, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, universal_newlines=True)
        context.lines = []
        for line in context.proc.stdout:
            context.lines.append(line)
        context.proc.wait()
    except Exception as e:
        context.ex = e


@then("Output file exists with information")
def step_impl(context):
    with open(context.PATH, "r") as out_file:
        lines = out_file.readlines()
        for line in lines:
           assert line.startswith(datetime.datetime.today().strftime("%Y-%m-%d")), \
                "File contains current date %s" % datetime.datetime.today().strftime("%Y-%m-%d")


@then("Connect with '{ErrorCode}'")
def step_impl(context, ErrorCode):
    if __name__ == '__main__':
        assert context.ex.find(str(ErrorCode)) == -1, context.ex
