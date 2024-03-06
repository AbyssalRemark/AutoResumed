import subprocess
import json
import os
import tempfile

def convert(resume: dict, theme: str) -> str:
    """
    Converts the given resume to HTML
    """
    tmp_dir = tempfile.gettempdir()
    input_file_path = os.path.join(tmp_dir, "resume.json")
    output_file_path = os.path.join(tmp_dir, "resume.html")

    with open(input_file_path, "w") as json_file:
        json.dump(resume, json_file)

    subprocess.run(["npx", "resumed", "render", input_file_path, "-t", theme, "-o", output_file_path])

    # We no longer need resume.json
    os.remove(input_file_path)


    with open(output_file_path, "r") as html_file:
        contents =  html_file.read()

    # We no longer need resume.html
    os.remove(output_file_path)

    return contents

def test():
    tmp_dir = tempfile.gettempdir()
    path = os.path.join(tmp_dir, "resume.json")
    subprocess.run(["npx", "resumed", "init", path])

    with open(path, "r") as file:
        contents = file.read()

    print(convert(json.loads(contents), "jsonresume-theme-even"))

if __name__ == "__main__":
    test()
