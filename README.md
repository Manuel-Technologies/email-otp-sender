# Email OTP Sender

A secure and reliable email OTP sender for developers.

## Features

*   Send OTPs, verification codes, and confirmation codes via email.
*   Securely manage credentials using environment variables.
*   Easy to integrate into any Python project.
*   Simple Flask API for sending OTPs.

## Getting Started

### Prerequisites

*   Python 3.6 or higher
*   A Gmail account with "Less secure app access" enabled.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Manuel-Technologies/email-otp-sender.git
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  Create a `.env` file in the root of the project.
2.  Add the following lines to the `.env` file:
    ```
    SENDER_EMAIL="your_email@example.com"
    PASSWORD="your_password"
    ```
    Replace `"your_email@example.com"` and `"your_password"` with your Gmail credentials.

### Usage

```python
from main import send_otp_email

send_otp_email("recipient@example.com", "Your OTP Code", "123456")
```

### API Usage

To run the Flask API, run the following command:

```bash
python api.py
```

You can then send a POST request to `http://127.0.0.1:5000/send-otp` with the following JSON body:

```json
{
    "recipient_email": "recipient@example.com",
    "subject": "Your OTP Code",
    "otp": "123456"
}
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License.
