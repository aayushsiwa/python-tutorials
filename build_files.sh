# build_files.sh
python3 --version
pip install -r requirements.txt
python3 manage.py collectstatic --noinput