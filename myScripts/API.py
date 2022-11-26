from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from time import sleep

import mysql.connector

app = FastAPI()


class Post(BaseModel):
    userid = int


class Get(BaseModel):
    userid = int
    ticketid = int


while True:
    try:
        connection = mysql.connector.connect(host="localhost",
                                             database="ticketjk",
                                             user="root",
                                             password="admin")
        cursor = connection.cursor()
        print("Database connection successful!")
        break
    except mysql.connector.Error as error:
        print("Connection to database failed")
        print("Error: ", error)
        sleep(3)


@app.post("/add-user")
def create_user(username, email, password):
    add_user = ("INSERT INTO user"
                "(username, password, email)"
                "VALUES (%s, %s, %s)")
    data_user = (username, password, email)
    create_record(add_user, data_user)


@app.post("/add-ticket")
def create_ticket(userid, issue, categoryid):
    add_ticket = ("INSERT INTO ticket"
                  "(issueDescription, userID, categoryID)"
                  "VALUES (%s, %s, %s)")
    data_ticket = (issue, userid, categoryid)
    create_record(add_ticket, data_ticket)


@app.post("/add-message")
def create_message(userid, ticketid, message=None):
    add_message = ("INSERT INTO message"
                   "(userID, ticketID, message)"
                   "VALUES (%s, %s, %s)")
    data_message = (userid, ticketid, message)
    create_record(add_message, data_message)


@app.post("/add-progress")
def create_progress(ticketid, statusid, technicianid, message=None):
    add_progress = ("INSERT INTO progress"
                    "(ticketID, statusID, technicianID, message)"
                    "VALUES (%s, %s, %s, %s)")
    data_progress = (ticketid, statusid, technicianid, message)
    create_record(add_progress, data_progress)


@app.get("/tickets/{userid}")
def get_user_tickets(userid):
    querystring = ("SELECT * "
                   "From ticket "
                   "WHERE userID = %s")
    data = (userid,)
    cursor.execute(querystring, data)
    result = cursor.fetchall()
    return result


@app.get("/ticket/{ticketid}")
def get_ticket(ticketid):
    querystring = ("SELECT * "
                   "From ticket "
                   "WHERE ticketID = %s")
    data = (ticketid,)
    cursor.execute(querystring, data)
    result = cursor.fetchone()
    return result


@app.get("/messages")
def get_ticket_messages(ticketid):
    querystring = ("SELECT * "
                   "FROM message "
                   "WHERE ticketID = %s")
    data = (ticketid,)
    load_record(querystring, data)


def create_record(add, data):
    cursor.execute(add, data)
    connection.commit()  # Make sure data is committed to the database


def load_record(querystring, data):
    cursor.execute(querystring, data)
    result = cursor.fetchall()
    return result
