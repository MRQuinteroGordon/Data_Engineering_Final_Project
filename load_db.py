import csv
import db_connect
import math


connection = db_connect.connect2db()
con = connection[0]
cur = connection[1]

# cur.execute("select * from streamHistory limit 10;")
# results = cur.fetchone()
# print(results)

# Streaming history columns are: 
# index,artistName,trackName,minutesPlayed,trackId,streamingDate
with open('transformed_data/transformed_stream_hist.csv', 'r') as file:
    heading = next(file)
    reader = csv.reader(file)
    # count = 0
    for row in reader:
        artistName = row[1]
        trackName = row[2]
        minutesPlayed = row[3]
        trackId = row[4]
        streamingDate = row[5]
        
        parameters = (trackId, streamingDate, artistName, trackName, minutesPlayed)
        insert_query = "insert into spotify_weather.streamHistory(spotifyTrackId, streamingDate, artistName, trackName, minutesPlayed) values (%s, %s, %s, %s, %s)"
        cur.execute(insert_query, parameters)
con.commit()

# Audio Feature columns are:
# index,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,type,id,length_in_minutes,time_signature
with open('transformed_data/transformed_audio_features.csv', 'r') as file:
    heading = next(file)
    reader = csv.reader(file)
    # count = 0
    for row in reader:
        danceability = float(row[1])
        energy = float(row[2])
        keySig = row[3]
        loudness = float(row[4])
        scaleMode = row[5]
        speechiness = float(row[6])
        acousticness = float(row[7])
        instrumentalness = float(row[8])
        liveness = float(row[9])
        valence = float(row[10])
        tempo = float(row[11])
        infoType = row[12]
        trackId = row[13]
        length = row[14]
        timeSig = row[15]
        
        parameters = (trackId, danceability, energy, keySig, scaleMode, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, length, timeSig)
        insert_query = "insert into spotify_weather.audioFeatures(spotifyTrackId, danceability, energy, keySig, scaleMode, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, lengthInMinutes, timeSignature) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(insert_query, parameters)
        
con.commit()

# Weather columns are:
# index,date,cloud_coverage,humidity,precipitation_total,min_temperature,max_temperature,barometric_pressure,wind_max_speed,wind_direction
with open('transformed_data/transformed_weather.csv', 'r') as file:
    heading = next(file)
    reader = csv.reader(file)
    # count = 0
    for row in reader:
        date = row[1]
        cloud_coverage = row[2]
        humidity = row[3]
        precipitation = float(row[4])
        min_temp = float(row[5])
        max_temp = float(row[6])
        barometric = row[7]
        wind_max = float(row[8])
        wind_direction = row[9]
        
        parameters = (date, cloud_coverage, humidity, precipitation, min_temp, max_temp, barometric, wind_max, wind_direction)
        insert_query = "insert into spotify_weather.dailyWeather(date, cloudCoverage, humidity, precipitationTotal, minTemp, maxTemp, barometricPressure, windMaxSpeed, windDirection) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(insert_query, parameters)
        
con.commit()


con.close()
