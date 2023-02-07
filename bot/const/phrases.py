
def phrase_for_start_first_greeting(data):
    return "Hello, " + data["user_name"] + "!"

def phrase_for_answer_to_main_menu_buttons(data):
    return "You pressed " + data["button_title"]

def phrase_for_notify_admins_about_some_event(data):
    return "❗️" + data["user_name"] + " " + data["user_nickname"] + " что-то сделал в " + data["weekday"] + " <b>" + data["date"] + "</b> в <b>" + data["time"]