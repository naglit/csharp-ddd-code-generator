from pyutil.util.file_query_repository import get_current_dir, path_join
from pyutil.util import datetime_util as du

def get_class_design_json_path():
    return path_join(get_current_dir(), "configs", "class_design.json")

def create_output_path():
    return path_join(get_current_dir(), "outputs", du.get_now())
