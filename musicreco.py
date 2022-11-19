import pandas as pd

def musicreco(emotion_dct, file_path = 'data/spotify_result.csv'):
    musics = pd.read_csv(file_path)

    mapping = {
        'anger':2,
        'fear':5,
        'joy':4,
        'neutral':3,
        'sadness':1,
        'surprise':0
    }

    if emotion_dct['is_dominate']:
        cluster = mapping[emotion_dct['highest_emotion']]
        music = musics[musics['Cluster'] == cluster].sample(5)
    else:
        main_cluster = mapping[emotion_dct['highest_emotion']]
        second_cluster = mapping[emotion_dct['second_emotion']]
        main_music = musics[musics['Cluster'] == main_cluster].sample(4)
        second_music = musics[musics['Cluster'] == second_cluster].sample(1)
        music = pd.concat([main_music, second_music])

    music['url'] = "https://open.spotify.com/track/"+ music['track_uri'].str.split(':',expand=True)[2]

    res = music[['name','artist_name','url']].to_records(index = False)
    #print(res)
    res_str_lst = []
    for index, r in enumerate(res):
        res_str_lst.append(str(index+1)+". "+ r[0]+' --> '+r[1])

    return [res, res_str_lst]