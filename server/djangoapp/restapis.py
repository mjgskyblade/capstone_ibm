# Uncomment the imports below before you add the function code
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def fetch_reviews():
    # Define the endpoint for fetching reviews
    endpoint = "/fetchReviews"
    # Make a GET request to fetch reviews from the backend
    reviews = get_request(endpoint)
    return reviews
    
def get_request(endpoint, **kwargs):
# Add code for get requests to back end
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict, dealer_id):  # dealer_id parameter
    request_url = backend_url + "/insert_review"
    data_dict['dealer_id'] = dealer_id  # dealer_id to the data dictionary
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")

def add_review(request, dealer_id):  # dealer_id parameter
    if(request.user.is_anonymous == False):
        data = json.loads(request.body)
        try:
            response = post_review(data, dealer_id)  # Pass dealer_id to post_review
            return JsonResponse({"status": 200})
        except:
            return JsonResponse({"status": 401, "message": "Error in posting review"})
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})