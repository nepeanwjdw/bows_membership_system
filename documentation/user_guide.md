# User Guide
## Installing the Application
## APIs
This table will be updated throughout the development of the project to show the catalogue of APIs available to call.

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

An example of using an authentication token in a curl command: `-H "Authorization: Token f7d5450f2a81be4dd01a2388120b9e48289f740a"`
