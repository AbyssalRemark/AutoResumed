import subprocess
import json
import os
import tempfile


def to_html(resume: dict, template: str) -> str:
    """
    Converts the given resume to HTML
    """
    tmp_dir = tempfile.gettempdir()

    input_file_path = os.path.join(tmp_dir, "resume.json")
    output_file_path = os.path.join(tmp_dir, "resume.html")

    # Dump dictionary to /tmp/resume.json
    with open(input_file_path, "w") as json_file:
        print(json_file)
        json.dump(resume, json_file)

    # Generate resume.html
    subprocess.run(
        [
            "npx",
            "resumed",
            "render",
            input_file_path,
            "-o",
            output_file_path,
            "-t",
            template,
        ]
    )

    # We no longer need resume.json
    os.remove(input_file_path)

    with open(output_file_path, "r") as html_file:
        contents = html_file.read()

    # We no longer need resume.html
    os.remove(output_file_path)

    return contents
