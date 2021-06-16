
from newsapi import NewsApiClient
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Here we are selecting the human like voices

for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.runAndWait()
    engine.stop()
    break

def speak(audio):
    engine.setProperty('rate', 160)
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def get_news(topic):
    my_api_key = "<YOUR API KEY>"

    news_api = NewsApiClient(api_key=my_api_key)

    data = news_api.get_everything(q=topic, language='en', page_size=20)

    # print(data['articles'][0]['title'])

    list_of_articles = []


    for i in range(15):
        new_dic = {'Title' : data['articles'][i]['title'], 'Content' : data['articles'][i]['description']}
        list_of_articles.append(new_dic)

    # print(list_of_articles)

    list_final = []

    for i in list_of_articles:
        listA = []
        listA.append(i['Title'])
        listA.append(i['Content'])
        list_final.append(listA)

    return list_final



topic = "technology in covid 19"
list_of_news = get_news(topic)
speak("Reading the top 5 news articles on the given topic")
for i in range(5):
    list_new = list_of_news[i]
    speak("Article {}".format(str(i+1)))
    speak(list_new[0])
    speak("Description")
    speak(list_new[1])

