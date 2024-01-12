# import service
from configs import config
from pyutil.util import file_query_repository as q_repo
from pyutil.util import file_update_repository as u_repo
from pyutil.util import log_util as log
from code_generation import bind_service, file_repository, template_service

def main():
    log.print_with_newline("=== Get it started ===")

    # make an output dir
    output_path = config.create_output_path()
    u_repo.make_dir(output_path)
    models = q_repo.read_json(config.get_class_design_json_path())["models"]
    
    get_class_structure(models)
        
    
    
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