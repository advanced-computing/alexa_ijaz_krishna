from flask import Flask, jsonify, request
import duckdb

app = Flask(__name__)

# Database helper function
def get_db():
    return duckdb.connect('nypd_date.db')

# POST method to register a new user
@app.route("/register", methods=["POST"])
def register_user():
    username = request.json.get('username')
    age = request.json.get('age')
    country = request.json.get('country')

    with get_db() as con:
        con.execute("INSERT INTO users (username, age, country) VALUES (?, ?, ?)", 
                    (username, age, country))

    return jsonify({"message": "User added successfully"}), 201

# GET method to fetch user statistics
@app.route("/user_stats", methods=["GET"])
def user_stats():
    with get_db() as con:
        total_users = con.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        avg_age = con.execute("SELECT AVG(age) FROM users").fetchone()[0]
        top_countries = con.execute("""
            SELECT country, COUNT(*) AS count
            FROM users
            GROUP BY country
            ORDER BY count DESC
            LIMIT 3
        """).fetchall()

    return jsonify({
        "total_users": total_users,
        "avg_age": avg_age,
        "top_countries": [{"country": row[0], "count": row[1]} for row in top_countries]
    })

if __name__ == "__main__":
    app.run(debug=True)
