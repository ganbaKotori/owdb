pip install virtualenv
pip install -r requirements.txt

MacOs:
conda deactivate (if on conda)
deactivate
source venv/bin/activate

export FLASK_APP=app.py  
export FLASK_ENV=development
export FLASK_DEBUG=1
flask fun

Windows:
owdb-env\Scripts\activate
$env FLASK_APP=app