import requests
import json

YOUR_EMAIL = "manivannan57@gmail.com"
YOUR_SECRET = "sZDvmlFlNGrPrTtH"

FRONTEND_URL = "http://mp4-frontend-635114519658.s3-website-us-east-1.amazonaws.com"
BEANSTALK_URL = "http://mp4-backend-env.eba-zmt7mc3z.us-east-1.elasticbeanstalk.com"

FRONTEND_S3_LOG_URL = "https://mp4-logs-635114519658.s3.amazonaws.com/frontend-logs/?AWSAccessKeyId=AKIAZHX6GPRVLVLHZA2O&Signature=s7Pp67vmc6ONi2mgJ2CQBYeltHM%3D&Expires=1773553908"

BACKEND_S3_LOG_URL = "https://mp4-logs-635114519658.s3.amazonaws.com/backend-logs/?AWSAccessKeyId=AKIAZHX6GPRVLVLHZA2O&Signature=DrB9KDkKM%2B%2BFk%2BJAp5SBh8h%2FHmg%3D&Expires=1773553908"

LAMBDA_URL = "https://ttrejw3rxf.execute-api.us-east-1.amazonaws.com/default/mp5_fullstack"

input_data = {
    'frontend_url': FRONTEND_URL,
    'beanstalk_url': BEANSTALK_URL,
    'frontend_s3_log_url': FRONTEND_S3_LOG_URL,
    'backend_s3_log_url': BACKEND_S3_LOG_URL,
    'submitterEmail': YOUR_EMAIL,
    'secret': YOUR_SECRET
}

payload = {
    "input": json.dumps(input_data),
}

try:
    response = requests.post(LAMBDA_URL, json=payload)
    print(response.status_code, response.reason)
    print(response.text)
except Exception as e:
    print("Error during submission:", e)

