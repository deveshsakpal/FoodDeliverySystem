from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Food Delivery System"

@app.route("/menu")
def menu():
    return "Pizza - Rs. 200 | Burger - Rs. 150 | Biryani - Rs. 250"

@app.route("/order")
def order():
    return "Order placed successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)