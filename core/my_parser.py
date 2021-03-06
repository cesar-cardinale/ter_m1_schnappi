import xml.dom.minidom as xml
from model.action import Action


def parse(file_path):
    doc = xml.parse(file_path)
    events = doc.getElementsByTagName("event")
    all_actions = []
    for event in events:
        action_index = events.index(event)
        action_type = event.getAttribute("type")
        action_time = get_text(event.getElementsByTagName("time")[0].childNodes)
        action_text = get_text(event.getElementsByTagName("text")[0].childNodes)
        action_position = int(get_text(event.getElementsByTagName("pos")[0].childNodes))

        my_action = Action(action_index, action_type, action_time, action_text, action_position)
        all_actions.append(my_action)

        my_action.to_cli()
    return all_actions


def get_text(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    text = ''.join(rc)
    return unescape(text)


def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&#xa;", "\n")
    s = s.replace("&amp;", "&")
    return s
