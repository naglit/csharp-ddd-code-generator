from pyutil.util import file_query_repository as q_repo
from pyutil.util import file_update_repository as u_repo
import code_generation.bind_service as tr
from code_generation.dto import Dto
from code_generation.template import Template
from pyutil.util import log_util as log

DTO_CLASS = 0
MODEL_CLASS = 1
MODEL_PROPERTY_CLASS = 2
VALUE_OBJECT_CLASS = 3
TEMPLATES_MAP = {
        DTO_CLASS: "template-dto.cs",
        MODEL_CLASS: "template-model.cs",
        MODEL_PROPERTY_CLASS: "template-model_property.cs",
        VALUE_OBJECT_CLASS: "template-valueobject.cs",
    }

def generate_dtos(models: list[Dto]) -> None:
    for model in models: generate_dto(model)

def generate_dto(dto: Dto):
    lines = __read_dto_template().bind_properties(dto)
    u_repo.write_file(dto.filepath, lines)

def __read_dto_template() -> Template:
    return __read_template(TEMPLATES_MAP[DTO_CLASS])

def __read_model_template() -> Template:
    return __read_template(TEMPLATES_MAP[MODEL_CLASS])

# def read_model_template():
#     return read_template(TEMPLATES_MAP[MODEL_PROPERTY_CLASS])

# def read_model_template():
#     return read_template(TEMPLATES_MAP[VALUE_OBJECT_CLASS])

def __get_template_code(prpty_spec):
    template = TEMPLATES_MAP[MODEL_PROPERTY_CLASS] if prpty_spec["is_value_object"] == "0" else TEMPLATES_MAP[VALUE_OBJECT_CLASS]
    return __read_template(template)

def __read_template(file_name) -> Template:
    template_path = q_repo.append_path_to_current_dir("templates", file_name)
    template = Template(q_repo.read_file(template_path))
    return template