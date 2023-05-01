from os.path import abspath
from os import listdir
import re
ABS_PATH = abspath("certs")


def get_files_to_copy():
    f = [f for f in listdir(ABS_PATH) if re.match(r'.*\.txt', f)]
    return [ABS_PATH+'\\'+ f for f in f ]
