Certainly! Here's the updated `README.md` file based on your provided project structure and Docker setup:

```markdown
# E-commerce Web App

Welcome to our E-commerce Web App! This project contains all the necessary components for building an e-commerce platform. Follow the steps below to set up and run the application using Docker.

## Getting Started

### 1. Clone the Repository
```bash
$ git clone https://github.com/07x/ecom_web_pro.git
```

### 2. Install Docker
Make sure you have Docker installed on your system. You can download it from [Docker's official website](https://www.docker.com/get-started).

### 3. Build and Run the Docker Container
```bash
$ cd ecom_web
$ docker-compose up --build
```

This command will build the Docker image and start the container. Once the container is up and running, you can access your E-commerce Web App at http://localhost:8000.

## Project Structure
```
ecom_web/
├── ecom_web/
│   ├── shop/
│   ├── userapp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── plans.md
└── requirements.txt
```

## Contributing
This project is open for contributions! Whether it's adding new features, fixing bugs, or improving documentation, we welcome your contributions. Please fork the repository, make your changes, and submit a pull request.

For any inquiries or feedback, please contact [abhinavsrivasta421@gmail.com](mailto:your-email@example.com).

Happy coding!
```

This `README.md` file provides clear instructions on how to clone the repository, set up Docker, build and run the Docker container, and access the E-commerce Web App. It also includes information about the project structure and how to contribute to the project.