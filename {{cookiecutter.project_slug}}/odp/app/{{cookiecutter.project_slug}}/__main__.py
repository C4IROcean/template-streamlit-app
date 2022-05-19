"""Top-level code-execution for streamlit applicatication

Allows a streamlit app to be run as a module:

```sh
python -m odp.app.{{cookiecutter.project_slug}}
```
"""
import sys
from streamlit import cli as stcli
import streamlit as st
from odp.app.{{cookiecutter.project_slug}}.app import main as streamlit_entry



if __name__ == "__main__":
    if st._is_running_with_streamlit:
        streamlit_entry()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())

