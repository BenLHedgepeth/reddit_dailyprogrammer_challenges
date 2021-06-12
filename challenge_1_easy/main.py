
import re
import datetime

def clean_value(x):
    n = int(x)
    if len(x) == 2 and n < 10:
        n = int(x[1])
    return n

def introduce():
    user = {
        'name': {
            'regex': re.compile(r"^[A-Z]{1,}", re.I),
            'prompt': "Provide your first name:\n>>> ",
            'error': "The name your provided is invalid. Try another one.\n>>> "
        },
        'age': {
            'regex': re.compile(r"^\d{4}-\d{2}-\d{2}"),
            'prompt': "Provide your birthday (YYYY-MM-DD):\n>>> ",
            'error': "Invalid date provided. Date format must be: YYYY-MM-DD\n>>> "
        },
        'username': {
            'regex': re.compile(r"^\w{3,15}"),
            'prompt': "Enter your username:\n>>> ",
            'error': "That username doesn't work. A user name must consist between 3 and 15 characters\n>>> "
        }
    }
    for user_key in user.keys():
        while True:
            value = input(user[user_key]['prompt'])
            criteria_match = re.match(user[user_key]['regex'], value)
            if not criteria_match:
                print(user[user_key]['error'])
                continue
            else:
                if user_key == 'age':
                    birthday = criteria_match.group().split("-")
                    year, month, day = list(
                        map(clean_value, birthday)
                    )
                    today = datetime.date.today()
                    if year > today.year:
                        error = f"You cannot be born after {today.year}. "
                        error += f"Re-enter your birth date (YYYY-MM-DD)\n>>> "
                        user[user_key].update(prompt=error)
                        continue
                    else:
                        try:
                            date = datetime.date(year, month, day)
                        except ValueError:
                            prompt = "Double check your birthday...(YYYY-MM-DD)\n>>> "
                            user[user_key].update(prompt=prompt)
                            continue
                user[user_key].update(value=criteria_match.group())
                break
    name, age, username = [
        user['name']['value'], user['age']['value'], user['username']['value']
    ]
    return f"Your name is {name}, you are {age} years old, and your username is {username}."

if __name__=="__main__":
    greeting = introduce()
    print(greeting)
