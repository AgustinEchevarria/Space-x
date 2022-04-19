Space-x Endpoint Documentation

requirements:
            python3:
                    random, socket, request, json

Steps:
        1__    Python3 Endpoint.py (localserver)
        2__    Send request 'POST' or 'GET' (GET request response json with lists) --- (All request in path '/')

Entry:
        New issue:
                type = issue
                title = 'issue_title'
                description = 'issue_description'
        New bug:
                type = bug
                description = 'bug_description'
        New Task:
                type = task
                title = 'task_title'
                category = 'Maintenance'/'Research'/'Test'

Payload: "{"type":"type","title":"title","description":"description"}"

(this experimental server uses json as the communication language, regardless of the content-type header, the payload must always be json)
(If you send bad payload, this server response empty packet.)
Send requests to Endpoint port:
    ej:
       curl '127.0.0.1:8081' -X PUT -H "Content-Type: application/json" -d '{"type":"task","title":"DESCRIPTION CURL","category":"research"}'
 
