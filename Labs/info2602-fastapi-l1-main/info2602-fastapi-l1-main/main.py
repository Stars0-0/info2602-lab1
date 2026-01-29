from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'

@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: # select only the students with a given meal preference
            filtered_students.append(student) # add match student to the result
        return filtered_students
    return data

#Exercise 1

@app.get('/stats')
async def get_stats():
    meal_stats = {}
    programme_stats = {}

    for student in data:
        meal = student['pref']
        programme = student['programme']

        if meal in meal_stats:
            meal_stats[meal] += 1
        else:
            meal_stats[meal] = 1

        if programme in programme_stats:
            programme_stats[programme] += 1
        else:
            programme_stats[programme] = 1

    return {
        "meal_preferences": meal_stats,
        "programmes": programme_stats
    }


#Exercise 2

@app.get('/add/{a}/{b}')
def add(a: int, b: int):
    return a + b

@app.get('/subtract/{a}/{b}')
def subtract(a: int, b: int):
    return a - b

@app.get('/multiply/{a}/{b}')
def multiply(a: int, b: int):
    return a * b

@app.get('/divide/{a}/{b}')
def divide(a: int, b: int):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
