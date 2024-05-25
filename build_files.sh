# build_files.sh
python3 --version
python3 -m ensurepip --upgrade
pip3 install -r requirements.txt
# python3 manage.py collectstatic --noinput