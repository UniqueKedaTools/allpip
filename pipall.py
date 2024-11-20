import subprocess
import sys
print("""

__________._____________     _____  .____    .____     
\______   \   \______   \   /  _  \ |    |   |    |    
 |     ___/   ||     ___/  /  /_\  \|    |   |    |    
 |    |   |   ||    |     /    |    \    |___|    |___ 
 |____|   |___||____|     \____|__  /_______ \_______ \ 
                                  \/        \/       \/
                                  by kawaz""")

modules = [
    'numpy', 'pandas', 'matplotlib', 'requests', 'scikit-learn', 'tensorflow', 'keras', 'seaborn', 'scipy', 'plotly',
    'flask', 'django', 'sqlalchemy', 'beautifulsoup4', 'lxml', 'pillow', 'pytest', 'mock', 'pyyaml', 'paramiko',
    'pyspark', 'sympy', 'statsmodels', 'opencv-python', 'python-dateutil', 'pyodbc', 'pyautogui', 'geopy', 'pyttsx3',
    'smtplib', 'twilio', 'cx_Oracle', 'pyjnius', 'cx_Freeze', 'pyinstaller', 'nltk', 'textblob', 'pytesseract', 
    'imageio', 'pyaudio', 'cherrypy', 'fastapi', 'pydantic', 'requests-html', 'bokeh', 'dash', 'pyqt5', 'kivy',
    'jupyter', 'ipython', 'notebook', 'sympy', 'pywin32', 'watchdog', 'tabulate', 'faker', 'loguru', 'click', 
    'colorama', 'rich', 'tqdm', 'xlrd', 'openpyxl', 'xlwt', 'cryptography', 'pycryptodome', 'pyzbar', 'pyjsparser', 
    'nose', 'asyncio', 'aiohttp', 'tornado', 'celery', 'redis', 'sqlalchemy', 'boto3', 'google-api-python-client', 
    'gspread', 'pika', 'paramiko', 'dataclasses', 'shapely', 'fuzzywuzzy', 'texttable', 'soundfile', 'librosa', 
    'python-igraph', 'rpy2', 'pyqode', 'python-magic', 'h5py', 'biopython', 'pycuda', 'pyarrow', 'python-mnist', 
    'pywebview', 'pyshorteners', 'pytz', 'watchdog', 'pytest-cov', 'pytest-mock', 'unittest', 'hypothesis', 'shutil',
    'selenium', 'pytorch', 'openai', 'pyttsx3', 'pylint', 'pytest-bdd', 'celery', 'gevent', 'websockets', 'kafka-python',
    'elasticsearch', 'pymongo', 'cx_Oracle', 'psycopg2', 'sqlalchemy', 'peewee', 'tweepy', 'python-twitter', 'telegram',
    'discord.py', 'pywikibot', 'lxml', 'requests-oauthlib', 'pyjwt', 'rsa', 'ecdsa', 'pyspelling', 'netmiko', 'paramiko',
    'pygraphviz', 'matplotlib', 'plotly', 'pyplot3d', 'vispy', 'mpl_toolkits', 'networkx', 'py3Dmol', 'vedo', 'mayavi',
    'pyOpenGL', 'pyfunt', 'ptvsd', 'pdb', 'flask-login', 'flask-restful', 'flask-socketio', 'flask-wtf', 'flask-babel',
    'flask-mail', 'flask-admin', 'flask-cors', 'flask-sqlalchemy', 'flask-bootstrap', 'flask-testing', 'flask-security', 
    'flask-jwt-extended', 'flask-migrate', 'flask-marshmallow', 'flask-wtf', 'django-cors-headers', 'django-rest-framework',
    'django-allauth', 'django-filter', 'django-crispy-forms', 'django-debug-toolbar', 'django-model-utils', 
    'django-extensions', 'django-rq', 'django-cache-url', 'django-storages', 'django-modeltranslation', 'py3dbp', 'pyface', 
    'kivy', 'matplotlib', 'geopandas', 'shapely', 'cartopy', 'folium', 'requests-cache', 'geocoder', 'gdal', 'cartopy',
    'folium', 'osmnx', 'pymap3d', 'pyproj', 'xgboost', 'lightgbm', 'catboost', 'fastai', 'prophet', 'yellowbrick',
    'sklearn-pandas', 'imbalanced-learn', 'tpot', 'optuna', 'hyperopt', 'pytest-sugar', 'pytest-asyncio', 'pytest-flask', 
    'pylint', 'flake8', 'tox', 'black', 'autopep8', 'isort', 'mypy', 'django-stubs', 'pyright', 'prettier', 'bandit',
    'pyup', 'trufflehog', 'sentiment-analysis', 'rasa', 'convo', 'transformers', 'sentence-transformers', 'spaCy', 
    'tesseract', 'azure-cognitiveservices-vision-computervision', 'google-cloud-vision', 'pytorch-lightning', 'matplotlib',
    'wordcloud', 'pytrec', 'allennlp', 'textacy', 'spaCy', 'scikit-image', 'deepface', 'deepdetect', 'detectron2', 'albumentations',
    'PyTorchGeometric', 'torchvision', 'torch', 'fastapi', 'aiohttp', 'websockets', 'python-telegram-bot', 'discord.py',
    'instaloader', 'instaloader', 'instaloader', 'instaloader', 'instaloader', 'instaloader', 'instaloader', 'instaloader',
    'pystyle', 'subprocess', 'phonenumbers'
]


def installer(module):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
        print(f"{module} installé avec succès.")
    except subprocess.CalledProcessError:
        print(f"Erreur lors de l'installation de {module}.")

for module in modules:
    installer(module)
