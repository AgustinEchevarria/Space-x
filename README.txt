Space-x Endpoint Documentation

requirements:
            python3:
                    random, socket, request, json

Run in your host:
        python3 Endpoint.py (localserver)

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

Send requests to Endpoint port:
    ej:
       curl '127.0.0.1:8081' -X PUT -H "Content-Type: application/json" -d '{"type":"task","title":"DESCRIPTION CURL","category":"research"}'
 