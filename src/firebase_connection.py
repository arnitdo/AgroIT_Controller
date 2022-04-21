import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

CREDENTIAL_PATH = "../credentials.json"

credentialsCertificate = credentials.Certificate(CREDENTIAL_PATH)
firebase_admin.initialize_app(credentialsCertificate)

database = firestore.client()

def insertData(sensorValues):
	smokeSensor = sensorValues["smokeSensor"]
	motionSensor = sensorValues["motionSensor"]
	moistureSensor = sensorValues["moistureSensor"]
	dhtSensor = sensorValues["dhtSensor"]
	collection = database.collection("sensorData")
	collection.document("smokeSensor").set(smokeSensor)
	collection.document("motionSensor").set(motionSensor)
	