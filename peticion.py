import http.client

conn = http.client.HTTPSConnection("exercise-db-fitness-workout-gym.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "56f3d0b7fcmsh75ef5de6ca3d2d1p1f2f10jsn7d8f28fb8c6c",
    'x-rapidapi-host': "exercise-db-fitness-workout-gym.p.rapidapi.com"
}

conn.request("GET", "/exercises/muscle/chest", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
