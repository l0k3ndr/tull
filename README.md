# TULL - `T`eleport `U`r `L`ogs with `L`ove

```
            .----------------.  .----------------.  .----------------.  .----------------.   
           | .--------------. || .--------------. || .--------------. || .--------------. |  
           | |  _________   | || | _____  _____ | || |   _____      | || |   _____      | |  
           | | |  _   _  |  | || ||_   _||_   _|| || |  |_   _|     | || |  |_   _|     | |  
           | | |_/ | | \_|  | || |  | |    | |  | || |    | |       | || |    | |       | |  
           | |     | |      | || |  | '    ' |  | || |    | |   _   | || |    | |   _   | |  
           | |    _| |_     | || |   \ `--' /   | || |   _| |__/ |  | || |   _| |__/ |  | |  
           | |   |_____|    | || |    `.__.'    | || |  |________|  | || |  |________|  | |  
           | |              | || |              | || |              | || |              | |  
           | '--------------' || '--------------' || '--------------' || '--------------' |  
            '----------------'  '----------------'  '----------------'  '----------------'   
```

`tull` is a command line utility which with help of a background server, organizes your log storage and sharing workflow.

Installion with pip. `pip install tull`

Execute `tull web` and it will give you few urls. Open the one with TULL_WEB_URL in front.

For each session `tull` generates a ID, and that ID is used to associate the data of that session.

Type anything into the active terminal. On the web also on the correponding ID page it will reflect.

Exit with Ctrl-D.

`ls | tull`

`ps | tull`

`python manage.py runserver 2>&1 | tull`

All these above commands will start sending logs to tull server as well as transparently pass them to output. That way: 

1. you have your logs stored for future reference in an organized manner
2. you can share the url to anyone having access to your server via http. 

Read the code and see for yourself - less than 150 lines I guess. 

Future Plans:-
 1. Security 
 2. Better UI for /web interface
 3. API pagination for /api interface
 4. Streaming for /raw interface
