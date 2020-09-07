import http.client

conn = http.client.HTTPConnection("fx,cp2y,com")

payload = ""

headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "b0ddf855-5fb1-4e1d-88c8-ba525e8b832e,48e5fbe9-74b2-48e0-bd46-b1bca9c154f2",
    'Host': "fx.cp2y.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

conn.request("GET", "data,issue_number%21.jsp", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))