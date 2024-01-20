
from configs import config
from pyutil.util import log_util as log
from code_generation.model import Model
from pyutil.util import file_query_repository  as q_repo
from pyutil.util import file_update_repository  as u_repo

PROPERTIES = "properties"

def recursively_make_dir(models: list[Model]):
    recursively_make_dir(config.create_output_path(), models)
    
def recursively_make_dir(parent_path: str, models: list[Model]):
    for model in models:
        if model.has_properties() == False: continue

        path = q_repo.append_path(parent_path, model.get_physical_name())
        log.print_with_newline("# path: " + path)
        u_repo.make_dir(path)
        recursively_make_dir(path, model.get_properties())
        
def make_output_root_dir():
    output_path = config.create_output_path()
    u_repo.make_dir(output_path)