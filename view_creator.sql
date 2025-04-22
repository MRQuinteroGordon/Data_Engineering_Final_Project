-- view of streaming history with audio features
create view streaming_history_features as
	select sh.spotifyTrackId, sh.streamingDate, sh.artistName, sh.trackName, af.danceability, af.energy, af.keySig, af.scaleMode, af.loudness, af.speechiness, af.acousticness, af.instrumentalness, af.liveness, af.valence, af.tempo, af.lengthInMinutes, af.timeSignature
	from streamHistory sh inner join audioFeatures af on sh.spotifyTrackId = af.spotifyTrackID;
-- view of streaming history with audio features via a left join
create view streaming_history_features_lj as
	select sh.spotifyTrackId, sh.streamingDate, sh.artistName, sh.trackName, af.danceability, af.energy, af.keySig, af.scaleMode, af.loudness, af.speechiness, af.acousticness, af.instrumentalness, af.liveness, af.valence, af.tempo, af.lengthInMinutes, af.timeSignature
	from streamHistory sh left join audioFeatures af on sh.spotifyTrackId = af.spotifyTrackID;
-- view of all three data sets combined together
create view weather_and_music as
	select streaming_history_features.*, dailyWeather.*
    from streaming_history_features inner join dailyWeather on streaming_history_features.streamingDate = dailyWeather.date;