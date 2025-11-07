test_settings = {'Theme': 'dark', 'Notifications': 'enabled','Volume':'high'}

def add_setting(settings, key_value_pair):
    key, value= key_value_pair
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    if key not in settings:
        settings.update({key:value})
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, key_value_pair):
    key, value = key_value_pair
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        settings.update({key:value})
        return f"Setting '{key}' updated to '{value}' successfully!"

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key_value_pair):
    key = str(key_value_pair).lower()

    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    
    else:
        return "Setting not found!"

def view_settings(settings):
    if len(settings) == 0:
        return "No settings available."
    
    else:
        entries = ""
        for key, value in settings.items():
            entries += f"\n{key.capitalize()}: {value}" 
        return f"Current User Settings:{entries}\n" 



print(add_setting({'theme': 'light'}, ('THEME', 'dark')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(update_setting({'theme': 'light'}, ('theme', 'dark')))
print(update_setting({'theme': 'light'}, ('volume', 'high')))
print(delete_setting({'theme': 'light'}, 'theme'))
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
