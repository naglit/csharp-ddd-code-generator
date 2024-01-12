IMPORT = "@@imp@@"
PHYSICAL_NAME = "@@physc@@"
LOGICAL_NAME = "@@lgc@@"
NAMESPACE = "@@namespace@@"
TYPE = "@@type@@"
TO_TYPE = "@@Type@@"
INIT = "@@init@@"
PROPERTIES = "@@properties@@"

def bind_dto(template:list[str], data:list[dict]) -> list[str]:
    print()


def replace_tags_in_model(model_spec, lines):    
    # dynamically render multiple lines
    spec = model_spec["model_properties"]
    imp = render_import_lines(spec)
    init = render_init_lines(spec)
    properties = render_property_lines(spec)
    lineslen = len(lines)
    
    new_linesss = "".join(list(map(\
        replace_line,\
        make_list(model_spec, lineslen),\
        lines,\
        make_list(imp, lineslen),\
        make_list(init, lineslen),\
        make_list(properties, lineslen))))
    return new_linesss

def replace_template_code(prpty_spec, template_code):
    replace_func = replace_tags_in_model_property if prpty_spec["is_value_object"] == "0" else replace_tags_in_value_obj
    return replace_func(prpty_spec, template_code)

def replace_line(model_spec, line, imp, init, properties):
    new_line = line\
        .replace(IMPORT, imp)\
        .replace(LOGICAL_NAME, model_spec["logical_name"])\
        .replace(PHYSICAL_NAME, model_spec["physical_name"])\
        .replace(NAMESPACE, model_spec["namespace"])\
        .replace(INIT, init)\
        .replace(PROPERTIES, properties)
    return new_line
    
def make_list(item, lineslen):
    return [item for i in range(0, lineslen)]

def retrieve_model_properties_from_model(model_spec):
    return model_spec["model_properties"]
def retrieve_value_obj_from_model_property(model_property_spec):
    return model_property_spec["value_objects"]

def render_property_lines(upper_spec):
    property_lines = []
    for p in upper_spec: # not recursively
        coment = f"///<summary>{p['logical_name']}</summary>"
        property_lines.append(coment)
        property_line = f"public {p['property_type']} {p['property_name']} {{ get; set; }}"
        property_lines.append(property_line)
    return f"\n\t\t".join(property_lines)

def render_init_lines(model_spec):
    init_lines = []
    for p in model_spec: # not recursively
        init_line = f"this.{p['property_name']} = new {p['property_type']}(dto.{p['property_name']});"
        init_lines.append(init_line)
    return f"\n\t\t\t".join(init_lines)

def render_import_lines(model_spec):
    assemblies= find_assemblies_to_be_called(model_spec)
    imports = []
    for asb in assemblies: imports.append(f"using {asb};")
    import_lines = "\n".join(imports)
    return import_lines

def find_assemblies_to_be_called(model_spec):
    assemblies = []
    for p in model_spec: # not recursively
        if p["namespace"] in assemblies: continue
        assemblies.append(p["namespace"])
    return assemblies
    
def replace_tags_in_model_property(model_property_spec, lines):
    new_lines = []
    value_objects = model_property_spec["value_objects"]
    imp = render_import_lines(value_objects)
    init = render_init_lines(value_objects)
    properties = render_property_lines(value_objects)
    for line in lines:
        new_line = line\
            .replace(IMPORT, imp)\
            .replace(LOGICAL_NAME, model_property_spec["logical_name"])\
            .replace(PHYSICAL_NAME, model_property_spec["property_type"])\
            .replace(NAMESPACE, model_property_spec["namespace"])\
            .replace(INIT, init)\
            .replace(PROPERTIES, properties)
        new_lines.append(new_line)
    return new_lines

def replace_tags_in_value_obj(value_obj_spec, lines):
    new_lines = []
    for line in lines:
        new_line = line\
            .replace(PHYSICAL_NAME, value_obj_spec["property_type"])\
            .replace(LOGICAL_NAME, value_obj_spec["logical_name"])\
            .replace(NAMESPACE, value_obj_spec["namespace"])\
            .replace(TYPE, value_obj_spec["primitive_type"])\
            .replace(TO_TYPE, value_obj_spec["primitive_type"].capitalize().replace("?", ""))
        new_lines.append(new_line)
    return new_lines