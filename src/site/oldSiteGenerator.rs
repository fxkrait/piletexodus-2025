// https://stackoverflow.com/questions/31225745/iterate-over-stdfsreaddir-and-get-only-filenames-from-paths
// https://www.hackertouch.com/rust-loop-over-vector.html
use std::env;
use std::fs;
use std::collections::BTreeMap;
use std::collections::BTreeSet;
use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {

    let paths = fs::read_dir("../../feeds/melody/files/webm_96k/").unwrap();

    // get filenames
    let names =
        paths.map(|entry| {
            let entry = entry.unwrap();
            let entry_path = entry.path();
            let file_name = entry_path.file_name().unwrap();
            let file_name_as_str = file_name.to_str().unwrap();
            let file_name_as_string = String::from(file_name_as_str);

            file_name_as_string
        }).collect::<Vec<String>>();

    // print filenames out
    for i in &names {
        println!("{}: {}", i, getKey(&i));
    }
    
    // https://doc.rust-lang.org/std/collections/hash_map/struct.HashMap.html
    let mut name_map: BTreeMap<&str, BTreeSet<&str>> = BTreeMap::new();
    for name in &names {
        let key = getKey(name);
        if name_map.contains_key(key) {
            name_map.get_mut(key).expect("error").insert(name); // append name to vector
        } else {
            let mut set: BTreeSet<&str> = BTreeSet::new();
            set.insert(name);
            // name_map.insert(key, BTreeSet::from(name));
            name_map.insert(key, set);
        }
    }
    for (key, value) in &name_map {
        println!("{}: {:?}", key, value);
    }

    // https://doc.rust-lang.org/std/fs/struct.File.html
    for (key, value) in &name_map {
        let mut file = File::create(format!("{}.html", key))?;
        file.write_all(b"<!DOCTYPE html>\n")?;
        file.write_all(b"<html>\n")?;
        file.write_all(b"    <body>\n")?;
        println!("{}: {:?}", key, value);
        //file.write_all(b"Hello, world!")?;
        file.write_all(format!("<h3>{}</h3>\n", key).as_bytes())?;
        for val in value {
            println!(".....{}", val);
            file.write_all(format!("<p>{}</p>\n", val).as_bytes())?;
            file.write_all(format!("<audio controls preload=\"none\"><source src=\"feeds/melody/files/webm_96k/{}\" type=\"audio/webm\"></audio>\n", val).as_bytes())?;
        }
        file.write_all(b"    </body>\n")?;
        file.write_all(b"</html>")?;
    }

    Ok(())
}

// map filename to header
fn getKey(name: &str) -> &str {
    // https://users.rust-lang.org/t/how-to-get-a-substring-of-a-string/1351
    let first_two_chars = &name[..2];
    // https://stackoverflow.com/questions/49441484/matching-on-an-enum-reference-and-returning-a-string-results-in-match-arms-have
    let matched_val = match first_two_chars {
        // Match a single value
        "te" => "B.C.E.",
        "01" => "01-January",
        "02" => "02-February",
        "03" => "03-March",
        "04" => "04-April",
        "05" => "05-May",
        "06" => "06-June",
        "07" => "07-July",
        "08" => "08-August",
        "09" => "09-September",
        "10" => "10-October",
        "11" => "11-November",
        "12" => "12-December",
        // Handle the rest of cases
        _ => "Ain't special",
    };
    return matched_val
}