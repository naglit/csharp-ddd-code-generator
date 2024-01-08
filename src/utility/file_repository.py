import sys, os, json

def read_file(file_path):
    with open(file_path, encoding="utf-8") as fin:
        lines = []
        for line in fin.readlines():
            lines.append(line.replace("\r\n", "\n"))
        return lines
    
def read_json(json_arg = None):
    json_name = "spec.json" if json_arg == None else json_arg
    
    json_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", json_name)
    print(json_path)
    return
    with open(json_path, 'r',encoding="utf-8") as f:
        config = json.load(f)
        return config
    
def write_file(file_name, lines):
    file_path = file_name + ".cs"
    data = "".join(lines)
    if "-d" in sys.argv:
        print("\nDEBUG MODE:")
        print(data)
        return

    with open(file_path, "w", encoding="utf-8") as fout:
        print(f"Create {file_path}")        
        fout.write(data)

def make_dir(dir_path):
    if "-d" not in sys.argv:
        if not os.path.isdir(dir_path): os.makedirs(dir_path)
    else:
        print("\nDEBUG MODE:")
        print(dir_path)

