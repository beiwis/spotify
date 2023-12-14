### [Documentation](https://spotipy.readthedocs.io/en/2.22.1/)

- `add_to_queue`(_uri_, _device_id=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.add_to_queue "Permalink to this definition")
	Adds a song to the end of a user’s queue
	**Parameters** 
	- **uri** - song uri, id, or url
	- **device_id** - the id of a Spotify device.(**IGNORE**)

- `album`(_album_id_, _market=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.album "Permalink to this definition")
	returns a single album given the album’s ID, URIs or URL
	**Parameters**:
	- album_id - the album ID, URI or URL
	- market - an ISO 3166-1 alpha-2 country code

- `album_tracks`(_album_id_, _limit=50_, _offset=0_, _market=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.album_tracks "Permalink to this definition")
	Get Spotify catalog information about an album’s tracks
	**Parameters**:
	- album_id - the album ID, URI or URL
	- limit - the number of items to return
	- offset - the index of the first item to return
	- market - an ISO 3166-1 alpha-2 country code.

- `albums`(_albums_, _market=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.albums "Permalink to this definition")
	returns a list of albums given the album IDs, URIs, or URLs
	**Parameters**:
	- albums - a list of album IDs, URIs or URLs
	- market - an ISO 3166-1 alpha-2 country code

- `artist`(_artist_id_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.artist "Permalink to this definition")
	returns a single artist given the artist’s ID, URI or URL
	**Parameters**:
	- artist_id - an artist ID, URI or URL

- `artist_albums`(_artist_id_, _album_type=None_, _country=None_, _limit=20_, _offset=0_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.artist_albums "Permalink to this definition")
	Get Spotify catalog information about an artist’s albums
	**Parameters**:
	- artist_id - the artist ID, URI or URL
	- album_type - ‘album’, ‘single’, ‘appears_on’, ‘compilation’
	- country - limit the response to one particular country.
	- limit - the number of albums to return
	- offset - the index of the first album to return

- `artist_related_artists`(_artist_id_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.artist_related_artists "Permalink to this definition")
	Get Spotify catalog information about artists similar to an identified artist. Similarity is based on analysis of the Spotify community’s listening history.
	**Parameters**:
	- artist_id - the artist ID, URI or URL

`artist_top_tracks`(_artist_id_, _country='US'_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.artist_top_tracks "Permalink to this definition")

Get Spotify catalog information about an artist’s top 10 tracks by country.

Parameters:

- artist_id - the artist ID, URI or URL
- country - limit the response to one particular country.

`artists`(_artists_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.artists "Permalink to this definition")

returns a list of artists given the artist IDs, URIs, or URLs

Parameters:

- artists - a list of artist IDs, URIs or URLs

`audio_analysis`(_track_id_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.audio_analysis "Permalink to this definition")

Get audio analysis for a track based upon its Spotify ID Parameters:

> - track_id - a track URI, URL or ID

`audio_features`(_tracks=[]_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.audio_features "Permalink to this definition")

Get audio features for one or multiple tracks based upon their Spotify IDs Parameters:

> - tracks - a list of track URIs, URLs or IDs, maximum: 100 ids

`auth_manager`[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.auth_manager "Permalink to this definition")

`available_markets`()[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.available_markets "Permalink to this definition")

Get the list of markets where Spotify is available. Returns a list of the countries in which Spotify is available, identified by their ISO 3166-1 alpha-2 country code with additional country codes for special territories.

`categories`(_country=None_, _locale=None_, _limit=20_, _offset=0_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.categories "Permalink to this definition")

Get a list of categories

Parameters:

- country - An ISO 3166-1 alpha-2 country code.
- locale - The desired language, consisting of an ISO 639-1 alpha-2 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore.
- limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
- offset - The index of the first item to return. Default: 0 (the first object). Use with limit to get the next set of items.

`category`(_category_id_, _country=None_, _locale=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.category "Permalink to this definition")

Get info about a category

Parameters:

