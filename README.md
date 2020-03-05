# flask-api-starter

### Setup
  Steps for setup:
  1. Setup the virtual environment in pycharm editor and create a new project.
  2. Clone the content of this repository to the project folder.
  3. Install the requirements using 
  ```
      pip install -r requirement.txt
  ```
  4. Create a config.ini file with the following contents:
  '''
      	[credentials]
	username = <SQL Server Username>
	password = <SQL Server Password>
  '''
     These Username and Password should be same as your windows username and password.
  5. Run the api.py
  ```
      python api.py
  ```
  6. Once successfully run, open any rest client like postman and hit the auth URL. The request should look like below.
  ```
      URL: http://127.0.0.1:5000/auth
      VERB: POST
      HEADER:
        "Content-Type":"application/json"
      BODY:
        {
	        "username":"bob",
	        "password":"asdf"	
        }
   ```
  7. The response of above request would return an access_token. Copy the token and make another sample request like below.
```
      URL: http://127.0.0.1:5000/
      VERB: GET
      HEADER:
        "Authorization":"JWT <ACCESSTOKEN>"
```
  8. The response for the above request will be: "Hello World"
   
   
  ### Additional Points
   - Currently the username & password are hardcoded in the security.py. This should be stored in the database user table.
   - The secret_key for encryption in Auth is hard coded in the variable. Ideally this should managed by a trusted platform service.
