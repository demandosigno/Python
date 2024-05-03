import http.client

conn = http.client.HTTPSConnection('www.python.org')
conn.request('GET', '/downloads/')
response = conn.getresponse()
# print(response.getheaders())
text = response.read().decode('UTF-8')
print(text)
conn.close()