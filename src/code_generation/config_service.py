from code_generation.model import Model
from pyutil.util import file_query_repository  as q_repo
from configs import config

def get_models():
    models = [Model(x) for x in q_repo.read_json(config.get_class_design_json_path())["models"]]
    return models
