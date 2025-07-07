from secrets import token_urlsafe
import os

os.makedirs("secrets", exist_ok=True)

with open("secrets/db_pass.txt", "w") as f:
    f.write(token_urlsafe(512))

with open("secrets/casbin_login_pass.txt", "w") as f:
    f.write(token_urlsafe(512))