# TrackWatch
### Online Overwatch Match Logger
 TrackWatch is a Flask/Python web application that lets users log their Overwatch matches to keep track of their wins and losses. Submit matches and tag your friends at the same time so they can also keep track of their progress.  
### How to Install
```
pip install virtualenv
pip install -r requirements.txt
```

### MacOs
 if on conda:
```
conda deactivate
```
```
deactivate
source venv/bin/activate

export FLASK_APP=app.py  
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run
```

### Windows (Powershell)
```sh
owdb-env\Scripts\activate
$env:FLASK_ENV = "development"
$env FLASK_APP=app
flask run
```