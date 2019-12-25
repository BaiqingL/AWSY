extern crate serde;
extern crate serde_derive;
extern crate serde_json;
extern crate reqwest;

use std::process;
use reqwest::Error;
use serde::Deserialize;

#[derive(Deserialize, Debug)]
struct Results {
    trilat: f64,
    trilong: f64,
}

#[derive(Deserialize)]
struct Output {
    success: bool,
    results: Vec<Results>,
}

fn main() -> Result<(), Error> {
    let request_url = format!("https://api.wigle.net/api/v2/network/search?first=0&latrange1={lat_range_min}&latrange2={lat_range_max}&longrange1={long_range_min}&longrange2={long_range_max}&freenet=false&paynet=false&ssid={ssid}",
                              lat_range_min = "41.159",
                              lat_range_max = "42.889",
                              long_range_min = "-73.5081",
                              long_range_max = "-69.7398",
                              ssid= "xfinity"
                            );

    let client = reqwest::Client::new();
    let raw_data = client.get(&request_url).header("Authorization","Basic -").send()?.text()?.to_owned();
    let process: &str = &raw_data[..];


    let resp: Output = serde_json::from_str(process).unwrap();
    
    if !resp.success{
        println!("Query unsucessful");
        process::exit(1);
    }
    
    let content = resp.results;

    let result = (content[0].trilat, content[0].trilong);
    println!("{:?}", result);

    Ok(())
}
