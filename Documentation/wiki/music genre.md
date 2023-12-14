## Definition
In 1982, [Franco Fabbri](https://en.wikipedia.org/wiki/Franco_Fabbri "Franco Fabbri") proposed a definition of the musical genre that is now considered to be normative: ([[Categorical Conventions in Music Discourse Style and Genre.pdf]]) "musical genre is a set of musical events (real or possible) whose course is governed by a definite set of socially accepted rules", where a musical event be defined as "any type of activity performed around any type of event involving sound".[5](https://en.wikipedia.org/wiki/Music_genre#cite_note-:2-5)

A music genre or subgenre may be defined by the [[musical techniques]], the cultural context, and the content and spirit of the themes. Geographical origin is sometimes used to identify a music genre, though a single geographical category will often include a wide variety of subgenres. Timothy Laurie argues that, since the early 1980s, "genre has graduated from being a subset of popular music studies to being an almost ubiquitous framework for constituting and evaluating musical research objects".[6](https://en.wikipedia.org/wiki/Music_genre#cite_note-6)

The term _genre_ is generally defined similarly by many authors and musicologists, while the related term _style_ has different interpretations and definitions. Some, like [Peter van der Merwe](https://en.wikipedia.org/wiki/Peter_van_der_Merwe_(musicologist) "Peter van der Merwe (musicologist)"), treat the terms _genre_ and _style_ as the same, saying that _genre_ should be defined as pieces of music that share a certain style or "basic musical language".[7](https://en.wikipedia.org/wiki/Music_genre#cite_note-Pete-7) Others, such as Allan F. Moore, state that _genre_ and _style_ are two separate terms, and that secondary characteristics such as subject matter can also differentiate between genres.([[Categorical Conventions in Music Discourse Style and Genre.pdf]])
## How they were chosen:
to identify genders, we first have to make a list of all the available options, to do this, we're using the ones Spotify uses in it's API:

_using the [spotify.recommendation_genre_seeds() function](https://developer.spotify.com/documentation/web-api/reference/get-recommendation-genres):_

```{'genres': ['acoustic', 'afrobeat', 'alt-rock', 'alternative', 'ambient', 'anime', 'black-metal', 'bluegrass', 'blues', 'bossanova', 'brazil', 'breakbeat', 'british', 'cantopop', 'chicago-house', 'children', 'chill', 'classical', 'club', 'comedy', 'country', 'dance', 'dancehall', 'death-metal', 'deep-house', 'detroit-techno', 'disco', 'disney', 'drum-and-bass', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo', 'folk', 'forro', 'french', 'funk', 'garage', 'german', 'gospel', 'goth', 'grindcore', 'groove', 'grunge', 'guitar', 'happy', 'hard-rock', 'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'holidays', 'honky-tonk', 'house', 'idm', 'indian', 'indie', 'indie-pop', 'industrial', 'iranian', 'j-dance', 'j-idol', 'j-pop', 'j-rock', 'jazz', 'k-pop', 'kids', 'latin', 'latino', 'malay', 'mandopop', 'metal', 'metal-misc', 'metalcore', 'minimal-techno', 'movies', 'mpb', 'new-age', 'new-release', 'opera', 'pagode', 'party', 'philippines-opm', 'piano', 'pop', 'pop-film', 'post-dubstep', 'power-pop', 'progressive-house', 'psych-rock', 'punk', 'punk-rock', 'r-n-b', 'rainy-day', 'reggae', 'reggaeton', 'road-trip', 'rock', 'rock-n-roll', 'rockabilly', 'romance', 'sad', 'salsa', 'samba', 'sertanejo', 'show-tunes', 'singer-songwriter', 'ska', 'sleep', 'songwriter', 'soul', 'soundtracks', 'spanish', 'study', 'summer', 'swedish', 'synth-pop', 'tango', 'techno', 'trance', 'trip-hop', 'turkish', 'work-out', 'world-music']}```

However, this are not all the genres that we can find in Spotify, and there are some major genres are missing from this list, for example, rap or trap, and more specific genres that are relevant to me personally like trash-metal or riot grrrl.

To complete the list, I was divided between three different resources:
- [musicgenrelist.com](https://www.musicgenreslist.com/)
	This website was started as a hobby and has been completed for years by crowdsourcing, contains **976** genres so that it's specific enough but also not too many as to feel overwhelmed by them, the most interesting aspect is that they are classified into general genres. However the last update was done on December 2018.
- [[everynoise.com]]
	This website, updated often, tracks (25/11/2023) **6293** musical genres, taken from Spotify's artist's genre tags, this would be the best solution (accuracy wise), however it would be very difficult to implement this in any user friendly way
- [Spotify Genres (github.com)](https://gist.github.com/andytlr/4104c667a62d8145aa3a)
	This list was composed 8 years ago, and for that reason is not as reliable, however they are all actual genres that exist on Spotify and there are **1383** of them which is a much more manageable dataset to filter through. 

To make the classification procedure easier, I've placed all this genres into main global genres, based on the [musicgenrelist.com](https://www.musicgenreslist.com/) classification, using the Every Noise at Once list of all genres and filtering by popularity, tracking only the 1350 most popular genres:

`{'genres' :['pop', 'rap', 'rock', 'urbano latino', 'hip hop', 'trap latino', 'dance pop', 'reggaeton', 'pop rap', 'modern rock', 'pov  indie', 'musica mexicana', 'latin pop', 'classic rock', 'permanent wave', 'filmi', 'trap', 'alternative metal', 'k pop', 'r b', 'corrido', 'canadian pop', 'norteno', 'sierreno', 'soft rock', 'album rock', 'pop dance', 'sad sierreno', 'edm', 'hard rock', 'contemporary country', 'mellow gold', 'melodic rap', 'uk pop', 'banda', 'modern bollywood', 'alternative rock', 'corridos tumbados', 'post grunge', 'sertanejo universitario', 'nu metal', 'country', 'atl hip hop', 'art pop', 'urban contemporary', 'sertanejo', 'southern hip hop', 'singer songwriter', 'reggaeton colombiano', 'french hip hop', 'arrocha', 'alt z', 'country road', 'canadian hip hop', 'colombian pop', 'mexican pop', 'j pop', 'singer songwriter pop', 'ranchera', 'indonesian pop', 'new wave pop', 'german hip hop', 'pop urbaine', 'indietronica', 'soul', 'rock en espanol', 'latin alternative', 'gangster rap', 'k pop boy group', 'latin arena pop', 'italian pop', 'chicago rap', 'heartland rock', 'k pop girl group', 'latin hip hop', 'agronejo', 'modern country pop', 'electro house', 'neo mellow', 'canadian contemporary r b', 'latin rock', 'pop punk', 'pop rock', 'punjabi pop', 'new wave', 'new romantic', 'adult standards', 'rap metal', 'uk dance', 'trap argentino', 'modern alternative rock', 'slap house', 'indie pop', 'indie rock', 'conscious hip hop', 'house', 'folk rock', 'italian hip hop', 'east coast hip hop', 'turkish pop', 'metal', 'modern country rock', 'desi pop', 'bedroom pop', 'hoerspiel', 'afrobeats', 'post teen pop', 'neo soul', 'viral pop', 'sped up', 'cloud rap', 'talent show', 'spanish pop', 'puerto rican pop', 'opm', 'grupera', 'west coast rap', 'punk', 'alternative r b', 'boy band', 'german pop', 'psychedelic rock', 'glam metal', 'stomp and holler', 'ccm', 'miami hip hop', 'rage rap', 'desi hip hop', 'tropical', 'argentine rock', 'hip pop', 'sertanejo pop', 'glam rock', 'nigerian pop', 'funk carioca', 'detroit hip hop', 'argentine hip hop', 'dark trap', 'vocal jazz', 'piano rock', 'latin viral pop', 'underground hip hop', 'country rock', 'synthpop', 'italian adult pop', 'mexican hip hop', 'progressive electro house', 'metropopolis', 'indie folk', 'garage rock', 'classical', 'progressive house', 'europop', 'yacht rock', 'art rock', 'mpb', 'pagode', 'urbano espanol', 'chamber pop', 'dance rock', 'tropical house', 'j rock', 'anime', 'polish hip hop', 'rap francais', 'folk', 'lounge', 'disco', 'sleep', 'british soul', 'australian pop', 'pluggnb', 'trap brasileiro', 'metalcore', 'christian music', 'forro', 'big room', 'swedish pop', 'gen z singer songwriter', 'uk hip hop', 'reggaeton flow', 'electropop', 'classic oklahoma country', 'contemporary r b', 'mexican rock', 'british invasion', 'pop nacional', 'indie soul', 'white noise', 'folk pop', 'french pop', 'pagode novo', 'soundtrack', 'funk metal', 'emo rap', 'grunge', 'salsa', 'rain', 'r b francais', 'lgbtq  hip hop', 'turkish rock', 'dirty south rap', 'memphis hip hop', 'trap italiana', 'mariachi', 'brostep', 'easy listening', 'classic soul', 'funk mtg', 'trap triste', 'blues rock', 'melancholia', 'pop soul', 'brazilian gospel', 'alternative hip hop', 'outlaw country', 'melodic metalcore', 'turkish hip hop', 'orchestral soundtrack', 'dutch house', 'queens hip hop', 'motown', 'christian alternative rock', 'quiet storm', 'mandopop', 'electronica', 'pixel', 'dfw rap', 'worship', 'funk', 'rock and roll', 'otacore', 'new orleans rap', 'pop reggaeton', 'japanese teen pop', 'brazilian hip hop', 'gruperas inmortales', 'dream pop', 'rap conscient', 'indie poptimism', 'funk rock', 'bolero', 'australian dance', 'g funk', 'bachata', 'progressive rock', 'barbadian pop', 'neon pop punk', 'eurodance', 'emo', 'hardcore hip hop', 'neo synthpop', 'funk paulista', 'brazilian rock', 'trap boricua', 'cantautor', 'chanson', 'indonesian pop rock', 'pop venezolano', 'florida rap', 'kleine hoerspiel', 'drift phonk', 'bedroom r b', 'latin christian', 'russian hip hop', 'spanish hip hop', 'movie tunes', 'cali rap', 'urbano chileno', 'dancehall', 'children s music', 'color noise', 'trap queen', 'brooklyn drill', 'classic texas country', 'world worship', 'sheffield indie', 'rockabilly', 'escape room', 'modern indie pop', 'anime rock', 'plugg', 'shoegaze', 'funk rj', 'reggae fusion', 'pop argentino', 'britpop', 'australian rock', 'brooklyn indie', 'baroque pop', 'industrial metal', 'merseybeat', 'tamil pop', 'turkish trap', 'lilith', 'r b en espanol', 'trance', 'sophisti pop', 'thai pop', 'downtempo', 'southern rock', 'tamil hip hop', 'indian instrumental', 'candy pop', 'country dawn', 'girl group', 'polish trap', 'punjabi hip hop', 'compositional ambient', 'old school thrash', 'socal pop punk', 'classic bollywood', 'atl trap', 'uk contemporary r b', 'dark r b', 'instrumental lullaby', 'symphonic rock', 'north carolina hip hop', 'pittsburgh rap', 'tennessee hip hop', 'kindermusik', 'acoustic pop', 'thrash metal', 'gym phonk', 'canadian rock', 'modern blues rock', 'melodic drill', 'rock nacional brasileiro', 'healing hz', 'dutch hip hop', 'nyc rap', 'philly rap', 'afrofuturism', 'madchester', 'spanish pop rock', 'new americana', 'reggae', 'rap latina', 'alternative dance', 'trip hop', 'k rap', 'la indie', 'australian hip hop', 'chill house', 'indie anthem folk', 'v pop', 'funk consciente', 'musica chihuahuense', 'rap rock', 'tejano', 'pop flamenco', 'screamo', 'nova mpb', 'urbano mexicano', 'dutch edm', 'pop emo', 'cancion melodica', 'aesthetic rap', 'azontobeats', 'classic country pop', 'sertanejo tradicional', 'cumbia pop', 'jazz', 'afropop', 'rap conciencia', 'korean ost', 'dutch pop', 'j division', 'sigilkore', 'adoracao', 'neo psychedelic', 'ska argentino', 'classic italian pop', 'groove metal', 'irish rock', 'indie pop rap', 'power metal', 'danish pop', 'jazz pop', 'axe', 'pop r b', 'lo fi study', 'industrial rock', 'southern soul', 'pixie', 'uk post punk', 'bossa nova', 'hyperpop', 'lo fi indie', 'lo fi beats', 'phonk brasileiro', 'cumbia sonidera', 'roots reggae', 'german techno', 'sad lo fi', 'sad rap', 'binaural', 'cumbia villera', 'german metal', 'arab pop', 'kentucky hip hop', 'roots rock', 'filter house', 'drill', 'german dance', 'latin worship', 'brazilian reggae', 'video game music', 'broadway', 'samba', 'tech house', 'pop edm', 'neo classical', 'show tunes', 'canadian trap', 'sufi', 'swedish hip hop', 'nursery', 'mollywood', 'korean r b', 'hollywood', 'rap canario', 'irish singer songwriter', 'turkish alt pop', 'spanish rock', 'lullaby', 'electro latino', 'baton rouge rap', 'russian pop', 'skate punk', 'swing', 'german rock', 'shimmer pop', 'grime', 'noise pop', 'country pop', 'speed metal', 'vallenato', 'nigerian hip hop', 'jazz blues', 'salsa puertorriquena', 'indonesian indie', 'swedish trap pop', 'rap marseille', 'musica para ninos', 'reggaeton mexicano', 'la pop', 'ohio hip hop', 'environmental', 'deep underground hip hop', 'ambient pop', 'french indie pop', 'cloud rap francais', 'tollywood', 'lagu jawa', 'stutter house', 'hindi hip hop', 'background piano', 'florida drill', 'new rave', 'cuarteto', 'french rock', 'pinoy hip hop', 'chicago drill', 'turbo folk', 'dreamo', 'japanese singer songwriter', 'oxford indie', 'czsk hip hop', 'swedish electropop', 'classic j pop', 'canadian singer songwriter', 'drill espanol', 'polish pop', 'dangdut', 'rap napoletano', 'drill francais', 'indonesian singer songwriter', 'flamenco urbano', 'new jack swing', 'new french touch', 'industrial', 'coverchill', 'gym hardstyle', 'el paso indie', 'uk alternative pop', 'baroque', 'deep house', 'modern indie folk', 'uk metalcore', 'complextro', 'kollywood', 'hare krishna', 'early music', 'norwegian pop', 'egyptian pop', 'bachata dominicana', 'cantopop', 'modern folk rock', 'country rap', 'mexican indie', 'glitchcore', 'arabesk', 'beatlesque', 'meditation', 'symphonic metal', 'bubblegrunge', 'german drill', 'late romantic era', 'classic pakistani pop', 'weirdcore', 'electric blues', 'electronic trap', 'japanese vgm', 'funk ostentacao', 'chill r b', 'indie rock italiano', 'meme rap', 'blues', 'viral rap', 'indie r b', 'previa', 'pop rock brasileiro', 'trap funk', 'bhojpuri pop', 'covertronica', 'contemporary vocal jazz', 'arrochadeira', 'scandipop', 'pagode baiano', 'neue deutsche harte', 'classic canadian rock', 'indonesian jazz', 'classic swedish pop', 'ambient lo fi', 'dutch rap pop', 'rap dominicano', 'nu cumbia', 'anime score', 'meme', 'swamp rock', 'belgian edm', 'mambo chileno', 'classical era', 'indonesian rock', 'old school atlanta hip hop', 'instrumental hip hop', 'vocaloid', 'russian trap', 'punk blues', 'memphis soul', 'australian indie', 'c pop', 'musica popular colombiana', 'schlager', 'taiwan pop', 'pakistani hip hop', 'australian psych', 'power pop', 'chillhop', 'early romantic era', 'classic indonesian rock', 'drum and bass', 'jam band', 'soul blues', 'edmonton indie', 'nz pop', 'christian rock', 'turkish folk', 'greek trap', 'gujarati pop', 'hamburg hip hop', 'sacramento indie', 'dangdut koplo', 'operatic pop', 'javanese dangdut', 'melbourne bounce international', 'post punk argentina', 'golden age hip hop', 'alternative emo', 'venezuelan hip hop', 'cantautora mexicana', 'pop rap brasileiro', 'electro', 'post punk', 'j pixie', 'nouvelle chanson francaise', 'celtic rock', 'bass house', 'spanish indie pop', 'deep euro house', 'p pop', 'progressive metal', 'red dirt', 'torch song', 'bebop', 'crunk', 'stoner rock', 'bubblegum pop', 'ectofolk', 'background jazz', 'irish pop', 'vietnamese hip hop', 'new york drill', 'pop lgbtq  brasileira', 'malaysian pop', 'danish hip hop', 'turkce drill', 'countrygaze', 'chinese viral pop', 'argentine indie', 'canadian metal', 'modern bhajan', 'comic', 'german alternative rap', 'post romantic era', 'pop house', 'ska', 'chilean rock', 'etherpop', 'indie hip hop', 'philly indie', 'australian electropop', 'dancefloor dnb', 'rumba', 'musica de fondo', 'indie garage rock', 'swedish gangsta rap', 'hip house', 'piano cover', 'korean pop', 'funk pop', 'canadian indie', 'chill pop', 'scenecore', 'funk bh', 'shush', 'tagalog rap', 'dance punk', 'reggae rock', 'electra', 'background music', 'preschool children s music', 'moombahton', 'indonesian r b', 'pop romantico', 'j poprock', 'indie surf', 'smooth jazz', 'dutch rock', 'uk drill', 'turkish alternative rock', 'old school hip hop', 'small room', 'protopunk', 'turkish singer songwriter', 'cartoon', 'cumbia', 'kentucky roots', 'rome indie', 'writing', 'modern salsa', 'speedrun', 'musica infantil', 'bedroom soul', 'experimental pop', 'norteno sax', 'chillwave', 'romanian pop', 'gauze pop', 'lo fi jazzhop', 'dembow', 'trova', 'deep ccm', 'world', 'finnish pop', 'desi trap', 'belgian hip hop', 'classic opm', 'tecnobanda', 'reggaeton chileno', 'alternative pop rock', 'finnish hip hop', 'jazz funk', 'rock cristiano', 'sunshine pop', 'melbourne bounce', 'aussietronica', 'french indietronica', 'norwegian indie', 'laiko', 'japanese soundtrack', 'modern dream pop', 'south carolina hip hop', 'indie triste', 'boom bap espanol', 'albanian hip hop', 'classic schlager', 'pinoy r b', 'birmingham metal', 'rap politico', 'trap mexicano', 'german soundtrack', 'chutney', 'nashville sound', 'czech hip hop', 'velha guarda', 'disco house', 'japanese alternative rock', 'instrumental worship', 'acid rock', 'corridos alternativos', 'greek pop', 'scottish rock', 'british singer songwriter', 'fvnky rimex', 'slowcore', 'israeli pop', 'bossa nova cover', 'british soundtrack', 'detroit trap', 'modern alternative pop', 'cumbia', 'german baroque', 'rap df', 'texas country', 'brill building pop', 'swedish metal', 'german romanticism', 'houston rap', 'scorecore', 'new jersey rap', 'nu jazz', 'social media pop', 'czech pop', 'arkansas country', 'post disco', 'epicore', 'political hip hop', 'redneck', 'gaming edm', 'death metal', 'panamanian pop', 'swedish trap', 'r b brasileiro', 'greek hip hop', 'mexican rock and roll', 'brazilian edm', 'high vibe', 'j rap', 'chicano rap', 'japanese emo', 'ghazal', 'uk funky', 'post hardcore', 'trap chileno', 'uk alternative hip hop', 'black americana', 'salsa colombiana', 'indonesian folk', 'indian indie', 'albanian pop', 'modern southern rock', 'russian dance', 'christian indie', 'cumbia chilena', 'gothic metal', 'french synthpop', 'slowed and reverb', 'indian singer songwriter', 'kentucky indie', 'italian indie pop', 'euphoric hardstyle', 'polish viral pop', 'frauenrap', 'rap genovese', 'nyc pop', 'oakland hip hop', 'italo dance', 'modern blues', 'musica sonorense', 'canadian punk', 'hungarian pop', 'lo fi cover', 'german cloud rap', 'hard rock brasileiro', 'rawstyle', 'russian alt pop', 'rap belge', 'rap calme', 'bronx drill', 'british blues', 'hardcore punk', 'anime lo fi', 'grupero romantico', 'deboxe', 'afroswing', 'indie game soundtrack', 'modern power pop', 'phonk', 'rock urbano mexicano', 'cumbia peruana', 'lo fi sleep', 'banda jalisciense', 'chicago indie', 'indonesian pop punk', 'acoustic cover', 'minimal techno', 'stomp and flutter', 'asmr', 'early modern classical', 'gothic symphonic metal', 'spanish new wave', 'bossbeat', 'lo fi chill', 'jazz trumpet', 'minnesota hip hop', 'hi nrg', 'nu disco', 'dutch trance', 'barnmusik', 'anadolu rock', 'zolo', 'ocean', 'afro r b', 'persian pop', 'latin talent show', 'jazz rap', 'duranguense', 'alternative country', 'trancecore', 'dubstep', 'rock gospel brasileiro', 'afrofuturismo brasileiro', 'modern hard rock', 'supergroup', 'finnish dance pop', 'belgian pop', 'christian hip hop', 'pop electronico', 'classic hardstyle', 'deep groove house', 'hip hop tuga', 'haryanvi pop', 'contemporary post bop', 'gospel', 'northern soul', 'vietnamese melodic rap', 'water', 'doo wop', 'american metalcore', 'shiver pop', 'seattle hip hop', 'stoner metal', 'canadian electronic', 'visual kei', 'colombian hip hop', 'traprun', 'pakistani pop', 'argentine telepop', 'deathcore', 'ukrainian pop', 'piseiro', 'detroit rock', 'big beat', 'melodic dubstep', 'australian surf rock', 'ambient worship', 'canadian country', 'hindi indie', 'hardwave', 'pinoy trap', 'vapor soul', 'future garage', 'ska mexicano', 'taiwan singer songwriter', 'folklore argentino', 'rock alternativo brasileiro', 'partyschlager', 'cool jazz', 'australian indie folk', 'london rap', 'diva house', 'argentine reggae', 'haryanvi hip hop', 'intelligent dance music', 'charva', 'indonesian folk pop', 'nwobhm', 'soul jazz', 'melodic death metal', 'j pop boy group', 'muziek voor kinderen', 'milan indie', 'canadian pop punk', 'progressive bluegrass', 'corridos clasicos', 'a cappella', 'j acoustic', 'indonesian alternative rock', 'chicago bop', 'italian underground hip hop', 'turkce slow sarkilar', 'japanese electropop', 'drumless hip hop', 'hawaiian hip hop', 'rif', 'middle earth', 'canadian contemporary country', 'boston rock', 'classic mandopop', 'swedish synthpop', 'jazz saxophone', 'rave funk', 'mainland chinese pop', 'seattle indie', 'cubaton', 'russelater', 'manguebeat', 'moroccan pop', 'tropicalia', 'vapor twitch', 'neoperreo', 'rap espanol', 'rock uruguayo', 'trap soul', 'electronica argentina', 'urdu hip hop', 'impressionism', 'korean city pop', 'jamaican dancehall', 'musica bajacaliforniana', 'chill drill', 'brighton indie', 'dinner jazz', 'new age piano', 'spacegrunge', 'new age', 'alte', 'suomi rock', 'comic metal', 'funk     bpm', 'arabic hip hop', 'experimental r b', 'japanese r b', 'swedish alternative rock', 'psychedelic hip hop', 'japanese chillhop', 'vallenato moderno', 'uplifting trance', 'roots worship', 'p funk', 'vocal house', 'perreo', 'traditional blues', 'german indie', 'swedish idol pop', 'rock drums', 'sound', 'swedish indie pop', 'rap maroc', 'russian rock', 'vancouver indie', 'bolero mexicano', 'jazz piano', 'levenslied', 'nashville hip hop', 'uk americana', 'nueva cancion', 'scam rap', 'english indie rock', 'ska punk', 'sky room', 'rap cristiano', 'naija worship', 'modern j rock', 'experimental hip hop', 'new jersey indie', 'bhajan', 'south african pop', 'ambient folk', 'neo singer songwriter', 'trap colombiano', 'indie quebecois', 'classic girl group', 'progressive trance', 'classic kollywood', 'dark pop', 'tierra caliente', 'bass trap', 'rebel blues', 'toronto indie', 'manele', 'lo fi product', 'ambient', 'rap baiano', 'amapiano', 'lo fi', 'celtic', 'odia pop', 'funk mandelao', 'folk brasileiro', 'trap baiano', 'teen pop', 'instrumental rock', 'funk viral', 'british folk', 'float house', 'japanese soul', 'german hard rock', 'australian reggae fusion', 'turkish alternative', 'jazz cover', 'tekk', 'minneapolis sound', 'old school rap francais', 'antiviral pop', 'canadian latin', 'medieval rock', 'bases de freestyle', 'shamanic', 'baltimore indie', 'german trap', 'rkt', 'funk das antigas', 'alabama rap', 'women s music', 'nasheed', 'basshall', 'brazilian ccm', 'deep tropical house', 'philly soul', 'czech rock', 'canzone d autore', 'st louis rap', 'pinoy rock', 'zhongguo feng', 'nu gaze', 'crank wave', 'r b argentino', 'athens indie', 'australian house', 'bow pop', 'turkish trap pop', 'harlem renaissance', 'british indie rock', 'thai indie pop', 'austropop', 'synthwave', 'trap catala', 'classify', 'chill phonk', 'russian drain', 'nu metalcore', 'azonto', 'focus', 'karadeniz turkuleri', 'swedish singer songwriter', 'indie viet', 'boom bap', 'swedish eurodance', 'taiwan indie', 'ye ye', 'indiecoustica', 'rap catala', 'russian gangster rap', 'hopebeat', 'texas latin rap', 'variete francaise', 'djent', 'christmas instrumental', 'pinoy reggae', 'g house', 'lebanese pop', 'new school turkce rap', 'synth funk', 'hard bop', 'portuguese pop', 'gymcore', 'singaporean pop', 'russian romanticism', 'swedish drill', 'rap mineiro', 'indonesian worship', 'tamaulipas rap', 'batidao romantico', 'rap algerien', 'art punk', 'greek drill', 'rap chileno', 'hypnagogic pop', 'bubblegum dance', 'italian baroque', 'uk doom metal', 'polish alternative', 'j pop girl group', 'classic colombian pop', 'classic oundtrack', 'jazztronica', 'rap geek', 'westcoast flow', 'retro soul', 'jazz guitar', 'electronic rock', 'brazilian jazz', 'jazz fusion', 'proto metal', 'classic russian pop', 'prog metal', 'rhythm game', 'latin afrobeat', 'iskelma', 'classic uk pop', 'sleaze rock', 'australian children s music', 'spanish punk', 'chicha', 'stomp pop', 'rock nacional', 'electro swing', 'wonky', 'japanese classical', 'rock kapak', 'eau claire indie', 'nintendocore', 'proto hyperpop', 'salsa venezolana', 'deep german hip hop', 'pop folk', 'rock gaucho', 'ottawa rap', 'cyberpunk', 'turkish deep house', 'rap cearense', 'chill abstract hip hop', 'jazz trio', 'rap underground espanol', 'classic city pop', 'scottish singer songwriter', 'french soundtrack', 'hardcore techno', 'ghanaian pop', 'lo fi vgm', 'merengue', 'classic arab pop', 'bassline', 'latin jazz', 'italo disco', 'bitpop', 'boom bap brasileiro', 'pop violin', 'forro de favela', 'swedish power metal', 'glitch hop', 'anime rap', 'cumbia santafesina', 'thai rock', 'lata', 'hk pop', 'italian alternative', 'romanian trap', 'flamenco', 'black metal', 'french reggae', 'german underground rap', 'spanish metal', 'rock brasiliense', 'boston hip hop', 'atlanta indie', 'banda sinaloense', 'musica tlaxcalteca', 'newcastle nsw indie', 'filthstep', 'hands up', 'folk punk', 'trap carioca', 'pet calming', 'mahraganat', 'bandung indie', 'palm desert scene', 'indie punk', 'chill breakcore', 'breakbeat', 'classic russian rock', 'aussie drill', 'israeli mediterranean', 'finnish metal', 'cumbia del sureste', 'livetronica', 'barnsagor', 'german r b', 'chicago punk', 'rap sardegna', 'christian pop', 'nederpop', 'reggaeton cristiano', 'afghan pop', 'anthem emo', 'lo fi emo', 'boston folk', 'lo fi rap', 'argentine alternative rock', 'thai indie rock', 'abstract hip hop', 'violao', 'manchester hip hop', 'nordic soundtrack', 'grave wave', 'lovers rock', 'melodic thrash', 'german punk', 'german pop rock', 'fantasy metal', 'cumbia ranchera', 'german singer songwriter', 'anthem worship', 'australian alternative rock', 'desi emo rap', 'monterrey indie', 'venezuelan rock', 'deep disco house', 'bboy', 'future house', 'dark synthpop', 'cumbia sonorense', 'australian metalcore', 'icelandic indie', 'morelos indie', 'mississippi hip hop', 'noise rock', 'instrumental funk', 'australian country', 'scream rap', 'dembow dominicano', 'acoustic opm', 'narco rap', 'sholawat', 'organic electronic', 'pop nacional antigas', 'digital hardcore', 'indie liguria', 'garage rock revival', 'k indie', 'future bass', 'kirtan', 'neue neue deutsche welle', 'cancion infantil latinoamericana', 'traphall', 'swedish melodeath', 'psychedelic soul', 'upstate ny rap', 'qawwali', 'polish classical', 'ghanaian hip hop', 'thai hip hop', 'trap venezolano', 'canzone napoletana', 'kizomba', 'dutch indie', 'veracruz indie', 'belgian dance', 'nerdcore brasileiro', 'classic sierreno', 'chinese r b', 'solo wave', 'indian folk', 'modern reggae', 'dixieland', 'carnaval', 'new orleans jazz', 'neo r b', 'musica tradicional cubana', 'uptempo hardcore', 'indonesian reggae', 'reggae en espanol', 'egyptian trap', 'canadian soundtrack', 'classic praise', 'finnish power metal', 'pianissimo', 'turkish jazz', 'turkish psych', 'icelandic rock', 'asian american hip hop', 'liquid funk', 'happy hardcore', 'dansband', 'pop virale italiano', 'acoustic guitar cover', 'kayokyoku', 'detroit trap brasileiro', 'bronx hip hop', 'swedish pop rap', 'danish rock', 'bubble trance', 'japanese punk rock', 'vegas indie', 'tontipop', 'singaporean mandopop', 'egyptian hip hop', 'french romanticism', 'dark clubbing', 'electro pop francais', 'progressive metalcore', 'uk dnb', 'french shoegaze', 'japanese alternative pop', 'german house', 'drill italiana', 'rai', 'healing', 'uk reggae', 'aggressive phonk', 'jovem guarda', 'souldies', 'austindie', 'electropowerpop', 'samba enredo', 'afro soul', 'musica triste brasileira', 'swedish death metal', 'nightcore', 'umbanda', 'hamburg electronic', 'saskatchewan indie', 'canadian americana', 'brega paraense', 'cosmic american', 'anti folk', 'classic cantopop', 'musique pour enfants', 'romantico', 'indonesian idol pop', 'riot grrrl', 'rap feminino nacional', 'organic house', 'mexican classic rock', 'chicago soul', 'jawaiian', 'discofox', 'mariachi cristiano', 'british alternative rock', 'oklahoma country', 'bulgarian pop', 'german power metal', 'swedish tropical house', 'welsh rock', 'american folk revival', 'j metal', 'icelandic pop']}`
This resulted in **1350** results, more manageable than the previous numbers, but still specific enough. However now we have to place them in bigger categories. For this I wrote a script that checks the genres against the music genre list (already classified) but there will be stragglers that will be checked with another script to see if they include their genre on the name (electropop, pop punk, metalcore, etc.) and the rest of them will be manually placed using their Wikipedia pages.

# aqui la primera fusion, mas las q quedan
# aqui la segunda filtrando por nombre
# aqui la definitiva

After this, I have manually changed a few things ([[genre list modifications]]), reduced categories that I considered redundant and added my top 66 subgenres from the last 4 weeks, top 60 from the last 6 months, and the top 62 from my all time activity, running the statistics with [Chosic](https://www.chosic.com/spotify-listening-stats/), putting them together we get 77 subgenres:
`{'genres' : ['chicago rap', 'etherpop', 'candy pop', 'canadian contemporary r&b', 'pop emo', 'canadian pop', 'afrofuturism', 'hip pop', 'swedish synthpop', 'ohio hip hop', 'hip hop', 'pixie', 'pop rap', 'pop', 'art pop', 'nintendocore', 'post-teen pop', 'indie poptimism', 'synth funk', 'modern alternative rock', 'irish singer-songwriter', 'louisville indie', 'swedish electropop', 'spanish noise pop', 'metalcore', 'rap', 'barbadian pop', 'nz pop', 'trancecore', 'melodic rap', 'rock', 'pov: indie', 'alt z', 'alternative pop rock', 'escape room', 'permanent wave', 'metropopolis', 'la indie', 'rap metal', 'minneapolis sound', 'skramz', 'garage rock', 'modern rock', 'pop dance', 'post-grunge', 'vancouver indie', 'funk', 'uk post-hardcore', 'boy band', 'lgbtq+ hip hop', 'sheffield indie', 'colombian pop', 'edm', 'alternative metal', 'british indie rock', 'nu metal', 'funk rock', 'american metalcore', 'uk pop', 'australian pop', 'pop punk', 'british alternative rock', 'emo', 'swedish pop', 'dance pop', 'melodic metalcore', 'dfw rap', 'brooklyn indie', 'spanish indie rock', 'urban contemporary', 'bedroom pop', 'modern indie pop', 'urbano espanol', 'uk metalcore', 'uk pop punk', 'electropop', 'viral pop']}`
# functional one