# coding=utf-8

from time import strftime


def create_log_filename(filename):
    return filename + "_" + strftime("%Y%m%d%H%M%S") + ".log"
