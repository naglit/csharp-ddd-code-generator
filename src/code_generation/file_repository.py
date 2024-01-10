import os, re, time, sys
from pyutil.util import file_query_repository as q_repo
from pyutil.util import file_update_repository as u_repo

unique_output_dir = ""

# Write a domain model
def write_model(model_spec ,new_code): 
    return write_class(model_spec["physical_name"], new_code)

# Write either a model property or a value object
def write_property(spec_property, new_code):
        make_subdirectories(spec_property)
        path_from_root = os.path.join(get_sub_dir(spec_property["namespace"]), spec_property["property_type"])
        return write_class(path_from_root, new_code)

# Write
def write_class(file_path_from_root, new_code):
    replaced_code = u_repo.write_file(os.path.join(unique_output_dir, file_path_from_root), new_code)
    return replaced_code

# Make dir
def make_subdirectories(property_spec):
    sub_dir = get_sub_dir(property_spec["namespace"])
    new_dir = os.path.join(unique_output_dir, sub_dir)
    u_repo.make_dir(new_dir)

def get_sub_dir(namespace):
    regex_pattern = r"^(?:[a-zA-Z0-9]+)\.(?:[a-zA-Z0-9]+\.){3}([a-zA-Z0-9\.]+)"
    dir_structure_regex = re.compile(regex_pattern)
    match = dir_structure_regex.search(namespace)
    sub_dir_path = match.group(1).replace(".", "\\") if match is not None else ""
    # dir_structure = match.group(1).split(".") if match is not None else []
    return sub_dir_path


