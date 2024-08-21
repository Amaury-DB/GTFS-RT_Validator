# GTFS-RT Validator

## Description

GTFS-RT Validator is a simple web application built with Flask that allows users to validate the correctness of GTFS-RT (General Transit Feed Specification - Realtime) feeds. Users can input the URL of a GTFS-RT feed, and the application will check if the feed is valid according to the GTFS-RT specification.

## Features

- **URL Validation:** Ensures the provided GTFS-RT feed URL is valid.
- **GTFS-RT Validation:** Parses and validates the GTFS-RT feed to ensure it conforms to the expected format.
- **User-Friendly Interface:** Simple and intuitive web interface for easy use.

## Prerequisites

- Python 3.x
- Pip (Python package manager)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Amaury-DB/gtfs-rt-validator.git
    cd gtfs-rt-validator
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` does not exist, manually install the dependencies:

    ```bash
    pip install flask protobuf validators
    ```

## Usage

1. **Run the application:**

    ```bash
    python app.py
    ```

2. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Validate a GTFS-RT feed:**

   - Enter the URL of a GTFS-RT feed in the provided input field.
   - Click on the "Validate" button to check the validity of the feed.
   - The result of the validation will be displayed on the screen.

## Project Structure

```
gtfs_rt_validator/
│
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # HTML template for the web interface
└── static/
└── style.css           # CSS file for styling the interface
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - A lightweight WSGI web application framework in Python.
- [GTFS Realtime](https://developers.google.com/transit/gtfs-realtime) - Real-time public transit data specification.
- [Protobuf](https://developers.google.com/protocol-buffers) - Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.
