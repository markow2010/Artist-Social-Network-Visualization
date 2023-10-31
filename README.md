# Artist Social Network Visualization

**Table of Contents**
- [Artist Social Network Visualization](#artist-social-network-visualization)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Project Structure](#project-structure)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

The Artist Social Network Visualization project is a Python web application that allows users to explore and visualize relationships between artists in a social network. It uses the Flask web framework and Bokeh for graph visualization. This GitHub repository provides the source code for the project.

The main features of this application include:
- Interactive artist selection and network expansion.
- Visualization of artist networks using Bokeh.
- Calculation of various centrality measures for the artists.

## Getting Started

To get started with the Artist Social Network Visualization project, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/yourusername/artist-social-network.git
   ```

2. Navigate to the project directory:

   ```
   cd artist-social-network
   ```

3. Install the required dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```
   python app.py
   ```

The application should now be accessible in your web browser at `http://localhost:5000`.

## Project Structure

The project's directory structure is as follows:

- `app.py`: The main Flask application file containing the web server and route definitions.
- `guilayer`: Contains files related to the user interface.
- `applayer`: Contains files that handle the application's core logic.
- `templates`: Contains HTML templates for rendering pages.
- `static`: Contains static files such as CSS and JavaScript.
- `requirements.txt`: Lists the project's Python dependencies.

## Usage

1. Launch the application by running `app.py`.
2. Open your web browser and go to `http://localhost:5000` to access the main page.
3. Use the provided form to select an artist and adjust the network expansion options.
4. Explore the artist social network graph.
5. Various centrality measures will be calculated and displayed.

## Contributing

If you would like to contribute to the Artist Social Network Visualization project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them.
4. Push your changes to your fork: `git push origin feature/your-feature-name`.
5. Create a pull request on the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.