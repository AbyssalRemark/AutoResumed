import subprocess
import json
import os


def to_html(resume: dict, template: str, keep_html_file: bool = False) -> str:
    """
    Converts the given resume to HTML
    """
    cwd = os.getcwd()

    input_file_path = os.path.join(cwd, "resume.json")
    output_file_path = os.path.join(cwd, "resume.html")

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
            "jsonresume-theme-" + template,
        ],
        capture_output=True,
        text=True,
    )

    stderr = process.stderr
    if stderr:
        if "Could not load theme" in stderr:
            raise InvalidTemplate
        else:
            print(stderr)

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
