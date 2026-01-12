from flask import Flask, render_template, request, jsonify
import datetime
import random
import wikipedia
import requests
import webbrowser

app = Flask(__name__)

FALLBACK_JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why was the computer cold? Because it forgot to close Windows."
]

FALLBACK_QUOTES = [
    "Believe in yourself.",
    "Hard work beats talent when talent doesn’t work hard."
]

def get_time():
    return datetime.datetime.now().strftime("The current time is %I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("Today is %A, %B %d, %Y")

def get_day():
    return datetime.datetime.now().strftime("Today is %A")

def get_month():
    return datetime.datetime.now().strftime("The current month is %B")

def get_year():
    return datetime.datetime.now().strftime("The current year is %Y")

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        data = response.json()
        return f"{data['setup']} {data['punchline']}"
    except:
        return random.choice(FALLBACK_JOKES)

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        data = response.json()
        return f"{data['content']} — {data['author']}"
    except:
        return random.choice(FALLBACK_QUOTES)

def get_news():
    try:
        response = requests.get("https://inshortsapi.vercel.app/news?category=technology", timeout=5)
        articles = response.json().get("data", [])
        selected = random.sample(articles, min(3, len(articles)))
        return "Top tech news: " + "; ".join(a["title"] for a in selected)
    except:
        return "Sorry, I couldn't fetch the news right now."

def get_weather(city="Pune"):
    try:
        response = requests.get(f"https://wttr.in/{city}?format=%C+%t", timeout=5)
        return f"The weather in {city} is {response.text}"
    except:
        return "Sorry, I couldn't fetch the weather right now."

def get_fact():
    facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries are not.",
        "Octopuses have three hearts."
    ]
    return random.choice(facts)

def random_number():
    return f"Your random number is {random.randint(1, 100)}"

def flip_coin():
    return f"It's {random.choice(['Heads', 'Tails'])}!"

def roll_dice():
    return f"You rolled a {random.randint(1, 6)}"

def process_command(command):
    command = command.lower().strip()

    if command in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    if "good morning" in command:
        return "Good morning! Hope you have a great day."

    if "good evening" in command:
        return "Good evening! How can I help?"

    if "thank" in command:
        return "You're welcome!"

    if "bye" in command:
        return "Goodbye! Have a nice day."

    if "who are you" in command:
        return "I am Titan, your Python-powered voice assistant."

    if "who created you" in command:
        return "I was created using Python and Flask."

    if "what can you do" in command:
        return (
            "I can tell time and date, fetch weather and news, "
            "tell jokes, quotes, facts, flip coins, roll dice, "
            "and answer Wikipedia questions."
        )

    if "time" in command:
        return get_time()

    if "date" in command or "today" in command:
        return get_date()

    if "day" in command:
        return get_day()

    if "month" in command:
        return get_month()

    if "year" in command:
        return get_year()

    if "weather" in command:
        city = command.replace("weather", "").strip() or "Pune"
        return get_weather(city)

    if "news" in command:
        return get_news()

    if "joke" in command:
        return get_joke()

    if "quote" in command:
        return get_quote()

    if "fact" in command:
        return get_fact()

    if "random number" in command:
        return random_number()

    if "flip a coin" in command:
        return flip_coin()

    if "roll a dice" in command or "roll dice" in command:
        return roll_dice()

    if "wikipedia" in command:
        try:
            topic = command.replace("wikipedia", "").strip()
            return wikipedia.summary(topic, sentences=2)
        except:
            return "Sorry, I couldn't find anything on Wikipedia."

    if "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    if "open github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    return "Sorry, I don't understand that yet."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    command = data.get("command", "")
    response = process_command(command)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)