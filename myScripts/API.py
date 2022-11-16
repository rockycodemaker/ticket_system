import dbaccess as db


def api_call(call):
    result = db.init(address="localhost", database="ticketjk", username="root", password="admin")
    if result["success"]:
        connection = result["connection"]

        # the API options:
        if call == "register_user":
            # action
            db.create_user(connection=connection,
                           username="Jim",
                           email="jim_kerver@live.nl",
                           password="admin")
            print("user created")
        elif call == "create_ticket":
            db.create_ticket(connection=connection,
                             userid=4,
                             issue="test issue",
                             categoryid=1)
            print("created new ticket")
        elif call == "new_message":
            db.create_message(connection=connection,
                              userid=4,
                              ticketid=5,
                              message="Hello there, how is the test ticket coming along?"
                              )
            print("created new message")
        elif call == "update_status":
            db.create_progress(connection=connection,
                               ticketid=5,
                               technicianid=4,
                               statusid=1,
                               message="I have updated this status for testing purposes")
            print("fake update status")
        elif call == "get_tickets":
            tickets = db.get_user_tickets(connection=connection,
                                          userid=4)
            print(tickets)
        elif call == "get_messages":
            messages = db.get_ticket_messages(connection=connection,
                                              ticketid=5)
            print(messages)
        else:
            print("'{}' is not a valid request".format(call))

        db.close(connection)
