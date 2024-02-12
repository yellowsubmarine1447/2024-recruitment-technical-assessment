use axum::{http::StatusCode, response::IntoResponse, Json};
use serde::{Deserialize, Serialize};

pub async fn process_data(Json(request): Json<DataRequest>) -> impl IntoResponse {
    // Calculate sums and return response

    let mut response = DataResponse {
        string_len: 0,
        int_sum: 0,
    };
    for entry in request.data {
        match entry {
            DataEntry::Int(num) => response.int_sum += num,
            DataEntry::String(string) => response.string_len += string.len() as i32,
        };
    }

    (StatusCode::OK, Json(response))
}

#[derive(Deserialize)]
pub struct DataRequest {
    data: Vec<DataEntry>,
}

#[derive(Serialize)]
pub struct DataResponse {
    string_len: i32,
    int_sum: i32,
}

#[derive(Deserialize)]
enum DataEntry {
    Int(i32),
    String(String),
}
