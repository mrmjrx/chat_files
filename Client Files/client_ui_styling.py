"""Config file for the client's UI.  Has variables describing text, and functions to style text correctly.  Also handles
the styling options from the ui_config.json file."""

TEXT_BROWSER_START = \
    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" \
    "p, li { white-space: pre-wrap; }\n" \
    "</style></head><body style=\" font-size:16pt; font-weight:400; " \
    "font-style:normal;\">\n"
TEXT_BROWSER_ITEM_START = "<p style=\" margin: 0; -qt-block-indent:0; text-indent:0px;\">"
TEXT_BROWSER_ITEM_END = "</p><\n>"
TEXT_BROWSER_END = "</body></html>"

ui_config_filepath = "ui_config.json"


def style_text_browser(messages: list, style_start=TEXT_BROWSER_START, style_end=TEXT_BROWSER_END,
                       style_item_start=TEXT_BROWSER_ITEM_START, style_item_end=TEXT_BROWSER_ITEM_END):
    """Returns the desired text browser (HTML) for the list of messages. Messages should be in the form of
    [User] Message
    [Another User] Message
    [Server] Server Message"""
    msg_text = ""
    for msg in [n.strip() for n in messages]:  # For every message in (stripped) messages
        name_text_segments = msg.split("]")  # Split by ] (this is to signal the end of the name section)
        if len(name_text_segments) != 1:  # If there is less than 2 entries in the list (meaning there was no ])
            msg_text += f"{style_item_start}<b>{name_text_segments[0]}]</b> {name_text_segments[1].strip()}" \
                        f"{style_item_end}\n"
        else:
            msg_text += f"{style_item_start}<b>{msg.strip()}"
    return f"{style_start}{msg_text}{style_end}"


def load_ui_config():
    import json
    with open(ui_config_filepath, "r") as file:
        return json.load(file)


def get_style_sheets(config: dict) -> dict:
    style_sheets = {'primary_col': f"background-color: {config['primary_col']['bg']};"
                                   f"color: {config['primary_col']['text']};"
                                   f"border: none; outline: none;",
                    'secondary_col': f"background-color: {config['secondary_col']['bg']};"
                                     f"color: {config['secondary_col']['text']};"
                                     f"border: hidden; outline: none;"}
    return style_sheets


if __name__ == '__main__':
    load_ui_config()
