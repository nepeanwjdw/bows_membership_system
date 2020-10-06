# User Guide
## Installing the Application
#### Setup the Database
1. Install Homebrew (if not installed already): `/usr/bin/ruby -e "$(curl -fsSL
https://raw.githubusercontent.com/Homebrew/install/master/install)"`
1. Run `brew update`
1. Globally install postgres: `brew install postgres`
1. Start the postgres server: `pg_ctl -D /usr/local/var/postgres start`
1. Connect to the auto-generated database: `psql postgres`
1. Create a user for django to access the database: `CREATE USER bows_owner WITH PASSWORD 'postgres';`
1. Create the database: `CREATE DATABASE bows_db WITH OWNER bows_owner;`
1. Quit psql `\q`
#### Download the Application
1. Run `git clone <enter repo here>`
#### Setup Pipenv and Run the Application
1. Install pipenv: `brew install pipenv`
1. Install the last successful environment recorded: `pipenv install --ignore-pipfile`
1. Activate the virtual environment `pipenv shell`
1. Setup the database structure `python manage.py migrate`
1. If deploying locally, run the development server: `python manage.py runserver`
## APIs
The below shows a catalogue of API endpoints available to call.

HTTP Method | Action | Requires Token | Path
--- | --- | --- | ---
GET | Retrieve user's id and name | No | /api/v1/users/get-id/\<card-id>
POST | Login  | No | /api/v1/users/login
GET | Get user's details | Yes | /api/v1/users/get-details/\<user-id>
POST | Register | No | /api/v1/users/register
PUT/PATCH | Top Up | Yes | /api/v1/users/top-up/\<user-id>
POST | Logout | Yes | /api/v1/users/logout

Where the following consists of:
* \<card-id>: 16 alphanumeric characters e.g. r7jTG7dqBy5wGO4L
* \<id>: six digits  e.g. 532752

An example of using an authentication token in a curl command:
`-H "Authorization: Token f7d5450f2a81be4dd01a2388120b9e48289f740a"`

See the [Manual Testing](manual_testing.md) page for more in-depth instructions on how to call the endpoints
