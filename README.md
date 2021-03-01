# Syrups_dosage

1. In CMD clone git repository: git clone https://github.com/basileia/Syrups_dosage.git
2. Create new virtual environment in the folder: py -3 -m venv venv
3. Install requirements: pip install -r requirements.txt
4. To fully acces to database you need your own access account to MongoDb in file secrets.py
5. The FLASK_APP environment variable is used to specify how to load the application:  
      Windows CMD:  
      set FLASK_APP=app  
      flask run  
