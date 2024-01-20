# import service
from pyutil.util import file_query_repository as q_repo
from pyutil.util import file_update_repository as u_repo
from pyutil.util import log_util as log
from code_generation import bind_service, file_repository, template_service
from code_generation import directory_service, config_service
from code_generation.model import Model


def main():
    log.print_with_newline("=== Get it started ===")

    print("Make an output dir")
    directory_service.make_output_root_dir()
    
    print("Create model instances from the config")
    models = config_service.get_models()
    
    print("Make dir structure")
    directory_service.recursively_make_dir(models)
        
    print("Generate a domain model")
    template_service.generate_dtos(models)
    return
    

    generate(spec["domain"], reader.read_model_template, bind_service.replace_tags_in_model, output.write_model)
    
    # Generate model property and value object classes
    print("Generate model property and value object classes")
    generate_model_properties(spec["domain"]["model_properties"])
    return


if __name__ == "__main__":
    main()