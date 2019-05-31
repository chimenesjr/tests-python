student = {
    "name": "Jason",
    "hobbies": ["music", "code", "games"],
    "job": "software developer",
    'feedback': None
}

student['last-name'] = 'chimenes'

try:
    last_name = student['last-name']
    number = 4 + last_name
except KeyError as KeyError:
    print(KeyError)
except TypeError as type_error:
    print(type_error)
except Exception:
    print('general error')
finally:
    print('fechou')

print('run anyway')