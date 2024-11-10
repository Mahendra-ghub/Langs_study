import csv
import hashlib
import requests
from getpass import getpass

# Replace with your News API key (get it from https://newsapi.org/)
NEWS_API_KEY = "b46305602146404dacdb3397a96af8b1"  # Ensure you keep the quotes around the API key

# Define constants
MAX_LOGIN_ATTEMPTS = 5
LOGIN_FILE = "regno.csv"

def validate_email(email):
    return "@" in email and "." in email.split("@")[1]

def validate_password(password):
    return len(password) >= 8 and any(char in "!@#$%^&*()_+-=[]{};':|\,.<>/? " for char in password)

def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def load_users():
    users = {}
    try:
        with open(LOGIN_FILE, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users[row["email"]] = row
    except FileNotFoundError:
        print(f"CSV file '{LOGIN_FILE}' not found. Please create it.")
    return users

def login(users):
    login_attempts = 0
    while login_attempts < MAX_LOGIN_ATTEMPTS:
        email = input("Enter your email: ")
        if not validate_email(email):
            print("Invalid email format. Please try again.")
            continue

        password = getpass("Enter your password: ")
        if not validate_password(password):
            print("Password must be at least 8 characters and contain a special character.")
            continue

        if email in users:
            hashed_password = users[email]["password"]
            if hash_password(password) == hashed_password:  # Corrected the comparison
                print("Login successful!")
                return users[email]
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Email not found. Please try again.")

        login_attempts += 1
    print("Maximum login attempts reached. Please restart the application.")
    return None

def forgot_password(users):
    email = input("Enter your registered email: ")
    if email in users:
        security_question = users[email]["security_question"]
        answer = input(f"Answer your security question: {security_question}")
        if answer == users[email]["security_answer"]:
            new_password = getpass("Enter your new password: ")
            if validate_password(new_password):
                users[email]["password"] = hash_password(new_password)
                with open(LOGIN_FILE, "w", newline="") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=users[email].keys())
                    writer.writeheader()
                    writer.writerow(users[email])
                print("Password reset successful!")
                return True
        else:
            print("Incorrect security answer. Password reset failed.")
    else:
        print("Email not found. Password reset failed.")
    return False

def fetch_news(keyword):
    url = f"https://newsapi.org/v2/top-headlines?q={keyword}&apiKey={NEWS_API_KEY}"  # Use NEWS_API_KEY
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-200 status codes
        data = response.json()
        if data["status"] == "ok" and data["articles"]:
            articles = data["articles"][:5]  # Get top 5 headlines
            headlines = [f"{article['title']} - {article['source']['name']}" for article in articles]
            return headlines
        else:
            print("No news found for the given keyword.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None

if __name__ == "__main__":
    users = load_users()
    while True:
        print("Welcome to the News App!")
        print("1. Login")
        print("2. Forgot Password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_data = login(users)
            if user_data:
                keyword = input("Enter a keyword or topic: ")
                headlines = fetch_news(keyword)
                if headlines:
                    print("Top 5 news headlines:")
                    for headline in headlines:
                        print(headline)
                else:
                    print("No news found for the given keyword.")
        elif choice == "2":
            forgot_password(users)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
