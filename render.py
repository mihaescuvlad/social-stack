import yaml, os, shutil
from jinja2 import Environment, FileSystemLoader, StrictUndefined

with open("config.yaml") as f:
    context = yaml.safe_load(f)

env = Environment(
    loader=FileSystemLoader("templates"),
    undefined=StrictUndefined
)

files = {
    "index.html.jinja": "index.html",
    "styles.css.jinja": "styles.css",
    "main.js.jinja": "main.js"
}

os.makedirs("renders", exist_ok=True)
shutil.copytree("assets", "renders/assets", dirs_exist_ok=True)
for template_name, output_name in files.items():
    template = env.get_template(template_name)
    rendered = template.render(**context)

    output_path = os.path.join("renders", output_name)
    with open(output_path, "w") as f:
        f.write(rendered)
