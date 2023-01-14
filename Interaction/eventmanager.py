# Event Manager
# FILE - eventmanager.py
# DESC - Event manager file to store and execute events across application

if __name__ == "__main__":
    print("🔴 Root import only module")
    exit()

events = {}

def register_event(event:str, func):
    if events.get(event) is None:
        events[event] = func
    else:
        print("Event name has already been registered")
    

def call_event(event:str, header:list, data:list):
    if events.get(event) is not None:
        events[event](header, data)
    else:
        print("Event name has not been registered and cannot be called")


# Instructions:
# To register a new event use the register_event function
# Pass a unique event name and a function that will be executed when the event is called
# The function must follow the template function(header list, data list)
# How the function handles the header and data can be handled at the function definition

# To call a function use the call_event function with the event string, header and data arguments