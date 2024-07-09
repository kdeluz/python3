# Assignment 3: Building Interactive APIs with Flask and Dash

This repository contains the following applications for the Assignment 3 submission in my Web Development 3 class at RRC:
1. A Flask app with three routes
2. A Dash app that displays and graphs the given data.

## Installation

1. **Clone the repository**:
    ```bash
    git clone git@github.com:kdeluz/python3.git
    cd python3
    ```

2. **Install the required packages**:
    ```bash
    pip install Flask Pillow dash pandas dash-table plotly requests
    ```
    Alternatively, you can also run the following command:
    ```bash
    pip install -r requirements.txt
    ```

## Part 1: Flask Application

### Overview

The Flask application provides three main routes:
1. Home page explaining the usage.
2. Converting an image from one format to another.
3. Generating a random number within a given range.

### Usage

1. **Run the Flask app through Jupyter Lab**:
    ```bash
    jupyter lab
    ```
   This will start the Jupyter Lab notebook server; access it in your web browser at `http://localhost:8888/`.

2. **Endpoints**:
    - **Index Route**:
        - Method: `GET`
        - URL: `http://127.0.0.1:5000/`
        - Description: Displays the usage instructions for the other routes.

    - **Convert Route**:
        - Method: `POST`
        - URL: `http://127.0.0.1:5000/convert`
        - Description: Converts an image from one format to another.
        - Form Data:
            - `image`: The image file to be converted.
            - `output_type`: The desired output format (e.g., `jpeg`, `png`, `gif`).

    - **Random Number Route**:
        - Method: `GET`
        - URL: `http://127.0.0.1:5000/random-number?min=<min>&max=<max>`
        - Description: Generates a random number within the specified range.
        - Query Parameters:
            - `min`: The minimum value.
            - `max`: The maximum value.

### Usage with Postman

1. **Convert Route**:
    - Set the request type to `POST`.
    - URL: `http://127.0.0.1:5000/convert`
    - Under the `Body` tab, select `form-data`.
    - Add a file field named `image` and upload an image file.
    - Add a text field named `output_type` and set its valuee to one of the supported types (e.g., `jpeg`).
    - Click `Send`.

2. **Random Number Route**:
    - Set the request type to `GET`.
    - URL: `http://127.0.0.1:5000/random-number?min=10&max=50`
    - Alternatively, you can set the URL to be whichever number you'd like.
    - Click `Send`.

## Part 2: Dash Application

### Overview

This Dash aplication is meant to visualizes recycling, garbage, and yard waste collection days in Winnipeg, using the API from the [Winnipeg Recycling, Garbage, and Yard Waste Collection Days](https://data.winnipeg.ca/resource/6rcy-9uik.json).

### Usage

1. **Run the Flask app through Jupyter Lab**:
    ```bash
    jupyter lab
    ```
   This will start the Jupyter Lab notebook server; access it in your web browser at `http://localhost:8888/`.

2. **Features**:
    - **Data Table**:
        - Displays the data fetched from the Winnipeg open data API.
    - **Bar Chart**:
        - Visualizes the count of addresses per collection day, distinguishing between "A" and "B" weeks.

### Data Source

The data is fetched from the Winnipeg open data API:
[Winnipeg Recycling, Garbage, and Yard Waste Collection Days](https://data.winnipeg.ca/resource/6rcy-9uik.json)
