# Social Stack

---

Fast and aesthetic open-source social links index page
* Easily configurable using a single YAML file that holds all build options
* Can be built, dockerized and deployed to GitHub Pages with CI/CD Actions, just fork the repository and modify the configs
* Few dependencies for building
* Builds into a static HTML page

## Index
* [Configuring](#configuring)
* [Building](#building)
    * [GitHub Actions](#github-actions)
    * [Docker](#docker)

## Configuring
Tweak `config.yaml` to customize your social stack, from adding or removing links to enabling or disabling animations.

Assets must be stored in `assets/`, and they should be referenced by their file name, i.e., if there exists a file `assets/profile.png` then it can be referenced using `profile.png`.

You should feel free to modify the templates and add more configuration options if the defaults don't meet your expectations.

## Building
### GitHub Actions
You can have GitHub build the project for you, publish Docker images, and/or deploy the project to GitHub Pages.

Instructions:
1. Fork the repository
2. Enable GitHub Actions
3. Enable deployment to GitHub Pages from actions (if needed)
4. Make [configuring](#configuring) changes as needed
5. Push the changes to `main`. The commit message must include a [semver](https://semver.org/) string. You must also update the CHANGELOG.
For example run:
```bash
VERSION='v2.0.0' MESSAGE="Configure Social Stack" \
bash << 'EOF'
echo "# $VERSION $'\n' "* $MESSAGE" >> CHANGELOG.md && \
git add . && \
git commit -m "$MESSAGE $VERSION" && \
git push
EOF
```

This will trigger the workflows in `.github/workflows`, and GitHub will release and deploy the project for you.

### Doker
Instructions:
1. Fork the repository
2. Make [configuring](#configuring) changes as needed
3. Build the Docker container: `docker build -t <TAG>`
3. Run the container `docker run -d -p <PORT>:80 <TAG>`

### Building manually
Instructions:
1. Fork the repository
2. Make [configuring](#configuring) change as needed
3. Install Python
4. Optional (Recommended): Create a virtual environment in Python `python -m venv .<VENV>`
5. Optional (Recommended): Access your virtual environment by writing `./<VENV>/bin/activate` (GNU/Linux) or `.\<VENV>\Scripts\Activate.ps1` (Windows PowerShell) or `.\<VENV>\Scripts\activate.bat` (Windows cmd)
6. Install the dependencies using pip `pip install -r requirements.txt`
7. Run the rendering script `python renderer.py`

This creates a new directory, `renders/` containing the HTML, CSS, JS and asset files.

