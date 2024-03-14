import subprocess
import json
import os
import tempfile
import string
import random


def to_html(resume: dict, template: str) -> str:
    """
    Converts the given resume to HTML and returns the name of the resume
    """
    tmp_dir = tempfile.gettempdir()

    resume_name = f"resume-{generate_random_string()}"

    input_file_path = os.path.join(tmp_dir, "resume.json")
    output_file_path = os.path.join("/var/www/html/html-resumes", resume_name + ".html")
    print(output_file_path)

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

    if process.stderr:
        if "Could not load theme" in process.stderr:
            raise InvalidTemplate
        else:
            print(process.stderr)

    # We no longer need resume.json
    os.remove(input_file_path)

    return resume_name

def generate_random_string():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(12))

class InvalidTemplate(Exception):
    pass
