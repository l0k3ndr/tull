use serde_derive::Serialize;

use std::path::Path;
use std::fs;
use std::net::SocketAddr;

use home::home_dir;
use warp::Filter;

#[derive(Serialize)]
struct JSONResponse {
    data: Vec<String>,
}


#[tokio::main]
pub async fn run_server(socket: SocketAddr) {
    fn get_data_dir_path() -> String {
        let user_home = home_dir().unwrap().to_owned();
        let user_home_str = user_home.to_str().unwrap();
        format!("{}/{}", user_home_str, ".tull/data")
    }

    let session_list_web = warp::path!("tull" / "web")
        .map(|| {
            let files = fs::read_dir(get_data_dir_path()).unwrap();
            let mut s: String = "".to_string();
            for file in files {
                let file_name = file.unwrap().file_name();
                let file_name_str = file_name.to_str().unwrap();
                s.push_str(&format!("<a href='/tull/web/{}'>{}</a><br />", &file_name_str, &file_name_str).to_string());
            }
            warp::reply::html(s)
        });

    let session_logs_web = warp::path!("tull" / "web" / String)
        .map(|session_id| {
            let file_path = format!("{}/{}", get_data_dir_path(), session_id);
            let file_exists = Path::new(&file_path).exists();
            if !file_exists {
                warp::reply::html("Whatever you are looking for, is long gone!".to_string())
            } else {
                let file_contents: String = fs::read_to_string(file_path)
                    .unwrap()
                    .split("\n")
                    .map(|line: &str| format!("<span>{}</span>", line))
                    .collect::<Vec<String>>()
                    .join("<br />");

                let mut logs_html = "<script>setInterval(() => { window.location.reload() }, 5000);</script>".to_string();
                logs_html.push_str(&file_contents.to_string());
                warp::reply::html(logs_html)
            }
        });

    let session_list_api = warp::path!("tull" / "api")
        .map(|| {
            let files = fs::read_dir(get_data_dir_path()).unwrap();
            let mut sessions: Vec<String> = [].to_vec();

            for file in files {
                sessions.push(file.unwrap().file_name().to_str().unwrap().to_string());
            }

            warp::reply::json(&JSONResponse {
                data: sessions
            })
        });

    let session_logs_api = warp::path!("tull" / "api" / String)
        .map(|session_id| {
            let file_path = format!("{}/{}", get_data_dir_path(), session_id);
            let file_exists = Path::new(&file_path).exists();
            if !file_exists {
                warp::reply::json(&JSONResponse {
                    data: [].to_vec()
                })
            } else {
                let file_contents: Vec<String> = fs::read_to_string(file_path)
                    .unwrap()
                    .split("\n")
                    .map(|line: &str| line.parse().unwrap())
                    .collect::<Vec<String>>();

                warp::reply::json(&JSONResponse {
                    data: file_contents
                })
            }
        });

    let session_list_raw = warp::path!("tull" / "raw")
        .map(|| {
            let files = fs::read_dir(get_data_dir_path()).unwrap();
            let mut file_names: String = "".to_string();
            for file in files {
                let file_name = file.unwrap().file_name();
                let file_name_str = file_name.to_str().unwrap();
                file_names.push_str(file_name_str);
            }
            file_names
        });

    let session_logs_raw = warp::path!("tull" / "raw" / String)
        .map(|session_id| {
            let file_path = format!("{}/{}", get_data_dir_path(), session_id);
            let file_exists = Path::new(&file_path).exists();
            if !file_exists {
                "".to_string()
            } else {
                let file_contents: String = fs::read_to_string(file_path)
                    .unwrap()
                    .split("\n")
                    .map(|line: &str| line.parse().unwrap())
                    .collect::<Vec<String>>()
                    .join("\n");

                file_contents
            }
        });

    let routes = warp::get().and(
        session_list_web
            .or(session_logs_web)
            .or(session_list_api)
            .or(session_logs_api)
            .or(session_list_raw)
            .or(session_logs_raw)
    );

    warp::serve(routes).run(socket).await;
}
