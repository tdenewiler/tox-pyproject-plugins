# Tox Pyproject Plugins

Example project with plugins.

Make sure to have a virtual environment where the `tox-pyproject` package has already been installed.
The directory structure used looks like:

- ~/src/tox-pyproject
  - tox-pyproject (git repo)
  - tox-pyproject-plugins (git repo)
  - venv

The virtual environment is created and activated with

```shell
cd ~/src/tox-pyproject
python3 -m venv venv
. venv/bin/activate
cd tox-pyproject
pip install .
```

Running the following works.

```shell
cd ~/src/tox-pyproject/tox-pyproject-plugins
pip install .
pip install .[test]
pytest tests/
```

Running this does not work.

```shell
tox
```

There are errors related to `ModuleNotFoundError` imported from the `tox-pyproject` package.

```shell
_______________________________________________________________ ERROR collecting tests/b/test_b.py _______________________________________________________________
ImportError while importing test module '/home/thomas/src/tox-pyproject/tox-pyproject-plugins/tests/b/test_b.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../tests/b/test_b.py:5: in <module>
    from tox_pyproject.plugins.discovery.b import BDiscoveryPlugin
../src/tox_pyproject/plugins/discovery/b.py:3: in <module>
    from tox_pyproject.config import Config
E   ModuleNotFoundError: No module named 'tox_pyproject.config'
```

The missing module is in the tox virtual environment.

```shell
$ ls .tox/py310/lib/python3.10/site-packages/tox_pyproject/
app.py  config.py  __init__.py  plugins  __pycache__  tox_pyproject.py
```

After running tox once it is possible to run the import command that failed inside the tox virtual environment.

```shell
deactivate # from original virtual environment
. .tox/py310/bin/activate
python
from tox_pyproject.config import Config
```
