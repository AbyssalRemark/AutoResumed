import subprocess
import json
import os
import tempfile

def convert(resume: dict):
    """
    Converts the given resume to HTML
    """
    tmp_dir = tempfile.gettempdir()
    json_file_path = os.path.join(tmp_dir, "resume.json")

    with open(json_file_path, "w") as json_file:
        json.dump(resume, json_file)

    subprocess.run(["resumed", "render", json_file_path])
