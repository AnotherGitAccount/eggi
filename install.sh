python3 -m venv .venv
source .venv/bin/activate
pip install flit
pip install -e .

flask --app eggi/app.py init-db