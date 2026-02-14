from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DB = "users.db"
USER_ID = 1   # static user until login system added


def get_user():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (USER_ID,))
    user = cursor.fetchone()
    conn.close()
    return user


def update_user(data):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    query = """
        UPDATE users SET fullname=?, email=?, phone=?, address=?, bio=?, 
        instagram=?, linkedin=?, github=? WHERE id=?
    """

    cursor.execute(query, (*data, USER_ID))
    conn.commit()
    conn.close()


@app.route("/profile")
def profile():
    user = get_user()
    return render_template("profile.html", user=user)


@app.route("/update_profile", methods=["POST"])
def update_profile():
    data = (
        request.form["fullname"],
        request.form["email"],
        request.form["phone"],
        request.form["address"],
        request.form["bio"],
        request.form["instagram"],
        request.form["linkedin"],
        request.form["github"],
    )
    update_user(data)
    return redirect("/profile")


@app.route("/logout")
def logout():
    return "Logged out!"


app.run(debug=True, host="0.0.0.0", port=8000)