import json

from facebook.api import FacebookApi


def _update_button_type(buttonJson):
    buttonJson['type'] = "postback"
    return buttonJson

def _update_button_type_in_element(elementJson):
    if 'buttons' in elementJson:
        buttons = elementJson['buttons']
        postback_buttons = map(_update_button_type, buttons)
        elementJson['buttons'] = postback_buttons
    return elementJson

def response_text(text):
    return json.dumps({"text": text})

def response_buttons(text, buttons):
    postback_buttons = map(_update_button_type, buttons)
    return json.dumps({
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "button",
                "text": text,
                "buttons": postback_buttons
            }
        }
    })

def response_elements(elements):
    postback_elements = map(_update_button_type_in_element, elements)
    return json.dumps({
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": postback_elements
            }
        }
    })

def send_greeting_text_config():
    api = FacebookApi()
    response = json.dumps({
        "setting_type":"greeting",
        "greeting": {
            "text": "Hi {{user_first_name}}. I am a Prayer helper bot."
        }
    })
    api.post("/me/thread_settings", response)