.venv\Scripts\activate
python -m pip install --upgrade --force-reinstall pip
pip freeze > requirements.txt
pip uninstall -r requirements.txt -y