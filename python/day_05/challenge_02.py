## 2. Micro Challenge: The safe vault

## Goal: create a dictionary user = {"id": 1}. try to access user["email"]. then try to access it safely
## Contraint: use.get()

user = {"id": 1}

# email_ = user["email"]  ## it will raise an error if the key is missing

email = user.get("email") ## .get() method won't raise an error even if the key is missing.
print(email)
