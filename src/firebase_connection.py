import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

CREDENTIAL_PATH = "credentials.json"

credentialsCertificate = credentials.Certificate(CREDENTIAL_PATH)
firebase_admin.initialize_app(credentialsCertificate)
database = firestore.client()

if database:
	print("DEBUG : Connected to database successfully!")

def insertData(sensorValues):
	smokeSensor = sensorValues["smokeSensor"]
	motionSensor = sensorValues["motionSensor"]
	moistureSensor = sensorValues["moistureSensor"]
	dhtSensor = sensorValues["dhtSensor"]
	collection = database.collection("sensorData")
	collection.document("smokeSensor").update(smokeSensor)
	collection.document("motionSensor").update(motionSensor)
	collection.document("moistureSensor").update(moistureSensor)
	collection.document("dhtSensor").update(dhtSensor)