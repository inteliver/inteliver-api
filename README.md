# Inteliver API

Welcome to the Inteliver API repository! This template is designed for building AI services using FastAPI as the REST API server, with Docker and docker-compose for containerization.

## Main Folders

- **app:** Main application code resides here.
  - **app/assets:** Houses assets, files, and images.
  - **app/controllers:** Contains the controllers and logic code for the server.
  - **app/errors:** Holds error response definitions.
  - **app/routers:** Routers for defining API paths.
  - **app/schemas:** Pydantic schemas for the API.
  - **app/utils:** Any additional utility functions can be found here.
  - **app/models:** Store the AI models here.
  - **app/main.py:** The main FastAPI file.

- **docs:** Auto-generated code documentation. Do not modify this directory; it's generated using `make docs`.

- **tests:** Primary folder for unit tests and integration tests.

## Setup

### Using setup.sh

Run the `setup.sh` script to create a Conda environment, install main and development dependencies, and execute the project.

### Using Makefile

1. **Create a Conda environment:**
    ```sh
    conda create -n your-project-name python=3.11
    ```

2. **Install Dependencies:**
    ```sh
    make install-deps
    make install-dev-deps
    ```

3. **Run the Project:**
    ```sh
    make run
    ```

Feel free to explore the folders and utilize the structure to build robust AI services with FastAPI. Have fun coding!


## Linting

Before committing any changes, it's recommended to run the linting process using the following command:

```bash
make lint
```

This command will execute the linting checks based on the configurations specified in mypy.ini and .flake8 files. These configurations define rules for mypy and flake8 to ensure code consistency, style adherence, and type checking across the project.

## Make New AI Service Project

1. clone this repo
```bash
git clone http://172.31.112.27/ai-services/ai-service-template.git
```

2. change the remote to your-project
```bash
git remote rename origin template
git remote add origin http://172.31.112.27/ai-services/your-service-project.git
```

3. rename `ai-service-template` in the following locations to your project service name.
- docker-compose.yml
- Makefile
- setup.sh
- README.md
- interface.py
- main.py (docstring, fastapi, and root endpoint)
- utils/eureka.py (app-name)

search for `ai-service-template` to make sure you have renamed to your project name.

4. create conda env and running the `setup.sh` file, and installing the dependencies.
```bash
./setup.sh
```

5. start by creating a router file in `routers` and add your router in `routers/__init__.py`. Use `version_router` example.

6. we use trunk-based development. You can create feature branches and merge those frequent updates to `main` or directly push to main.

7. use `main` as default branch name.

8. use `make lint` before every commit and resolve `mypy` and `flake8` errors.

9. build docs after developing the main functionalities and classes.

```bash
make docs

pdoc -f --html --output-dir docs --config show_source_code=False app/
```

10. add gradio interface after developing the service api.

11. update dockerfile and build docker image.
```bash
make build-docker
```

12. build pydantic schemas for input and output of your api's.


## Versioning

[Python Semantic Release (PSR)](https://python-semantic-release.readthedocs.io/en/latest/) is a tool that can automatically bump version numbers based on keywords it finds in commit messages. The idea is to use a standardized commit message format and syntax, which PSR can parse to determine how to increment the version number. The default commit message format used by PSR is the [Angular commit style](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commit-message-format), which looks like this:

```bash
<type>(optional scope): short summary in present tense

(optional body: explains motivation for the change)

(optional footer: note BREAKING CHANGES here, and issues to be closed)
```

`<type>` refers to the kind of change made and is usually one of:

* `feat`: A new feature.

* `fix`: A bug fix.

* `docs`: Documentation changes.

* `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).

* `refactor`: A code change that neither fixes a bug nor adds a feature.

* `perf`: A code change that improves performance.

* `test`: Changes to the test framework.

* `build`: Changes to the build process or tools.

`scope` is an optional keyword that provides context for where the change was made. It can be anything relevant to your package or development workflow (e.g., it could be the module or function name affected by the change).

Different text in the commit message will trigger PSR to make different kinds of releases:

* A `<type>` of `fix` triggers a patch version bump, e.g.:

```bash
$ git commit -m "fix(mod_plotting): fix confusing error message in \
                 plot_words"
```

* A `<type>` of `feat` triggers a minor version bump, e.g.:

```bash
$ git commit -m "feat(package): add example data and new module to \
                 package"
```

* The text `BREAKING CHANGE`: in the `footer` will trigger a major release, e.g.:

```bash
$ git commit -m "feat(mod_plotting): move code from plotting module \
                 to pycounts module
$ 
$ BREAKING CHANGE: plotting module wont exist after this release."
```

### commands

To release a new version using semantic-release you can use the following make command.

```bash
make version
```

The detailed commands for using the semantic-release.

```bash

# default use this command: to update the version, commit and push the version change
semantic-release version --no-tag --no-vcs-release

# to show the next version only
semantic-release -vv --noop version --print

# show the next version updating patch
semantic-release version --patch --print

# to forcefully update the patch number
semantic-release version --patch --no-tag --no-vcs-release

# show the next version updating minor
semantic-release version --minor --print

# to forcefully update the minor number
semantic-release version --minor --no-tag --no-vcs-release

# show the next version updating major
semantic-release version --major --print

# to forcefully update the major number
semantic-release version --major --no-tag --no-vcs-release
```

