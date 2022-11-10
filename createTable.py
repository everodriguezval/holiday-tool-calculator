from sqlConnect import cursor

cursor.execute(
    """ 
CREATE TABLE "holiday" (
	"countryID"	INTEGER NOT NULL UNIQUE,
    "country" TEXT,
	"index"	REAL,
	"flight_cost" INTEGER,
    "food_low" INTEGER,
    "food_mid"	INTEGER,
    "food_high"	INTEGER,
    "accommodation_low"	INTEGER,
    "accommodation_mid"	INTEGER,
    "accommodation_high" INTEGER,
    "activities_low" INTEGER,
    "activities_mid" INTEGER,	
    "activities_high" INTEGER,
	PRIMARY KEY("countryID" AUTOINCREMENT)
)"""
)

