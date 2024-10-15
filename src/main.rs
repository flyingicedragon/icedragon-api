#[macro_use]
extern crate rocket;

use chrono::NaiveDate;
use holidays::Country;

fn init() -> anyhow::Result<()> {
    holidays::init()?;
    holidays::Builder::new()
        .countries(&[Country::CN])
        .years(2023..2025)
        .init()?;

    Ok(())
}

#[get("/")]
fn index() -> &'static str {
    "API for icedragon"
}

#[get("/holidays/<year>/<month>/<day>")]
fn holiday(year: i32, month: u32, day: u32) -> &'static str {
    if cfg!(debug_assertions) {
        println!("It's {}/{}/{}", year, month, day);
    }
    let d = NaiveDate::from_ymd_opt(year, month, day).expect("Invalid date");
    let holiday = holidays::contains(Country::CN, d).unwrap();
    if cfg!(debug_assertions) {
        println!("{:?}", holiday);
    }
    match holiday {
        true => "true",
        _ => "false",
    }
}

#[launch]
fn rocket() -> _ {
    init().unwrap();
    rocket::build().mount("/", routes![index, holiday])
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn init_test() -> anyhow::Result<()> {
        init()?;
        let d = NaiveDate::from_ymd_opt(2024, 10, 12).expect("Invalid date");
        let holiday = holidays::contains(Country::CN, d)?;
        assert_eq!(false, holiday);
        let d = NaiveDate::from_ymd_opt(2024, 10, 7).expect("Invalid date");
        let holiday = holidays::contains(Country::CN, d)?;
        assert_eq!(true, holiday);

        Ok(())
    }
}
