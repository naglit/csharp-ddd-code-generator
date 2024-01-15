from pyutil.util import specification as sp
from pyutil.util import file_query_repository as q_repo
from code_generation import bind_service, file_repository, template_service
from configs import config

def generate_classes():
    print("=== Get it started ===")
    design = q_repo.read_json(config.get_class_design_json_path())
    output_path = config.create_output_path()
    return

    # Generate domain model
    print("Generate a domain model")
    generate(spec["domain"], template_service.__read_model_template, bind_service.replace_tags_in_model, output.write_model)
    
    # Generate model property and value object classes
    print("Generate model property and value object classes")
    generate_model_properties(spec["domain"]["model_properties"])

# Generate a domain mode. This could be, however, used for another type of class generaion
def generate(spec, read, replace, write):
    # read
    replaced_code = read()

    # replace
    new_code = replace(spec, replaced_code)

    # write
    write(spec, new_code)

# generate_model_properties
def generate_model_properties(properties_spec):
    # read
    template_codes = list(map(template_service.__get_template_code, properties_spec))

    # replace
    new_codes = list(map(bind_service.replace_template_code, properties_spec, template_codes))

    # write
    results = list(map(output.write_property, properties_spec, new_codes))
    
    # recurse
    for p in properties_spec: recursively_create_properties(p)

# Recursively generate classes like model properties or value objects
def recursively_create_properties(prpty_spec):
    if ("value_objects" in prpty_spec): generate_model_properties(prpty_spec["value_objects"])