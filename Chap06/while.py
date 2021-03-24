secret = 'password'
pw = ''
auth = False
count = 0 
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt:
        break
    if count == 3:
        continue
    
    pw = input("{} whats the secret word ".format(count))
else:
    auth = True

print("Authorized " if auth else "Calling the FBI...")