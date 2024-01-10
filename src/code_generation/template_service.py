from pyutil.util import file_query_repository as q_repo
import code_generation.tag_replacement_service as tr

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

def generate_dto_classes(dto_designs: list[dict]):
    dto_template = read_dto_template()
    tr.generate_dto_classes()

def read_dto_template():
    return __read_template(TEMPLATES_MAP[DTO_CLASS])

def read_model_template():
    return __read_template(TEMPLATES_MAP[MODEL_CLASS])

# def read_model_template():
#     return read_template(TEMPLATES_MAP[MODEL_PROPERTY_CLASS])

# def read_model_template():
#     return read_template(TEMPLATES_MAP[VALUE_OBJECT_CLASS])

def get_template_code(prpty_spec):
    template = TEMPLATES_MAP[MODEL_PROPERTY_CLASS] if prpty_spec["is_value_object"] == "0" else TEMPLATES_MAP[VALUE_OBJECT_CLASS]
    return __read_template(template)

def __read_template(file_name):
    template_path = q_repo.append_path_to_current_dir("templates", file_name)
    replaced_code = q_repo.read_file(template_path)
    return replaced_code