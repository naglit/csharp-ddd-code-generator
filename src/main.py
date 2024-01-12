# import service
from configs import config
from pyutil.util import file_query_repository as q_repo
from pyutil.util import file_update_repository as u_repo
from pyutil.util import log_util as log
from code_generation import bind_service, file_repository, template_service
from code_generation import directory_service
from code_generation.model import Model
from code_generation.template import Template

def main():
    log.print_with_newline("=== Get it started ===")

    # make an output dir
    output_path = config.create_output_path()
    u_repo.make_dir(output_path)
    models = [Model(x) for x in q_repo.read_json(config.get_class_design_json_path())["models"]]
    directory_service.recursively_make_dir(output_path, models)
        
    print("Generate a domain model")
    dto_template = Template(template_service.read_dto_template())
    template_service.generate_dto_classes(dto_template, models)
    return
    

    generate(spec["domain"], reader.read_model_template, bind_service.replace_tags_in_model, output.write_model)
    
    # Generate model property and value object classes
    print("Generate model property and value object classes")
    generate_model_properties(spec["domain"]["model_properties"])
    return


if __name__ == "__main__":
    main()