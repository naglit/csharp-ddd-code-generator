from pyutil.util import log_util as log
from code_generation.model import Model

PROPERTIES = "properties"

def get_class_structure(models: list[Model]):
    for model in models:
        # Recursive
        if model.has_properties():
            log.print_with_newline("# class_name: " + model.get_physical_name())
            # directory_name = os.path.join(base_path, class_name)
            # os.makedirs(directory_name, exist_ok=True)

            get_class_structure(model.get_properties())
            # for property_data in properties:
            #     print("prop")
            #     print(property_data)
                
        else:
            log.print_with_newline("value_model: "+ model.get_physical_name())
            continue

