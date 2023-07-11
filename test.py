import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "deutschHallo/bill")
# response = requests.get(BASE + "deutschHallo/bill/21")
# response = requests.post(BASE + "deutschHallo/bill")
# response = requests.post(BASE + "deutschHallo")

# response = requests.put(BASE+"video/1", {"likes":10,"name":"MyFirstVideo","views":30})
# print(response.json())

# input( ) #used to pause

# response = requests.put(BASE+"video/1", {"likes":10,"name":"MyFirstVideo","views":30})
# print(response.json())

# input( ) #used to pause

# response = requests.get(BASE+"video/1")
# print(response.json())

# input( ) #used to pause

# response = requests.delete(BASE+"video/1")

# input( ) #used to pause

# response = requests.get(BASE+"video/1")
# print(response.json())

data = [
    {"likes":20,"views":300,"name":"video1"},
    {"likes":30,"views":500,"name":"video2"},
    {"likes":40,"views":200,"name":"video3"},
    
]

# for i in range(len(data)):
#     response = requests.put(BASE+"video/"+str(i),data[i])
#     print(response.json())


# input()
response1 = requests.get(BASE+"video/2")
response2 = requests.get(BASE+"video/1")
response3 = requests.get(BASE+"video/0")
response4 = requests.get(BASE+"video/849494")

print(response1.json())
print(response2.json())
print(response3.json())
print(response4.json())


