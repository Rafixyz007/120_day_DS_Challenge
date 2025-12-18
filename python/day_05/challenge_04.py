## 4. Micro Challenge: The Database Merger

## Goal: you have two dictionaries: defaults = {"theme": "light", "audio": "on"} and user_pref = {"theme": "dark"}. merge them so user_pref overrides defaults.
## Constraint: use the update operator

defaults = {"theme": "light", "audio":"on"}
user_pref = {"theme": "dark"}

user_pref.update(defaults)
print(user_pref)