# build_files.sh
python3 --version
python -m ensurepip --upgrade
pip install -r requirements.txt
python3 manage.py collectstatic --noinput