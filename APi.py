import twitter
import csv
api_key="Kua41JGvLGDFGwSdEFPImiM67"
api_secret_key="XhCr36YMuK0jrgu34oLMrTnvYTqDznQazzEaEi4DLXp9Ne28Bk"
bearer_token="AAAAAAAAAAAAAAAAAAAAABEeNAEAAAAAkVKTlVQaQq6KASnV%2F6L5QyzrLDU%3DQ4yjfbWX6Is3VT594rNpRHnZuAG09NaMY3YyIw1AGzSeAvubo3"
access_token="1266645527917211649-AG6as3XTuTAj2qpISQoYJV8duZZjDJ"
access_token_secrets="d5ujUWla5zIatoghRhOCRSbqAXqrXTAvc9yrjUYLinBsd"
api = twitter.Api(consumer_key=api_key,consumer_secret=api_secret_key,access_token_key=access_token,access_token_secret=access_token_secrets)
# print(api.VerifyCredentials())
# statuses = api.GetUserTimeline(1266645527917211649)
# print([s.text for s in statuses])
tweets=api.GetSearch(term="Australia", since=2020-11-18,count=10)
# tweets.text.encode("utf-8")
a=[t.text for t in tweets]
# a.encode("utf-8")
# print(a)
fields = ['Name']
with open('tweets.csv','w+',newline='',encoding='utf-8') as f:
    write = csv.writer(f) 
    # write.writerow(fields) 
    for sen in a:
        write.writerow([sen]) 
