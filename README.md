# real-estate-demo

- project setup 
1. cd to the root folder of the project
2. create a python environment using this command: python -m venv ./venv
3. activate the python environment using this command: source venv/Scripts/activate
4. install the required libraries by running this command: pip install -r requirements.txt
5. Set up Oracle Instant Client and your .env (see configuration below)

- run project
1. cd to the root folder of the project
2. run the flask app using this command: flask run

- configuration
1. Copy `.env.example` to `.env` and fill in your Oracle Autonomous Database, Oracle Content Management and Oracle Integration credentials. `flask run` loads `.env` automatically via python-dotenv.
2. Download Oracle Instant Client (with your database wallet in `network/admin`) into `Oracle-client/instantclient_21_7`, or point `ORACLE_CLIENT_DIR` at it. Neither the client nor the wallet is committed to this repo.
