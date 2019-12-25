extern crate serde;
extern crate serde_derive;
extern crate serde_json;
extern crate reqwest;

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

pub fn search(lat_min:f64, lat_max:f64, long_min:f64, long_max:f64, ssid: String) -> Result<(f64, f64), Error> {
    let request_url = format!("https://api.wigle.net/api/v2/network/search?first=0&latrange1={lat_range_min}&latrange2={lat_range_max}&longrange1={long_range_min}&longrange2={long_range_max}&freenet=false&paynet=false&ssid={ssid}",
                              lat_range_min = lat_min,
                              lat_range_max = lat_max,
                              long_range_min = long_min,
                              long_range_max = long_max,
                              ssid= ssid,
                            );

    let client = reqwest::Client::new();
    println!("Searching...")
    let raw_data = client.get(&request_url).header("Authorization","Basic ***").send()?.text()?.to_owned();
    let process: &str = &raw_data[..];


    let resp: Output = serde_json::from_str(process).unwrap();
    
    if !resp.success{
        println!("Query unsucessful");
        Ok((0.0,0.0))
    } else {

        let content = resp.results;

        Ok((content[0].trilat, content[0].trilong))
    }

}