- category_id - The Spotify category ID for the category.
- country - An ISO 3166-1 alpha-2 country code.
- locale - The desired language, consisting of an ISO 639-1 alpha-2 language code and an ISO 3166-1 alpha-2 country code, joined by an underscore.

`category_playlists`(_category_id=None_, _country=None_, _limit=20_, _offset=0_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.category_playlists "Permalink to this definition")

Get a list of playlists for a specific Spotify category

Parameters:

- category_id - The Spotify category ID for the category.
- country - An ISO 3166-1 alpha-2 country code.
- limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
- offset - The index of the first item to return. Default: 0 (the first object). Use with limit to get the next set of items.

`country_codes`_= ['AD', 'AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'EC', 'SV', 'EE', 'FI', 'FR', 'DE', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'ID', 'IE', 'IT', 'JP', 'LV', 'LI', 'LT', 'LU', 'MY', 'MT', 'MX', 'MC', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'ES', 'SK', 'SE', 'CH', 'TW', 'TR', 'GB', 'US', 'UY']_[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.country_codes "Permalink to this definition")

`current_playback`(_market=None_, _additional_types=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_playback "Permalink to this definition")

Get information about user’s current playback.

Parameters:

- market - an ISO 3166-1 alpha-2 country code.
- additional_types - episode to get podcast track information

`current_user`()[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user "Permalink to this definition")

Get detailed profile information about the current user. An alias for the ‘me’ method.

`current_user_follow_playlist`(_playlist_id_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_follow_playlist "Permalink to this definition")

Add the current authenticated user as a follower of a playlist.

Parameters:

- playlist_id - the id of the playlist

`current_user_followed_artists`(_limit=20_, _after=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_followed_artists "Permalink to this definition")

Gets a list of the artists followed by the current authorized user

Parameters:

- limit - the number of artists to return
- after - the last artist ID retrieved from the previous
    
    request
    

`current_user_following_artists`(_ids=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_following_artists "Permalink to this definition")

Check if the current user is following certain artists

Returns list of booleans respective to ids

Parameters:

- ids - a list of artist URIs, URLs or IDs

`current_user_following_users`(_ids=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_following_users "Permalink to this definition")

Check if the current user is following certain users

Returns list of booleans respective to ids

Parameters:

- ids - a list of user URIs, URLs or IDs

`current_user_playing_track`()[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_playing_track "Permalink to this definition")

Get information about the current users currently playing track.

`current_user_playlists`(_limit=50_, _offset=0_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_playlists "Permalink to this definition")

Get current user playlists without required getting his profile Parameters:

> - limit - the number of items to return
> - offset - the index of the first item to return

`current_user_recently_played`(_limit=50_, _after=None_, _before=None_)[see docs](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_recently_played "Permalink to this definition")

Get the current user’s recently played tracks

Parameters:

- limit - the number of entities to return
- after - unix timestamp in milliseconds. Returns all items
    
    after (but not including) this cursor position. Cannot be used if before is specified.
    
- before - unix timestamp in milliseconds. Returns all items
    
    before (but not including) this cursor position. Cannot be used if after is specified
    

`current_user_saved_albums`(_limit=20_, _offset=0_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_albums "Permalink to this definition")

Gets a list of the albums saved in the current authorized user’s “Your Music” library

Parameters:

- limit - the number of albums to return (MAX_LIMIT=50)
- offset - the index of the first album to return
- market - an ISO 3166-1 alpha-2 country code.

`current_user_saved_albums_add`(_albums=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_albums_add "Permalink to this definition")

Add one or more albums to the current user’s “Your Music” library. Parameters:

> - albums - a list of album URIs, URLs or IDs

`current_user_saved_albums_contains`(_albums=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_albums_contains "Permalink to this definition")

Check if one or more albums is already saved in the current Spotify user’s “Your Music” library.

Parameters:

- albums - a list of album URIs, URLs or IDs

`current_user_saved_albums_delete`(_albums=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_albums_delete "Permalink to this definition")

Remove one or more albums from the current user’s “Your Music” library.

Parameters:

- albums - a list of album URIs, URLs or IDs

`current_user_saved_episodes`(_limit=20_, _offset=0_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_episodes "Permalink to this definition")

Gets a list of the episodes saved in the current authorized user’s “Your Music” library

Parameters:

- limit - the number of episodes to return
- offset - the index of the first episode to return
- market - an ISO 3166-1 alpha-2 country code

`current_user_saved_episodes_add`(_episodes=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_episodes_add "Permalink to this definition")

Add one or more episodes to the current user’s “Your Music” library.

Parameters:

- episodes - a list of episode URIs, URLs or IDs

`current_user_saved_episodes_contains`(_episodes=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_episodes_contains "Permalink to this definition")

Check if one or more episodes is already saved in the current Spotify user’s “Your Music” library.

Parameters:

- episodes - a list of episode URIs, URLs or IDs

`current_user_saved_episodes_delete`(_episodes=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_episodes_delete "Permalink to this definition")

Remove one or more episodes from the current user’s “Your Music” library.

Parameters:

- episodes - a list of episode URIs, URLs or IDs

`current_user_saved_shows`(_limit=20_, _offset=0_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_shows "Permalink to this definition")

Gets a list of the shows saved in the current authorized user’s “Your Music” library

Parameters:

- limit - the number of shows to return
- offset - the index of the first show to return
- market - an ISO 3166-1 alpha-2 country code

`current_user_saved_shows_add`(_shows=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_shows_add "Permalink to this definition")

Add one or more albums to the current user’s “Your Music” library. Parameters:

> - shows - a list of show URIs, URLs or IDs

`current_user_saved_shows_contains`(_shows=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_shows_contains "Permalink to this definition")

Check if one or more shows is already saved in the current Spotify user’s “Your Music” library.

Parameters:

- shows - a list of show URIs, URLs or IDs

`current_user_saved_shows_delete`(_shows=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_shows_delete "Permalink to this definition")

Remove one or more shows from the current user’s “Your Music” library.

Parameters:

- shows - a list of show URIs, URLs or IDs

`current_user_saved_tracks`(_limit=20_, _offset=0_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_tracks "Permalink to this definition")

Gets a list of the tracks saved in the current authorized user’s “Your Music” library

Parameters:

- limit - the number of tracks to return
- offset - the index of the first track to return
- market - an ISO 3166-1 alpha-2 country code

`current_user_saved_tracks_add`(_tracks=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_tracks_add "Permalink to this definition")

Add one or more tracks to the current user’s “Your Music” library.

Parameters:

- tracks - a list of track URIs, URLs or IDs

`current_user_saved_tracks_contains`(_tracks=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_tracks_contains "Permalink to this definition")

Check if one or more tracks is already saved in the current Spotify user’s “Your Music” library.

Parameters:

- tracks - a list of track URIs, URLs or IDs

`current_user_saved_tracks_delete`(_tracks=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_saved_tracks_delete "Permalink to this definition")

Remove one or more tracks from the current user’s “Your Music” library.

Parameters:

- tracks - a list of track URIs, URLs or IDs

`current_user_top_artists`(_limit=20_, _offset=0_, _time_range='medium_term'_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_top_artists "Permalink to this definition")

Get the current user’s top artists

Parameters:

- limit - the number of entities to return
- offset - the index of the first entity to return
- time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term

`current_user_top_tracks`(_limit=20_, _offset=0_, _time_range='medium_term'_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_top_tracks "Permalink to this definition")

Get the current user’s top tracks

Parameters:

- limit - the number of entities to return
- offset - the index of the first entity to return
- time_range - Over what time frame are the affinities computed Valid-values: short_term, medium_term, long_term

`current_user_unfollow_playlist`(_playlist_id_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.current_user_unfollow_playlist "Permalink to this definition")

Unfollows (deletes) a playlist for the current authenticated user

Parameters:

- name - the name of the playlist

`currently_playing`(_market=None_, _additional_types=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.currently_playing "Permalink to this definition")

Get user’s currently playing track.

Parameters:

- market - an ISO 3166-1 alpha-2 country code.
- additional_types - episode to get podcast track information

`default_retry_codes`_= (429, 500, 502, 503, 504)_[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.default_retry_codes "Permalink to this definition")

`devices`()[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.devices "Permalink to this definition")

Get a list of user’s available devices.

`episode`(_episode_id_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.episode "Permalink to this definition")

returns a single episode given the episode’s ID, URIs or URL

Parameters:

- episode_id - the episode ID, URI or URL
- market - an ISO 3166-1 alpha-2 country code.
    
    The episode must be available in the given market. If user-based authorization is in use, the user’s country takes precedence. If neither market nor user country are provided, the content is considered unavailable for the client.
    

`episodes`(_episodes_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.episodes "Permalink to this definition")

returns a list of episodes given the episode IDs, URIs, or URLs

Parameters:

- episodes - a list of episode IDs, URIs or URLs
- market - an ISO 3166-1 alpha-2 country code.
    
    Only episodes available in the given market will be returned. If user-based authorization is in use, the user’s country takes precedence. If neither market nor user country are provided, the content is considered unavailable for the client.
    

`featured_playlists`(_locale=None_, _country=None_, _timestamp=None_, _limit=20_, _offset=0_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.featured_playlists "Permalink to this definition")

Get a list of Spotify featured playlists

Parameters:

- locale - The desired language, consisting of a lowercase ISO 639-1 alpha-2 language code and an uppercase ISO 3166-1 alpha-2 country code, joined by an underscore.
- country - An ISO 3166-1 alpha-2 country code.
- timestamp - A timestamp in ISO 8601 format: yyyy-MM-ddTHH:mm:ss. Use this parameter to specify the user’s local time to get results tailored for that specific date and time in the day
- limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
- offset - The index of the first item to return. Default: 0 (the first object). Use with limit to get the next set of items.

`max_retries`_= 3_[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.max_retries "Permalink to this definition")

`me`()[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.me "Permalink to this definition")

Get detailed profile information about the current user. An alias for the ‘current_user’ method.

`new_releases`(_country=None_, _limit=20_, _offset=0_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.new_releases "Permalink to this definition")

Get a list of new album releases featured in Spotify

Parameters:

- country - An ISO 3166-1 alpha-2 country code.
- limit - The maximum number of items to return. Default: 20. Minimum: 1. Maximum: 50
- offset - The index of the first item to return. Default: 0 (the first object). Use with limit to get the next set of items.

`next`(_result_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.next "Permalink to this definition")

returns the next result given a paged result

Parameters:

- result - a previously returned paged result

`next_track`(_device_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.next_track "Permalink to this definition")

Skip user’s playback to next track.

Parameters:

- device_id - device target for playback

`pause_playback`(_device_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.pause_playback "Permalink to this definition")

Pause user’s playback.

Parameters:

- device_id - device target for playback

`playlist`(_playlist_id_, _fields=None_, _market=None_, _additional_types=('track'_, _)_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist "Permalink to this definition")

Gets playlist by id.

Parameters:

- playlist - the id of the playlist
- fields - which fields to return
- market - An ISO 3166-1 alpha-2 country code or the
    
    string from_token.
    
- additional_types - list of item types to return.
    
    valid types are: track and episode
    

`playlist_add_items`(_playlist_id_, _items_, _position=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_add_items "Permalink to this definition")

Adds tracks/episodes to a playlist

Parameters:

- playlist_id - the id of the playlist
- items - a list of track/episode URIs or URLs
- position - the position to add the tracks

`playlist_change_details`(_playlist_id_, _name=None_, _public=None_, _collaborative=None_, _description=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_change_details "Permalink to this definition")

Changes a playlist’s name and/or public/private state, collaborative state, and/or description

Parameters:

- playlist_id - the id of the playlist
- name - optional name of the playlist
- public - optional is the playlist public
- collaborative - optional is the playlist collaborative
- description - optional description of the playlist

`playlist_cover_image`(_playlist_id_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_cover_image "Permalink to this definition")

Get cover image of a playlist.

Parameters:

- playlist_id - the playlist ID, URI or URL

`playlist_is_following`(_playlist_id_, _user_ids_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_is_following "Permalink to this definition")

Check to see if the given users are following the given playlist

Parameters:

- playlist_id - the id of the playlist
- user_ids - the ids of the users that you want to check to see
    
    if they follow the playlist. Maximum: 5 ids.
    

`playlist_items`(_playlist_id_, _fields=None_, _limit=100_, _offset=0_, _market=None_, _additional_types=('track'_, _'episode')_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_items "Permalink to this definition")

Get full details of the tracks and episodes of a playlist.

Parameters:

- playlist_id - the playlist ID, URI or URL
- fields - which fields to return
- limit - the maximum number of tracks to return
- offset - the index of the first track to return
- market - an ISO 3166-1 alpha-2 country code.
- additional_types - list of item types to return.
    
    valid types are: track and episode
    

`playlist_remove_all_occurrences_of_items`(_playlist_id_, _items_, _snapshot_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_remove_all_occurrences_of_items "Permalink to this definition")

Removes all occurrences of the given tracks/episodes from the given playlist

Parameters:

- playlist_id - the id of the playlist
- items - list of track/episode ids to remove from the playlist
- snapshot_id - optional id of the playlist snapshot

`playlist_remove_specific_occurrences_of_items`(_playlist_id_, _items_, _snapshot_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_remove_specific_occurrences_of_items "Permalink to this definition")

Removes all occurrences of the given tracks from the given playlist

Parameters:

- playlist_id - the id of the playlist
    
- items - an array of objects containing Spotify URIs of the
    
    tracks/episodes to remove with their current positions in the playlist. For example:
    
    > [ { “uri”:”4iV5W9uYEdYUVa79Axb7Rh”, “positions”:[2] }, { “uri”:”1301WleyT98MSxVHPZCA6M”, “positions”:[7] } ]
    
- snapshot_id - optional id of the playlist snapshot
    

`playlist_reorder_items`(_playlist_id_, _range_start_, _insert_before_, _range_length=1_, _snapshot_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_reorder_items "Permalink to this definition")

Reorder tracks in a playlist

Parameters:

- playlist_id - the id of the playlist
- range_start - the position of the first track to be reordered
- range_length - optional the number of tracks to be reordered
    
    (default: 1)
    
- insert_before - the position where the tracks should be
    
    inserted
    
- snapshot_id - optional playlist’s snapshot ID

`playlist_replace_items`(_playlist_id_, _items_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_replace_items "Permalink to this definition")

Replace all tracks/episodes in a playlist

Parameters:

- playlist_id - the id of the playlist
- items - list of track/episode ids to comprise playlist

`playlist_tracks`(_playlist_id_, _fields=None_, _limit=100_, _offset=0_, _market=None_, _additional_types=('track'_, _)_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_tracks "Permalink to this definition")

Get full details of the tracks of a playlist.

Parameters:

- playlist_id - the playlist ID, URI or URL
- fields - which fields to return
- limit - the maximum number of tracks to return
- offset - the index of the first track to return
- market - an ISO 3166-1 alpha-2 country code.
- additional_types - list of item types to return.
    
    valid types are: track and episode
    

`playlist_upload_cover_image`(_playlist_id_, _image_b64_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_upload_cover_image "Permalink to this definition")

Replace the image used to represent a specific playlist

Parameters:

- playlist_id - the id of the playlist
- image_b64 - image data as a Base64 encoded JPEG image string
    
    (maximum payload size is 256 KB)
    

`previous`(_result_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.previous "Permalink to this definition")

returns the previous result given a paged result

Parameters:

- result - a previously returned paged result

`previous_track`(_device_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.previous_track "Permalink to this definition")

Skip user’s playback to previous track.

Parameters:

- device_id - device target for playback

`queue`()[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.queue "Permalink to this definition")

Gets the current user’s queue

`recommendation_genre_seeds`()[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.recommendation_genre_seeds "Permalink to this definition")

Get a list of genres available for the recommendations function.

`recommendations`(_seed_artists=None_, _seed_genres=None_, _seed_tracks=None_, _limit=20_, _country=None_, _**kwargs_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.recommendations "Permalink to this definition")

Get a list of recommended tracks for one to five seeds. (at least one of seed_artists, seed_tracks and seed_genres are needed)

Parameters:

- seed_artists - a list of artist IDs, URIs or URLs
- seed_tracks - a list of track IDs, URIs or URLs
- seed_genres - a list of genre names. Available genres for
    
    recommendations can be found by calling recommendation_genre_seeds
    
- country - An ISO 3166-1 alpha-2 country code. If provided,
    
    all results will be playable in this country.
    
- limit - The maximum number of items to return. Default: 20.
    
    Minimum: 1. Maximum: 100
    
- min/max/target_<attribute> - For the tuneable track
    
    attributes listed in the documentation, these values provide filters and targeting on results.
    

`repeat`(_state_, _device_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.repeat "Permalink to this definition")

Set repeat mode for playback.

Parameters:

- state - track, context, or off
- device_id - device target for playback

`search`(_q_, _limit=10_, _offset=0_, _type='track'_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.search "Permalink to this definition")

searches for an item

Parameters:

- q - the search query (see how to write a query in the
    
    official documentation [https://developer.spotify.com/documentation/web-api/reference/search/](https://developer.spotify.com/documentation/web-api/reference/search/)) # noqa
    
- limit - the number of items to return (min = 1, default = 10, max = 50). The limit is applied
    
    within each type, not on the total response.
    
- offset - the index of the first item to return
- type - the types of items to return. One or more of ‘artist’, ‘album’,
    
    ‘track’, ‘playlist’, ‘show’, and ‘episode’. If multiple types are desired, pass in a comma separated string; e.g., ‘track,album,episode’.
    
- market - An ISO 3166-1 alpha-2 country code or the string
    
    from_token.
    

`search_markets`(_q_, _limit=10_, _offset=0_, _type='track'_, _markets=None_, _total=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.search_markets "Permalink to this definition")

(experimental) Searches multiple markets for an item

Parameters:

- q - the search query (see how to write a query in the
    
    official documentation [https://developer.spotify.com/documentation/web-api/reference/search/](https://developer.spotify.com/documentation/web-api/reference/search/)) # noqa
    
- limit - the number of items to return (min = 1, default = 10, max = 50). If a search is to be done on multiple
    
    markets, then this limit is applied to each market. (e.g. search US, CA, MX each with a limit of 10).
    
- offset - the index of the first item to return
- type - the types of items to return. One or more of ‘artist’, ‘album’,
    
    ‘track’, ‘playlist’, ‘show’, or ‘episode’. If multiple types are desired, pass in a comma separated string.
    
- markets - A list of ISO 3166-1 alpha-2 country codes. Search all country markets by default.
- total - the total number of results to return if multiple markets are supplied in the search.
    
    If multiple types are specified, this only applies to the first type.
    

`seek_track`(_position_ms_, _device_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.seek_track "Permalink to this definition")

Seek to position in current track.

Parameters:

- position_ms - position in milliseconds to seek to
- device_id - device target for playback

`set_auth`(_auth_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.set_auth "Permalink to this definition")

`show`(_show_id_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.show "Permalink to this definition")

returns a single show given the show’s ID, URIs or URL

Parameters:

- show_id - the show ID, URI or URL
- market - an ISO 3166-1 alpha-2 country code.
    
    The show must be available in the given market. If user-based authorization is in use, the user’s country takes precedence. If neither market nor user country are provided, the content is considered unavailable for the client.
    

`show_episodes`(_show_id_, _limit=50_, _offset=0_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.show_episodes "Permalink to this definition")

Get Spotify catalog information about a show’s episodes

Parameters:

- show_id - the show ID, URI or URL
- limit - the number of items to return
- offset - the index of the first item to return
- market - an ISO 3166-1 alpha-2 country code.
    
    Only episodes available in the given market will be returned. If user-based authorization is in use, the user’s country takes precedence. If neither market nor user country are provided, the content is considered unavailable for the client.
    

`shows`(_shows_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.shows "Permalink to this definition")

returns a list of shows given the show IDs, URIs, or URLs

Parameters:

- shows - a list of show IDs, URIs or URLs
- market - an ISO 3166-1 alpha-2 country code.
    
    Only shows available in the given market will be returned. If user-based authorization is in use, the user’s country takes precedence. If neither market nor user country are provided, the content is considered unavailable for the client.
    

`shuffle`(_state_, _device_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.shuffle "Permalink to this definition")

Toggle playback shuffling.

Parameters:

- state - true or false
- device_id - device target for playback

`start_playback`(_device_id=None_, _context_uri=None_, _uris=None_, _offset=None_, _position_ms=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.start_playback "Permalink to this definition")

Start or resume user’s playback.

Provide a context_uri to start playback of an album, artist, or playlist.

Provide a uris list to start playback of one or more tracks.

Provide offset as {“position”: <int>} or {“uri”: “<track uri>”} to start playback at a particular offset.

Parameters:

- device_id - device target for playback
- context_uri - spotify context uri to play
- uris - spotify track uris
- offset - offset into context by index or track
- position_ms - (optional) indicates from what position to start playback.
    
    Must be a positive number. Passing in a position that is greater than the length of the track will cause the player to start playing the next song.
    

`track`(_track_id_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.track "Permalink to this definition")

returns a single track given the track’s ID, URI or URL

Parameters:

- track_id - a spotify URI, URL or ID
- market - an ISO 3166-1 alpha-2 country code.

`tracks`(_tracks_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.tracks "Permalink to this definition")

returns a list of tracks given a list of track IDs, URIs, or URLs

Parameters:

- tracks - a list of spotify URIs, URLs or IDs. Maximum: 50 IDs.
- market - an ISO 3166-1 alpha-2 country code.

`transfer_playback`(_device_id_, _force_play=True_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.transfer_playback "Permalink to this definition")

Transfer playback to another device. Note that the API accepts a list of device ids, but only actually supports one.

Parameters:

- device_id - transfer playback to this device
- force_play - true: after transfer, play. false:
    
    keep current state.
    

`user`(_user_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user "Permalink to this definition")

Gets basic profile information about a Spotify User

Parameters:

- user - the id of the usr

`user_follow_artists`(_ids=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_follow_artists "Permalink to this definition")

Follow one or more artists Parameters:

> - ids - a list of artist IDs

`user_follow_users`(_ids=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_follow_users "Permalink to this definition")

Follow one or more users Parameters:

> - ids - a list of user IDs

`user_playlist`(_user_, _playlist_id=None_, _fields=None_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist "Permalink to this definition")

`user_playlist_add_episodes`(_user_, _playlist_id_, _episodes_, _position=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_add_episodes "Permalink to this definition")

`user_playlist_add_tracks`(_user_, _playlist_id_, _tracks_, _position=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_add_tracks "Permalink to this definition")

`user_playlist_change_details`(_user_, _playlist_id_, _name=None_, _public=None_, _collaborative=None_, _description=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_change_details "Permalink to this definition")

`user_playlist_create`(_user_, _name_, _public=True_, _collaborative=False_, _description=''_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_create "Permalink to this definition")

Creates a playlist for a user

Parameters:

- user - the id of the user
- name - the name of the playlist
- public - is the created playlist public
- collaborative - is the created playlist collaborative
- description - the description of the playlist

`user_playlist_follow_playlist`(_playlist_owner_id_, _playlist_id_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_follow_playlist "Permalink to this definition")

Add the current authenticated user as a follower of a playlist.

Parameters:

- playlist_owner_id - the user id of the playlist owner
- playlist_id - the id of the playlist

`user_playlist_is_following`(_playlist_owner_id_, _playlist_id_, _user_ids_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_is_following "Permalink to this definition")

Check to see if the given users are following the given playlist

Parameters:

- playlist_owner_id - the user id of the playlist owner
- playlist_id - the id of the playlist
- user_ids - the ids of the users that you want to check to see
    
    if they follow the playlist. Maximum: 5 ids.
    

`user_playlist_remove_all_occurrences_of_tracks`(_user_, _playlist_id_, _tracks_, _snapshot_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_remove_all_occurrences_of_tracks "Permalink to this definition")

Removes all occurrences of the given tracks from the given playlist

Parameters:

- user - the id of the user
- playlist_id - the id of the playlist
- tracks - the list of track ids to remove from the playlist
- snapshot_id - optional id of the playlist snapshot

`user_playlist_remove_specific_occurrences_of_tracks`(_user_, _playlist_id_, _tracks_, _snapshot_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_remove_specific_occurrences_of_tracks "Permalink to this definition")

Removes all occurrences of the given tracks from the given playlist

Parameters:

- user - the id of the user
    
- playlist_id - the id of the playlist
    
- tracks - an array of objects containing Spotify URIs of the
    
    tracks to remove with their current positions in the playlist. For example:
    
    > [ { “uri”:”4iV5W9uYEdYUVa79Axb7Rh”, “positions”:[2] }, { “uri”:”1301WleyT98MSxVHPZCA6M”, “positions”:[7] } ]
    
- snapshot_id - optional id of the playlist snapshot
    

`user_playlist_reorder_tracks`(_user_, _playlist_id_, _range_start_, _insert_before_, _range_length=1_, _snapshot_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_reorder_tracks "Permalink to this definition")

Reorder tracks in a playlist from a user

Parameters:

- user - the id of the user
- playlist_id - the id of the playlist
- range_start - the position of the first track to be reordered
- range_length - optional the number of tracks to be reordered
    
    (default: 1)
    
- insert_before - the position where the tracks should be
    
    inserted
    
- snapshot_id - optional playlist’s snapshot ID

`user_playlist_replace_tracks`(_user_, _playlist_id_, _tracks_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_replace_tracks "Permalink to this definition")

Replace all tracks in a playlist for a user

Parameters:

- user - the id of the user
- playlist_id - the id of the playlist
- tracks - the list of track ids to add to the playlist

`user_playlist_tracks`(_user=None_, _playlist_id=None_, _fields=None_, _limit=100_, _offset=0_, _market=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_tracks "Permalink to this definition")

`user_playlist_unfollow`(_user_, _playlist_id_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlist_unfollow "Permalink to this definition")

Unfollows (deletes) a playlist for a user

Parameters:

- user - the id of the user
- name - the name of the playlist

`user_playlists`(_user_, _limit=50_, _offset=0_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_playlists "Permalink to this definition")

Gets playlists of a user

Parameters:

- user - the id of the usr
- limit - the number of items to return
- offset - the index of the first item to return

`user_unfollow_artists`(_ids=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_unfollow_artists "Permalink to this definition")

Unfollow one or more artists Parameters:

> - ids - a list of artist IDs

`user_unfollow_users`(_ids=[]_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.user_unfollow_users "Permalink to this definition")

Unfollow one or more users Parameters:

> - ids - a list of user IDs

`volume`(_volume_percent_, _device_id=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.volume "Permalink to this definition")

Set playback volume.

Parameters:

- volume_percent - volume between 0 and 100
- device_id - device target for playback

_exception_`spotipy.client.``SpotifyException`(_http_status_, _code_, _msg_, _reason=None_, _headers=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.SpotifyException "Permalink to this definition")

Bases: `exceptions.Exception`

`__init__`(_http_status_, _code_, _msg_, _reason=None_, _headers=None_)[](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.SpotifyException.__init__ "Permalink to this definition")

x.__init__(…) initializes x; see help(type(x)) for signature