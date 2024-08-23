# GTFS-RT Validator

## Description

GTFS-RT Validator is a simple web application built with Flask that allows users to validate the correctness of GTFS-RT (General Transit Feed Specification - Realtime) feeds. Users can input the URL of a GTFS-RT feed, and the application will check if the feed is valid according to the GTFS-RT specification. If valid, an extract of the feed is displayed on the webpage.

## Features

- **URL Validation:** Ensures the provided GTFS-RT feed URL is valid.
- **GTFS-RT Validation:** Parses and validates the GTFS-RT feed to ensure it conforms to the expected format.
- **Feed Extract Display:** Displays an extract of the GTFS-RT feed if it is valid.
- **User-Friendly Interface:** Simple and intuitive web interface for easy use.

## Prerequisites

- Python 3.x
- Pip (Python package manager)
- `protoc` (Protocol Buffers compiler)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/gtfs-rt-validator.git
    cd gtfs-rt-validator
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Generate the `gtfs_realtime_pb2.py` file:**

    Download the GTFS-Realtime `.proto` file and generate the Python file:

    ```bash
    wget https://raw.githubusercontent.com/google/transit/master/gtfs-realtime/proto/gtfs-realtime.proto
    protoc --python_out=. gtfs-realtime.proto
    ```

## Usage

1. **Run the application:**

    ```bash
    sudo python app.py
    ```

2. **Access the application:**

    Open your web browser and navigate to `http://[hostname or IP]`.

3. **Validate a GTFS-RT feed:**

   - Enter the URL of a GTFS-RT feed in the provided input field.
   - Click on the "Validate" button to check the validity of the feed.
   - If the feed is valid, an extract will be displayed on the webpage.

## Project Structure

gtfs-rt-validator/
├── app.py                  # Main Flask application
├── gtfs_realtime_pb2.py    # Generated Python file from .proto
├── templates/
│   └── index.html          # HTML template for the web interface
├── static/
│   └── style.css           # CSS file for styling the interface
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - A lightweight WSGI web application framework in Python.
- [GTFS Realtime](https://developers.google.com/transit/gtfs-realtime) - Real-time public transit data specification.
- [Protobuf](https://developers.google.com/protocol-buffers) - Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.

## Author

© Amaury DUCHENE 2024
