# $pip install Flask
from flask import Flask, jsonify, request, render_template, redirect
import pandas as pd 
import duckdb

app = Flask(__name__)

with duckdb.connect("nypd_date.db") as con:
    df = con.table("felony").to_df()
    print(df)

@app.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        username = request.form['username']
        age = request.form['age']
        country = request.form['country']
   
        with get_db() as con:
            con.execute("INSERT INTO users (username, age, country) VALUES (?, ?, ?)", 
                        (username, int(age), country))
        
        return redirect("/user_stats")

    return '''
        <h2>Register User</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Age: <input type="number" name="age"><br><br>
            Country: <input type="text" name="country"><br><br>
            <input type="submit" value="Register">
        </form>
    '''

@app.route("/user_stats", methods=["GET"])
def user_stats():
    with duckdb.connect("nypd_date.db") as con:
        total_users = con.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        avg_age = con.execute("SELECT AVG(age) FROM users").fetchone()[0]
        countries = con.execute("""
            SELECT country, COUNT(*) AS count
            FROM users
            GROUP BY country
            ORDER BY count DESC
            LIMIT 3
        """).fetchall()

    return jsonify({
        "Total Users": total_users,
        "Average Age": round(avg_age,0),
        "Top Countries": [{"Country": row[0], "Number": row[1]} for row in countries]
    })

@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""

    return "<p>Hello, World!</p>"

@app.route("/sum", methods=["GET"])
def sum():
    """Return the sum of two numbers."""
    a = request.args.get("a")
    b = request.args.get("b")

    return jsonify({"sum": int(a) + int(b)})

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
@app.route("/factorial", methods=["GET"])
def factorial_route():
    """Return the factorial of a number."""

    n = request.args.get("n",10)
    r = factorial(int(n))
    response = f'{n}! equals {r}'
    return response

@app.route("/whole_data", methods=["GET"])
def whole_data():
    """Return the whole dataset."""
    df = pd.read_csv('NYPD_Hate_Crimes_20250131.csv')
    df = df.to_csv()
    return jsonify(df)

@app.route("/year_data", methods=["GET"])
def year_data():
    df = pd.read_csv('NYPD_Hate_Crimes_20250131.csv')
    return jsonify(df["Complaint Year Number"].tolist())

@app.route("/alexa_mean_function", methods=["GET"])
def alexa_mean_function():
    df = pd.read_csv('NYPD_Hate_Crimes_20250131.csv')
    df["Month Number"] = df["Month Number"].astype(float)
    return calc_mean(df)

def calc_mean(df):
    mean = df["Month Number"].mean()
    return mean.astype(str)

if __name__ == "__main__":
    app.run(debug=True)

#disclaimer: used ChatGPT to figure out how to receive user information on website (via HTML)