# build_files.sh
python3 --version
python3 -m ensurepip --upgrade
pip install -r requirements.txt
python3 manage.py collectstatic --noinput