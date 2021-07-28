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
Whatever you pipe into `tull`, will get a unique UUID and the data gets stored locally - accessible via a flask server with simple endpoints. You can use ngrok or localtunnel then to share it outside LAN as well. It won't break the console as it also redirects the stream transparently to stdout.

### Installation

1. clone the repo
2. install [Rust](https://www.rust-lang.org/learn/get-started)
3. then run `cargo build`

### Usage

[![TULL-TUTORIAL](https://img.youtube.com/vi/AQ6V2fIx1tw/0.jpg)](https://www.youtube.com/watch?v=AQ6V2fIx1tw)

**STDIN Test:**
Execute `tull web` and it will give you few urls. Open the one with TULL_WEB_URL in front.
For each session `tull` generates a ID, and that ID is used to associate the data of that session.
Type anything into the active terminal. On the web also on the correponding ID page it will reflect.
Exit with Ctrl-D. (Currently Ctrl-C is causing the flask server to stop as well along with stream caputre, working on it)

**Actual Use Case**
Execute `ps ax | tull` ; you can see the output of your command but also the logs are saved with a unique id. Go to TULL_WEB_URL(found via `tull web` earlier)

Outcome:
1. you have your logs stored for future reference in an organized manner
2. you can share the url to anyone having access to your server via http. 

What I do generally is hook it up with the ngrok tunnel. ngrok is a tool which you can use to create secure tunnels from your local ports in one-liner. So just do ```ngrok http 17171``` and you can share these logs with anyone on the other side of internet.

### Disclaimer

This is a personal project, don't use this in production or anywhere where you are not sure of security impacts. Until a v1.0 everything is considered unstable. :)

### Future Roadmap/Updates

 1. Security - add basic auth if needed
 2. HTTPS exposure
 3. add documentation and video --follow feature
 4. make --follow feature work over the network
 5. --expose-via=ngrok | --expose-via=localtunnel 
 6. How to use --tutorial mode
 7. Better UI for /web interface - make it easier to search/navigage/organize logs
 8. / and /tull endpoints need to show something
 9. API pagination for /api interface
 10. Streaming for /raw interface - also, how to read last n lines fast!
 11. Make readme look professional
 12. add unit tests
 13. start creating tags with pip pushes on version bumps
 14. follow semantic versioning and freeze external api models
 15. add colors to terminal outputs
 16. add timestamps to logs
 17. allow multiple log streams to be merged
 18. allow paginated access to logs
 19. improve the art of readme page | add colors
 20. add build banner in readme

### How it works

When you run this, it creates a folder .tull in your user home directory. Also, at the same time it starts a background process which runs the flask server with some simple apis if it is already not started. Then whenever any data is piped into it, or it is invoked from command line, it creates a unique ID, and starts storing the pipe stream data into that file and also transparently writing it to stdout. That way it doesn't break your existing flow, saves the logs with unique ID and allows you to browse them later. Not too fancy, but useful.

### Release Notes

v0.8: added log follow capability and log listing capability
