#!/usr/bin/python3

import argparse
import os

ignored_extensions = ["csv", "zip", "rar", "xlsx"]

parser = argparse.ArgumentParser(
                    prog="fixnewlines",
                    description="Adds a newline to files that do not have one")

parser.add_argument('dir', default="./")
parser.add_argument('-r', '--recursive', action="store_false", default=True)

os.chdir(parser.parse_args().dir)


def get_filelist(path_to_dir):
    filelist = []

    for file in os.listdir(path_to_dir):
        if os.path.isfile(path_to_dir + file):
            filelist.append(path_to_dir + file)

    return filelist


def get_dirlist(path_to_dir):
    dirlist = []
    for dir in os.listdir(path_to_dir):
        if os.path.isdir(path_to_dir + dir):
            dirlist.append(path_to_dir + dir)

    return dirlist


def has_trailing_newlines(path_to_file):
    if (path_to_file.split('.')[1] in ignored_extensions):
        print(f"found ignored file extension {path_to_file.split('.')[1]}")
        return False
    with open(path_to_file, 'r') as f:
        lines = f.read()
        last_line_has_newline = lines[-1] == '\n'
        second_to_last_line_has_newline = lines[-2] == '\n'
        has_trailing = last_line_has_newline and second_to_last_line_has_newline
        try:
            return has_trailing
        except IndexError:
            return False


def starts_with_newline(path_to_file):
    with open(path_to_file, 'r') as f:
        lines = f.readlines()
        return lines[0] == '\n'


def add_newline(path_to_file):
    if (path_to_file.split('.')[1] in ignored_extensions):
        print("found ignored file extension")
    else:
        with open(path_to_file, 'a') as f:
            f.writelines('\n')
        f.close()


def has_no_newline(path_to_file):
    if (path_to_file.split('.')[1] in ignored_extensions):
        print(f"found ignored file extension {path_to_file.split('.')[1]}")
        return True
    with open(path_to_file, 'r') as f:
        lines = f.read()
        has_no_newline = lines[-1] != '\n' and lines[-1] != ' '
        try:
            return has_no_newline
        except IndexError:
            return False


def has_whitespace(path_to_file):
    if (path_to_file.split('.')[1] in ignored_extensions):
        print(f"found ignored file extension {path_to_file.split('.')[1]}")
        return True
    with open(path_to_file, 'r') as f:
        lines = f.read()
        has_whitespace = lines[-1] == ' ' and lines[-1] != '\n'
        try:
            return has_whitespace
        except IndexError:
            return False


def remove_first_char(path_to_file):
    if (path_to_file.split('.')[1] in ignored_extensions):
        print("found ignored file extension")
    else:
        with open(path_to_file, 'r', newline='') as f:
            contents = f.read()
            f.close()
            strlist = list(contents)
            strlist[0] = ""
            result_string = ''.join(strlist)
        with open(path_to_file, 'w', newline='') as f:
            f.write(result_string)


def remove_last_char(path_to_file):
    if (path_to_file.split('.')[1] in ignored_extensions):
        print("found ignored file extension")
    else:
        with open(path_to_file, 'r', newline='') as f:
            contents = f.read()
            f.close()
            strlist = list(contents)
            strlist[-1] = ""
            result_string = ''.join(strlist)
        with open(path_to_file, 'w', newline='') as f:
            f.write(result_string)


def iterate(path_to_dir):
    for file in get_filelist(path_to_dir):
        try:
            if starts_with_newline(file):
                remove_first_char(file)
            if has_no_newline(file):
                add_newline(file)
            elif has_whitespace(file):
                remove_last_char(file)
            elif has_trailing_newlines(file):
                remove_last_char(file)
        except Exception as e:
            print(f"Failed on file {file}. Traceback: \n{e}")
    for dir in get_dirlist(path_to_dir):
        iterate(dir + '/')


iterate(os.path.abspath(parser.parse_args().dir) + '/')
