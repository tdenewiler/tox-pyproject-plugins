# Tox Pyproject Plugins

Example project with plugins.

Make sure to have a virtual environment where the `tox-pyproject` package has already been installed.
The directory structure used looks like:

- ~/src/tox-pyproject
  - tox-pyproject (git repo)
  - tox-pyproject-plugins (git repo)
  - venv

Create and activate a virtual environment, then install the `tox-pyproject` package.

```shell
cd ~/src/tox-pyproject
python3 -m venv venv
. venv/bin/activate
cd tox-pyproject
pip install .
```

Install the `tox-pyproject-plugins` package and make sure that both `a` and `b` plugins are discovered.

```shell
cd ~/src/tox-pyproject/tox-pyproject-plugins
pip install .
tox_project
```

Expected results are

```shell
$ tox_pyproject
discovered plugins: [EntryPoint(name='a', value='tox_pyproject.plugins.discovery.a:ADiscoveryPlugin', group='tox_pyproject.plugins.discovery'), EntryPoint(name='b', value='tox_pyproject.plugins.discovery.b:BDiscoveryPlugin', group='tox_pyproject.plugins.discovery')]
start
---Discovery---
Running A discovery plugin...
A discovery plugin done.
Running B discovery plugin...
B discovery plugin done.
All plugins run: ['A', 'B']
---Discovery---
success: True
```

Running `tox-pyproject-plugins` unit tests with `pytest` works.

```shell
cd ~/src/tox-pyproject/tox-pyproject-plugins
pip install .
pip install .[test]
pytest tests/
```

Running the unit tests with `tox` does not work.

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
$ ls ~/src/tox-pyproject/tox-pyproject-plugins/.tox/py310/lib/python3.10/site-packages/tox_pyproject/
app.py  config.py  __init__.py  plugins  __pycache__  tox_pyproject.py
```

After running tox once (so the tox virtual environment is created) it is possible to run the import command that failed
inside the tox virtual environment.

```shell
deactivate # from original virtual environment
. .tox/py310/bin/activate
python
from tox_pyproject.config import Config
```

It is not clear why the module is available in the tox virtual environment, but is not found when running the `tox`
command.
