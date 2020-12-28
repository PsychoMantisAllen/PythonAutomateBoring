import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)     # to check the status if accessible or not

# doing some general checks
print(len(res.text))

# check download status, return nothing if succeed otherwise raise an error
res.raise_for_status()
badRes = requests.get('http://automatetheboringstuff.com/abijiofdjsioeaj')
badRes.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)   # saving the text file in chunks, specifying one chunk to be 100,000 bytes

playFile.close()

