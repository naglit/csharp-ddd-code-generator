from pyutil.util import file_query_repository as q_repo
import code_generation.bind_service as tr
from code_generation.model import Model
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

def generate_dto_classes(parent_path: str, models: list[Model]):
    for model in models:
        if model.has_properties() == False:
            log.print_with_newline("value_model: "+ model.get_physical_name())
            continue

        path = q_repo.append_path(parent_path, model.get_physical_name())
        log.print_with_newline("# path: " + path)
        u_repo.make_dir(path)
        recursively_make_dir(path, model.get_properties())

    template = read_dto_template()
    tr.bind_dto() ## this is function

def read_dto_template() -> Template:
    return __read_template(TEMPLATES_MAP[DTO_CLASS])

def read_model_template() -> Template:
    return __read_template(TEMPLATES_MAP[MODEL_CLASS])

# def read_model_template():
#     return read_template(TEMPLATES_MAP[MODEL_PROPERTY_CLASS])

# def read_model_template():
#     return read_template(TEMPLATES_MAP[VALUE_OBJECT_CLASS])

def get_template_code(prpty_spec):
    template = TEMPLATES_MAP[MODEL_PROPERTY_CLASS] if prpty_spec["is_value_object"] == "0" else TEMPLATES_MAP[VALUE_OBJECT_CLASS]
    return __read_template(template)

def __read_template(file_name) -> Template:
    template_path = q_repo.append_path_to_current_dir("templates", file_name)
    template = Template(q_repo.read_file(template_path))
    return template