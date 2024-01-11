# import service
from configs import config
from pyutil.util import file_query_repository as q_repo
from pyutil.util import file_update_repository as u_repo
from pyutil.util import log_util as log
from code_generation import bind_service, file_repository, template_service

def get_class(models: list[dict]):
    for model in models:
        if "properties" in model:
            class_name = model.get("physical_name", "UnnamedClass")
            log.print_with_newline("# class_name: " + class_name)
            # directory_name = os.path.join(base_path, class_name)
            # os.makedirs(directory_name, exist_ok=True)

            properties = model.get("properties", [])
            get_class(properties)
            # for property_data in properties:
            #     print("prop")
            #     print(property_data)
                
        else:
            log.print_with_newline("value_model: "+ model["physical_name"])
            continue

def main():
    log.print_with_newline("=== Get it started ===")

    # make an output dir
    output_path = config.create_output_path()
    u_repo.make_dir(output_path)
    models = q_repo.read_json(config.get_class_design_json_path())["models"]
    
    get_class(models)
        
    
    
    return 
    print("Generate a domain model")
    # read the class design
    models = q_repo.read_json(config.get_class_design_json_path())
    models = models["models"]
    template_service.generate_dto_classes(models)
    
    return
    

    generate(spec["domain"], reader.read_model_template, bind_service.replace_tags_in_model, output.write_model)
    
    # Generate model property and value object classes
    print("Generate model property and value object classes")
    generate_model_properties(spec["domain"]["model_properties"])
    return


if __name__ == "__main__":
    main()