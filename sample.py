import json
import quopri

from gmail import *


if __name__ == "__main__":
    '''
        GmailApi sample code。
    '''

    user = 'me'

#    json_path = './client_secret_626154498738-l0qmanntp7ghmlkmr521s1ote3qmfnla.apps.googleusercontent.com.json'
    json_path = './client_id.json'
    api = GmailApi(json_path) #You need authorized when you run at first time.
    query =  "is:unread"#Unread message query

    #Show unread message list
    maillist = api.get_mail_list(user, query )
#    print("---Show unread message list as id and threadId---")
#    print( json.dumps(maillist, indent=4))

    #show row mail contents
    for i in range(len(maillist["messages"])):
        content = api.get_mail_content(user, maillist["messages"][i]['id']) # [0]<-select message from message list
#        print("---Show mail row contents---")
#        print( json.dumps(content, indent=4))
#        exit()

        print("---Title---")
        title = read_title(content)
        print(title)
        print("---Body---")
        body = read_message_html(content)
        print(body)
        print("---Snippet---")
        snippet = read_snippet(content)
        print(snippet)
