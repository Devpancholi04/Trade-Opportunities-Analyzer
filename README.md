# Trade Opportunities Analyzer

This project provides an API to analyze trade opportunities in the Indian stock market based on news data for specific sectors. It leverages web scraping, AI-powered analysis with Google Gemini, and rate limiting to provide a robust and informative service.

## Features and Functionality

*   **Sector-Specific Analysis:** Analyzes trade opportunities for a given sector in the Indian market.
*   **Data Scraping:** Scrapes news data from the web using DuckDuckGo search.
*   **AI-Powered Report Generation:** Uses Google's Gemini 1.5 Flash model to analyze scraped data and generate a markdown report with key trends, risks, and trade opportunities.
*   **API Endpoint:** Provides a FastAPI endpoint `/analyze/{sector}` to access the analysis.
*   **Authentication:** Implements basic HTTP authentication to secure the API.
*   **Rate Limiting:** Limits the number of requests per user per hour to prevent abuse.
*   **Session Management:** Manages user sessions with a configurable timeout.
*   **Markdown Report Saving:** Saves generated markdown reports to a file in the `reports/` directory.

## Technology Stack

*   **Python:** Primary programming language.
*   **FastAPI:** Web framework for building the API.
*   **Google Gemini 1.5 Flash:** AI model for market analysis.
*   **DuckDuckGo Search (DDGS):** For web scraping news data.
*   **python-dotenv:** For managing environment variables.
*   **uuid:** For generating unique session IDs.

## Prerequisites

Before running the application, ensure you have the following installed:

*   **Python 3.7+**
*   **pip** (Python package installer)

Additionally, you'll need a Google Cloud API key with access to the Gemini 1.5 Flash model.

## Installation Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Devpancholi04/Trade-Opportunities-Analyzer.git
    cd Trade-Opportunities-Analyzer
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```
    fastapi
    uvicorn[standard]
    python-dotenv
    google-generativeai
    ddgs
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add the following variables:

    ```
    api_key=<YOUR_GEMINI_API_KEY>
    myusername=<YOUR_USERNAME>
    mypassword=<YOUR_PASSWORD>
    ```

    Replace `<YOUR_GEMINI_API_KEY>`, `<YOUR_USERNAME>`, and `<YOUR_PASSWORD>` with your actual values.  These values are used for authentication and accessing the Gemini API.  The default username is `admin` and the default password is `123`.

## Usage Guide

1.  **Run the FastAPI application:**

    ```bash
    uvicorn main:app --reload
    ```

    This will start the server, typically on `http://127.0.0.1:8000`.

2.  **Access the API endpoint:**

    Use a tool like `curl` or Postman to make a GET request to the `/analyze/{sector}` endpoint. You will need to provide HTTP Basic authentication credentials in the request header.

    ```bash
    curl -X GET -u <YOUR_USERNAME>:<YOUR_PASSWORD> "http://127.0.0.1:8000/analyze/IT"
    ```

    Replace `<YOUR_USERNAME>` and `<YOUR_PASSWORD>` with the credentials you set in the `.env` file.  Replace "IT" with the sector you wish to analyze.

3.  **View the generated report:**

    The API will return the generated markdown report as a string in the response.  Additionally, the report is saved to a file named `reports/{sector} report.md` in the `reports/` directory.

## API Documentation

The API has one main endpoint:

*   **`GET /analyze/{sector}`**

    *   **Description:** Analyzes trade opportunities for a given sector.
    *   **Parameters:**
        *   `sector` (path parameter): The sector to analyze (e.g., "IT", "Finance"). Must be alphabetic and 3-32 characters long.
    *   **Authentication:** Requires HTTP Basic authentication.
    *   **Rate Limiting:** Limited to 10 requests per hour per user.
    *   **Returns:** A markdown-formatted string containing the analysis report.
    *   **Error Codes:**
        *   `400 Bad Request`: Invalid sector name.
        *   `401 Unauthorized`: Invalid credentials.
        *   `404 Not Found`: No data found for the specified sector.
        *   `429 Too Many Requests`: Rate limit exceeded.
        *   `502 Bad Gateway`: Data fetch failed.
        *   `503 Service Unavailable`: AI analysis failed.

## Contributing Guidelines

Contributions are welcome! To contribute to the project, follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Submit a pull request.

Please ensure your code follows the project's coding style and includes appropriate unit tests.

## License Information

This project does not currently have a license specified. All rights are reserved by the author.

## Contact/Support Information

For questions or support, please contact [Devpancholi04](https://github.com/Devpancholi04) by opening an issue on the GitHub repository.