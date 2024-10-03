# Animals API Client

## Setup

1. Clone the repository.
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the script:
    ```
    python src/main.py
    ```

## Notes
- This script will fetch all animals from the API, transform their data, and post them in batches to the `/home` endpoint.
- Handles retries and server errors with exponential backoff.