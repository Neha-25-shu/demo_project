## APIs Details

Base URL for all API endpoints : `http://127.0.0.1:8000/` <br />


i. User - Registration
Create/ Register a new user.

	Endpoint 	: http://127.0.0.1:8000/accounts/signup/
	Request Type 	: POST
	Request Params 	: username, email, password, password_2
	Non-mandatory params : invite_code

	Response Http status codes : HTTP_200_OK or HTTP_400_BAD_REQUEST
	
  
ii. User - Login
Obtain authentication token given the user credentials.

	Endpoint 	: http://127.0.0.1:8000/accounts/login/
	Request Type 	: POST
	Request Params 	: email (or username) and password
	
	Response 	: { "token": <token> }
	HTTP status code: HTTP_200_OK or HTTP_400_BAD_REQUEST
	
iii. User - Request for Password Reset
Receive an email with password reset link.

	Endpoint 	: http://127.0.0.1:8000/accounts/password/reset/
	Request Type 	: POST
	Request Params 	: email
	Request Sample : {"email": "some_email_id@gmail.com"}
	
	HTTP status code: HTTP_200_OK

iv. User - Password Change
  Change the password. Link as recieved from email by above request (iv).
	
	Endpoint 	: http://127.0.0.1:8000/accounts/change-password/
	Request Type 	: POST
  
