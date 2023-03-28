import requests
import html


def format_api_data(api_data):
    # checking if the api worked
    if api_data['response_code'] == 0:
        # creating list dicts with each question and answer
        question_data = []
        for question_dict in api_data['results']:
            question_answer = {key: html.unescape(question_dict[key]) for key in ['question', 'correct_answer']}
            question_data.append(question_answer)
    # api error message:
    else:
        print("There was an error getting your questions. Please try again.")
        return

    return question_data


def questions_api():
    # requesting data from api
    url = "https://opentdb.com/api.php?amount=10&type=boolean"
    r = requests.get(url)
    api_data = r.json()

    return format_api_data(api_data)


class ApiManager:
    def __init__(self):
        self.questions = questions_api()


