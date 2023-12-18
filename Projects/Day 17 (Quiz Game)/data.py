import requests
import html


def questions_api():
    # getting inputs
    num_questions = int(input("How many question do you want? "))

    print_categories()
    category = input("Which category do you want? ").lower().strip()

    difficulty = input("Choose a difficulty (Easy/Medium/Hard): ").lower().strip()

    # request new token
    token = requests.get('https://opentdb.com/api_token.php?command=request').json()
    token = token['token']

    # requesting data from api
    url = f'https://opentdb.com/api.php?amount={num_questions}&category={category}&difficulty={difficulty}' \
          f'&type=boolean&token={token}'
    r = requests.get(url)
    api_data = r.json()

    return format_api_data(api_data)


def print_categories():
    # initial message
    print("Printing the category options....")
    # get request
    r = requests.get('https://opentdb.com/api_category.php')
    categories = r.json()
    # loop through categories
    for cat in categories['trivia_categories']:
        print(f"Id: {cat['id']:2} | Category: {cat['name']:40}")


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
