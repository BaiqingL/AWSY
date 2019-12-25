mod state_query;
mod WiGLE;

use std::io;

fn main() {

    let mut state_input = String::new();

    println!("Enter state abbreivation for quicker search:");
    match io::stdin().read_line(&mut state_input) {
        Ok(_) => {
            state_input = state_input.trim().to_string();
        }
        Err(e) => {
            println!("{:?}", e);
        }
    }
    let value = state_query::state_boundaries(state_input.to_ascii_uppercase());

    if value == [0.0,0.0,0.0,0.0]{
        println!("Failed to find state: {}", state_input);
        return;
    }
    println!("Located state coordinates");

    let mut bssid_input = String::new();

    println!("Enter the BSSID to search:");
    match io::stdin().read_line(&mut bssid_input) {
        Ok(_) => {
            bssid_input = bssid_input.trim().to_string();
        }
        Err(e) => {
            println!("{:?}", e);
        }
    }

    let result = WiGLE::search(value[0],value[1],value[2],value[3],bssid_input);
    println!("{:?}", result);
}
