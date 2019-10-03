import os
class Utilities:
    def __init__(self):
        pass

    def get_main_dir(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path

