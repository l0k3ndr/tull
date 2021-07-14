# `T`eleport `U`r `L`ogs with `L`ove

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

`tull` is a command line utility which with help of a background server, organizes your log storage and sharing workflow. Whatever you pipe into it, will get a unique UUID and the data gets stored locally - accessible via a flask server with simple endpoints. You can use ngrok or localtunnel then to share it outside LAN as well.

### Installion

`pip install tull`

OR

1. clone the repo
2. create a venv and activate it
3. pip install -r requirements.txt

### Usage

Execute `tull web` and it will give you few urls. Open the one with TULL_WEB_URL in front.

For each session `tull` generates a ID, and that ID is used to associate the data of that session.

Type anything into the active terminal. On the web also on the correponding ID page it will reflect.

Exit with Ctrl-D.

Outcome:
1. you have your logs stored for future reference in an organized manner
2. you can share the url to anyone having access to your server via http. 

[youtube demo](https://www.youtube.com/watch?v=AQ6V2fIx1tw)

### Future Roadmap

 1. Security 
 2. Better UI for /web interface
 3. API pagination for /api interface
 4. Streaming for /raw interface
 5. Make readme look good
 6. Add tutorial
 7. Add gif
