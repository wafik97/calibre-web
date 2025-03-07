# Calibre Web - ReadingSync Feature


This project is a **Calibre Web** application that manages eBook collections. It includes a custom feature, **Read-Sync**, developed in a separate repository, which allows real-time synchronization of reading progress across multiple users viewing the same PDF.

## Features

- **ReadingSync**: A feature developed to synchronize reading progress in real time among users viewing the same PDF.
    - This feature is in a separate repository: [ReadingSync](https://github.com/wafik97/readingSync).
- **UI & API Tests**: Automated tests to ensure the correct functionality of the user interface and API.
    - The **API tests** focus on the **Calibre Desktop app**, which shares the same database as Calibre Web. These tests validate the operations of adding books to the database.
- **Testing Phases**:
    1. **Build Phase**: Triggered after a commit and push to the repository. Includes linting and unit tests.
    2. **Integration Phase**: Tests the interaction between different components in the system.
    3. **Pre-production Phase**: Ensures the application is production-ready by testing performance and load handling.

## Workflow

### 1. Build Phase

- Triggered after a commit and push to the repository.
- **Linting** and **unit tests** are executed through GitHub Actions to check for code quality and functionality.

### 2. Docker Update

- After successful tests, the **Docker image** for the Calibre Web project is updated and pushed to Docker Hub.
- The project uses **Docker Compose** for running Calibre Web, including the ReadingSync feature, with the following command:
  ```bash
  docker-compose up
  ```


### 3. Pull Request and Testing

- After updating the Docker image, a **Pull Request** (PR) is created.
- The PR triggers the following tests:
    - **UI Tests**: These tests verify the correct functionality of the user interface, ensuring that all features, including ReadingSync, work seamlessly within Calibre Web.
    - **API Tests**: These tests focus on the **Calibre Desktop app** and its interactions with the shared database, specifically testing operations related to adding books to the database.

  The tests are run through **GitHub Actions**, which automates the process after the PR is created.

### 4. Load Testing

- Once the PR is merged and the new features are integrated, **load tests** are triggered using **Locust**. These tests simulate various real-world usage patterns and ensure that the system can handle different levels of traffic and load.
- The load tests include three different test scenarios to simulate different usage situations, ensuring the application can scale and perform under stress.

## Ports

- **Calibre Web**: `8083`
- **ReadingSync (Separate Repository)**: `8080`

## Repositories

- **Calibre Web Project**: [GitHub - Calibre Web](https://github.com/wafik97/calibre-web)
- **ReadingSync Feature**: [GitHub - ReadingSync](https://github.com/wafik97/readingSync)
- **Calibre Web API Tests**: [GitHub - API Calibre Web](https://github.com/wafik97/API_calibre_web)

## Requirements

- Docker
- Docker Compose
- GitHub Actions
- Locust (for load testing)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/wafik97/calibre-web.git
   cd calibre-web
   ```

2. Build the project:
   ```bash
   docker-compose build
    ```

3. Run the project:
   ```bash
   docker-compose up
    ```

4. Run the tests:
    - **UI and API tests** are automatically triggered via **GitHub Actions** when a Pull Request is created.
    - **Load tests** can be manually triggered after a PR is merged using **Locust**:
        1. Install Locust:
           ```bash
           pip install locust
           ```
        2. Run Locust:
           ```bash
           locust -f locustfile.py
           ```

5. To stop the project:
    - You can stop the running services by pressing `Ctrl+C` in the terminal or using the following command:
      ```bash
      docker-compose down
      ```

6. Access the project:
    - Once the project is running, you can access **Calibre Web** at:
        - `http://localhost:8083`
    - For **ReadingSync** (if running in a separate container or repo):
        - `http://localhost:8080`


# Calibre-Web

Calibre-Web is a web app that offers a clean and intuitive interface for browsing, reading, and downloading eBooks using a valid [Calibre](https://calibre-ebook.com) database.

[![License](https://img.shields.io/github/license/janeczku/calibre-web?style=flat-square)](https://github.com/janeczku/calibre-web/blob/master/LICENSE)
![Commit Activity](https://img.shields.io/github/commit-activity/w/janeczku/calibre-web?logo=github&style=flat-square&label=commits)
[![All Releases](https://img.shields.io/github/downloads/janeczku/calibre-web/total?logo=github&style=flat-square)](https://github.com/janeczku/calibre-web/releases)
[![PyPI](https://img.shields.io/pypi/v/calibreweb?logo=pypi&logoColor=fff&style=flat-square)](https://pypi.org/project/calibreweb/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/calibreweb?logo=pypi&logoColor=fff&style=flat-square)](https://pypi.org/project/calibreweb/)
[![Discord](https://img.shields.io/discord/838810113564344381?label=Discord&logo=discord&style=flat-square)](https://discord.gg/h2VsJ2NEfB)

![Main screen](https://github.com/janeczku/calibre-web/wiki/images/main_screen.png)


## Installation

### Installation via pip (recommended)

1. **Create a virtual environment**: It’s essential to isolate your Calibre-Web installation to avoid dependency conflicts. You can create a virtual environment by running:
   ```
   python3 -m venv calibre-web-env
   ```
2. **Activate the virtual environment**:
   ```
   source calibre-web-env/bin/activate
   ```
3. **Install Calibre-Web**: Use pip to install the application:
   ```
   pip install calibreweb
   ```
4. **Start Calibre-Web**: After installation, you can start the application with:
   ```
   cps
   ```


## Quick Start

1. **Access Calibre-Web**: Open your browser and navigate to:
   ```
   http://localhost:8083
   ```
   or for the OPDS catalog:
   ```
   http://localhost:8083/opds
   ```
2. **Log in**: Use the default admin credentials:
   - **Username:** admin
   - **Password:** admin123
3. **Database Setup**: If you do not have a Calibre database, download a sample from:
   ```
   https://github.com/janeczku/calibre-web/raw/master/library/metadata.db
   ```
   Move it out of the Calibre-Web folder to avoid overwriting during updates.
4. **Configure Calibre Database**: In the admin interface, set the `Location of Calibre database` to the path of the folder containing your Calibre library (where `metadata.db` is located) and click "Save".
5. **Google Drive Integration**: For hosting your Calibre library on Google Drive, refer to the [Google Drive integration guide](https://github.com/janeczku/calibre-web/wiki/G-Drive-Setup#using-google-drive-integration).
6. **Admin Configuration**: Configure your instance via the admin page, referring to the [Basic Configuration](https://github.com/janeczku/calibre-web/wiki/Configuration#basic-configuration) and [UI Configuration](https://github.com/janeczku/calibre-web/wiki/Configuration#ui-configuration) guides.

## Requirements

- **Python Version**: Ensure you have Python 3.7 or newer.
- **Imagemagick**: Required for cover extraction from EPUBs. Windows users may also need to install [Ghostscript](https://ghostscript.com/releases/gsdnld.html) for PDF cover extraction.
- **Optional Tools**:
   - **Calibre desktop program**: Recommended for on-the-fly conversion and metadata editing. Set the path to Calibre’s converter tool on the setup page.
   - **Kepubify tool**: Needed for Kobo device support. Download the tool and place the binary in `/opt/kepubify` on Linux or `C:\Program Files\kepubify` on Windows.
