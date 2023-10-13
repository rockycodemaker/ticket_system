import mysql.connector
from mysql.connector import Error


# initialize connection to database server
def init(address, database, username, password, port = 3306):

    try:
        connection = mysql.connector.connect(host=address,
                                             port=port,
                                             database=database,
                                             user=username,
                                             password=password)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return {"success": True, "connection": connection}
        else:
            return {"success": False}

    except Error as e:
        print("Error while connecting to MySQL", e)
        return {"success": False}


def close(connection):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


def create_user(connection, username, email, password):
    add_user = ("INSERT INTO user"
                "(username, password, email)"
                "VALUES (%s, %s, %s)")
    data_user = (username, password, email)
    create_record(connection, add_user, data_user)


def create_ticket(connection, userid, issue, categoryid):
    add_ticket = ("INSERT INTO ticket"
                  "(issueDescription, userID, categoryID)"
                  "VALUES (%s, %s, %s)")
    data_ticket = (issue, userid, categoryid)
    create_record(connection, add_ticket, data_ticket)


def create_message(connection, userid, ticketid, message=None):
    add_message = ("INSERT INTO message"
                   "(userID, ticketID, message)"
                   "VALUES (%s, %s, %s)")
    data_message = (userid, ticketid, message)
    create_record(connection, add_message, data_message)


def create_progress(connection, ticketid, statusid, technicianid, message=None):
    add_progress = ("INSERT INTO progress"
                    "(ticketID, statusID, technicianID, message)"
                    "VALUES (%s, %s, %s, %s)")
    data_progress = (ticketid, statusid, technicianid, message)
    create_record(connection, add_progress, data_progress)


def get_user_tickets(connection, userid):
    querystring = ("SELECT * "
                   "From ticket "
                   "WHERE userID = %s")
    data = (userid,)
    return load_record(connection, querystring, data)


def get_ticket_messages(connection, ticketid):
    querystring = ("SELECT * "
                   "FROM message "
                   "WHERE ticketID = %s")
    data = (ticketid,)
    load_record(connection, querystring, data)


def create_record(connection, add, data):
    cursor = connection.cursor()
    cursor.execute(add, data)
    cursor.close()
    connection.commit()  # Make sure data is committed to the database


def load_record(connection, querystring, data):
    cursor = connection.cursor()
    cursor.execute(querystring, data)
    result = cursor.fetchall()
    cursor.close()
    return result
