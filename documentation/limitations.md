# Limitations and Future Improvements
### Limitations
* Currently the login endpoint only returns the authorisation token in the response. I have a separate endpoint,
requiring the token, to invoke which provides the user details including the balance and last_login fields in the
response. If I had more time I would look at providing the user details in the login endpoint response
* Some fields are named differently due to the constraints of the framework I used. For example, the kiosk will
need to provide 'username' and 'password' in place of the user's 'id' and 'pin' when calling login endpoint
* Currently the authentication tokens do not expire, however, the kiosk could potentially call the logout endpoint after
a few minutes of inactivity which would delete the token
* Currently, if the initial endpoint to retrieve the user's id and name fails as it can't find the user, then is will
return a not found message. The Kiosk will need to then call the register endpoint. If I had more time I would add this
logic to the API
### Future Improvements
* After successfully topping up, the details of the transaction are be returned in the response. A feature that
could be implemented is to display a list of a user's transaction history
* The API could be extended to provide functionality to view and purchase goods
* A feature could be implemented to allow a user to change their details
* I decided to use a decimal field to represent the balance and transactions, however I would consider changing the
format to integer (to display the pence rather than pounds) in line with industry standards
* I could implement a routing page which provides a list of available APIs to call
* When calling the register endpoint, the new user details are returned, including the password. It's not a security
concern as it's the hashed password, but it doesn't need to be returned so I could configure it not to
