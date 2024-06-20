# User Authentication

This project demonstrates a simple user authentication service using Python.

## Installation

1. Clone the repository:
git clone https://github.com/Kosuri-Pavan-Akhil/User_Authentication.git
cd user-authentication


2. Install dependencies:
pip install -r requirements.txt


## Usage

1. Set up your environment variables in a `.env` file:
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url

2. Run the application:
python app/main.py


3. Access the API documentation:
Open your browser and go to `http://localhost:8000/docs` to view Swagger UI with API endpoints.

## Project Structure

├── app
│ ├── main.py # Entry point of the application
│ ├── routers
│ │ ├── auth.py # Authentication routes
│ │ └── ...
│ ├── services
│ │ ├── auth.py # Authentication logic
│ │ └── ...
│ └── ...
├── tests # Unit tests
│ └── ...
├── .env # Environment variables configuration
└── README.md # This file


The project structure includes main files for application entry (`main.py`), authentication routes (`auth.py`), authentication logic (`auth.py` in services), unit tests directory (`tests`), and a configuration file for environment variables (`.env`).

## Features

- User registration and authentication
- JWT token generation and verification
- Secure password hashing and validation

## Contributing

Contributions are welcome! To contribute to this project:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature`.
3. Commit your changes and push to your forked repository.
4. Submit a pull request with a clear description of your changes.

Please follow the existing code style and conventions used in the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

