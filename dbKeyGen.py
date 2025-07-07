from secrets import token_urlsafe
with open('secrets/db_pass.txt','w') as file:
    file.write(token_urlsafe(512))
