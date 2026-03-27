## Day 23 — Virtual Environment  

> Today’s focus: use Python virtual environments to isolate dependencies per project, and manage them with pip and requirements files.  
> Author: Luka Marinkovic  

### Why virtual environments matter  

I learned that a virtual environment is a self‑contained Python installation that keeps its own packages separate from the global system Python. This prevents “dependency hell”, where different projects require incompatible versions of the same package. By creating a venv per project, I can upgrade, install, or remove libraries without breaking other projects on my machine.  

### Creating and activating a virtual environment  

On the command line, I used `python -m venv env` (or another name like `.venv`) to create a new virtual environment folder. To start using it I activated it (for example on Windows with `env\Scripts\activate` or on Unix‑like systems with `source env/bin/activate`), which changes the prompt and ensures that `python` and `pip` now refer to the environment’s executables. When I’m done, I can run `deactivate` to return to the global Python context.  

### Installing packages inside the venv  

With the environment active, I used `python -m pip install package_name` to install libraries such as `requests`, `pandas`, or `beautifulsoup4`. Only the virtual environment sees these installations, so `pip list` inside the venv shows a smaller, project‑specific set of packages. This makes it easy to experiment with different versions without affecting system tools or other projects.  

### Requirements.txt and pip freeze  

I learned that `python -m pip freeze` outputs an exact list of installed packages and their versions. Redirecting this to a `requirements.txt` file (for example `python -m pip freeze > requirements.txt`) captures the environment’s dependencies in a reproducible format. On another machine—or in a fresh venv—I can run `python -m pip install -r requirements.txt` to recreate the same environment. This is especially useful for sharing projects or deploying them.  

### Good practices for environments  

I saw that it’s best to always create a new virtual environment for each larger project and keep the folder (like `env` or `.venv`) out of version control using `.gitignore`. I also understood that I should run `pip freeze` only from within the active venv to avoid including unrelated global packages. Together, these habits make my Python projects easier to maintain, share, and run consistently on different systems.