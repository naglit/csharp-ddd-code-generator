import os, sys
import utility.file_repository as fc

MODEL_CLASS = 0
MODEL_PROPERTY_CLASS = 1
VALUE_OBJECT_CLASS = 2
TEMPLATES_MAP = {
        MODEL_CLASS: "template-model.cs",
        MODEL_PROPERTY_CLASS: "template-model_property.cs",
        VALUE_OBJECT_CLASS: "template-valueobject.cs",
    }

def read_model_template():
    return read_template(TEMPLATES_MAP[MODEL_CLASS])

def get_template_code(prpty_spec):
    template = TEMPLATES_MAP[MODEL_PROPERTY_CLASS] if prpty_spec["is_value_object"] == "0" else TEMPLATES_MAP[VALUE_OBJECT_CLASS]
    return read_template(template)

def read_template(file_name):
    template_path = os.path.join(sys.path[0], "template", file_name)
    replaced_code = fc.read_file(template_path)
    return replaced_code