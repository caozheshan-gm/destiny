from transformers import pipeline

def detectemotion(text):
    classifier = pipeline("text-classification", model="model/emotion-model/", return_all_scores=True)

    dct = {}
    output = classifier(text)

    for i in output[0]:
        label = i['label']
        if label == 'disgust':
            label = 'anger'
        if label in dct:
            dct[label] += i['score']
        else:
            dct[label] = i['score']
    
    sort_dct = sorted(dct.items(), key=lambda item: item[1], reverse=True)

    dominate = sort_dct[0][1] > 0.9
    if dominate:
        emotion_str = f'Your Emotion: {sort_dct[0][0]}({round(sort_dct[0][1]*100,2)}%)'
    else:
        emotion_str = f'Your Emotion: {sort_dct[0][0]}({round(sort_dct[0][1]*100,2)}%), {sort_dct[1][0]}({round(sort_dct[1][1]*100,2)}%)'

    return {
        'info': emotion_str,
        'highest_emotion': sort_dct[0][0],
        'second_emotion': sort_dct[1][0],
        'highest_score': sort_dct[0][1],
        'second_score': sort_dct[1][1],
        'is_dominate': dominate
    }

if __name__ == '__main__':
    text = input()
    print(detectemotion(text))