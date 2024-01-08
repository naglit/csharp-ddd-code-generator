import os, sys
# import service
from configs import config
from pyutil.util import file_query_repository as q_repo
from pyutil.util import file_update_repository as u_repo


def main():
    design = q_repo.read_json(config.get_class_design_json_path())
    output_path = config.create_output_path()
    u_repo.make_dir(output_path)
    print(output_path)
    return

if __name__ == "__main__":
    main()