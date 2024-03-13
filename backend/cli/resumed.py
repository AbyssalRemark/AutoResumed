import subprocess
import json
import os
import tempfile


def to_html(resume: dict, template: str, keep_html_file: bool = False) -> str:
    """
    Converts the given resume to HTML
    """
    tmp_dir = tempfile.gettempdir()

    input_file_path = os.path.join(tmp_dir, "resume.json")
    output_file_path = os.path.join(tmp_dir, "resume.html")

    # Dump dictionary to /tmp/resume.json
    with open(input_file_path, "w") as json_file:
        json.dump(resume, json_file)

    # Generate resume.html
    process = subprocess.run(
        [
            "npx",
            "resumed",
            "render",
            input_file_path,
            "-o",
            output_file_path,
            "-t",
            template,
        ],
        capture_output=True,
        text=True,
    )

    if "Could not load theme" in process.stderr:
        raise InvalidTemplate

    # We no longer need resume.json
    os.remove(input_file_path)

    with open(output_file_path, "r") as html_file:
        contents = html_file.read()

    # We no longer need resume.html
    if not keep_html_file:
        os.remove(output_file_path)

    return contents

class InvalidTemplate(Exception):
    pass
