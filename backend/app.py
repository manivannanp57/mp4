from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

DB_HOST="mp4-db.cp2go8020sgw.us-east-1.rds.amazonaws.com"
DB_USER="admin"
DB_PASSWORD="ManiPass123!"
DB_NAME="mp4db"

def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status":"healthy"}), 200

@app.route("/events", methods=["POST"])
def insert_event():

    payload=request.json

    conn=get_conn()

    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO events (title,date,image_url,description,location)
            VALUES(%s,%s,%s,%s,%s)
            """,
            (
                payload["title"],
                payload["date"],
                payload["image_url"],
                payload["description"],
                payload["location"]
            )
        )
        conn.commit()

    conn.close()

    return jsonify({"message":"Event created successfully"}), 201


def fetch_events():

    conn=get_conn()

    with conn.cursor() as cur:
        cur.execute("""
        SELECT title,date,image_url,description,location
        FROM events
        ORDER BY date DESC
        """)
        rows=cur.fetchall()

    conn.close()

    return rows


@app.route("/data")
def get_data():

    return jsonify({"data":fetch_events()})


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

