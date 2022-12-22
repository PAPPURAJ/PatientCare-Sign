import pyrebase

config = {
    "apiKey": "AIzaSyCpfYIfiC5-Wx3mvlHKHpsQXS0Mnpf99RU",
    "authDomain": "voiceautomation-8d4cc.firebaseapp.com",
    "databaseURL": "https://voiceautomation-8d4cc-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "voiceautomation-8d4cc",
    "storageBucket": "voiceautomation-8d4cc.appspot.com",
    "messagingSenderId": "284023033623",
    "appId": "1:284023033623:web:355627758869db40bb7152",
    "measurementId": "G-TZ4MD5JL9B"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database().child("Keya")

myd = '1'


def setdata(field, data):
    db.set({field: data})
    print("Light: ")
    print(data)
