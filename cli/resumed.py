import subprocess
import json
import os
import tempfile

def convert(resume: dict) -> str:
    """
    Converts the given resume to HTML
    """
    tmp_dir = tempfile.gettempdir()
    input_file_path = os.path.join(tmp_dir, "resume.json")

    with open(input_file_path, "w") as json_file:
        json.dump(resume, json_file)

    subprocess.run(["resumed", "render", input_file_path])

    # We no longer need resume.json
    os.remove(input_file_path)

    output_file_path = os.path.join(tmp_dir, "resume.html")

    with open(output_file_path, "r") as html_file:
        contents =  html_file.read()

    # We no longer need resume.html
    os.remove(output_file_path)

    return contents

def test():
    tmp_dir = tempfile.gettempdir()
    path = os.path.join(tmp_dir, "resume.json")
    subprocess.run(["resumed", "init", path])

    with open(path, "r") as file:
        contents = file.read()

    print(convert(json.loads(contents)))
