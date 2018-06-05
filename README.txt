python_version = "3.5"

If you want to use app on serve, go to:
https://cointrends2.herokuapp.com

If you want to run app locally, do the following:

1. Clone the application code from CoinTrends repository

2. Create and activate python virtual environment
$ virtualenv -p python3 venv
$ source venv/bin/activate

3. Install required python dependencies
In project root directory run:
$ pip install -r requirements.txt
or
find necessary packages in Pipfile
$ pip install pipenv
$ pipenv install

4. Run app
In directory CoinTrends, in terminal window:
$ export FLASK_APP=Kainos_static.py
$ flask run

*another run : $ flask run
