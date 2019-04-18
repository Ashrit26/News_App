import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import requests


def news():
    main_url = "https://hn.algolia.com/api/v1/search_by_date?tags=story"
    page = requests.get(main_url).json()
    print(page)
    articles = page["hits"]
    cred = credentials.Certificate("./today30-26ab1-firebase-adminsdk-6wkli-5992de534d.json")
    app = firebase_admin.initialize_app(cred)
    for i in range(len(articles)):

        jsson = {
            "title": articles[i]["title"],
            "datetime": articles[i]["created_at"].replace('-','').replace('T','').replace(':','').replace('Z','')[:12],
            "url": articles[i]["url"],
            "time" : articles[i]["created_at"].replace('-',':').replace('T',' ')[:16],
            "author" : articles[i]["author"]
        }
        store = firestore.client()
        doc_ref = store.collection(u'test')
        doc_ref.add(jsson)
        print(jsson)
    #     print("\n")

if __name__ == "__main__":
    news()