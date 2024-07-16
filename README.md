
# Bingo - Multiplayer Interactive Game

## Introduction

Bingo is a dynamic multiplayer game built with Python, inspired by the classic Mario series. Leveraging Tkinter, Pygame, OpenCV, and MySQL, this project offers a comprehensive setup, including user registration, email verification, and a rich gaming interface. Players can enjoy interactive gameplay with real-time updates, set against a vibrant and engaging graphical backdrop reminiscent of the beloved Mario universe. The repository is well-organized to facilitate ease of use, maintenance, and further development. Perfect for developers interested in game development, network programming, and GUI design.

## Setup Instructions

### Prerequisites

1. **Python 3.x**: Ensure you have Python 3.x installed.
2. **Pip**: Python package installer.
3. **MySQL**: Install MySQL Server for database management.

### Required Python Packages

Install the required packages using pip:

```bash
pip install pygame opencv-python pillow mysql-connector-python
```

### Database Setup

1. Start your MySQL server.
2. Create a database named `game`.
3. Run the SQL script `db.sql` to create the necessary tables.

```sql
CREATE DATABASE game;
USE game;

-- Create tables
-- Add your SQL commands here from db.sql file
```

### Email Setup

For email verification, the application uses Gmail's SMTP server. Update the `sign-up.py` file with your email credentials.

```python
email_s = 'your-email@gmail.com'
email_psd = 'your-app-password'  # Use an app-specific password for better security
```

### Running the Application

1. Start the server:

```bash
python server/server12.py
```

2. Run the game client:

```bash
python client/client.py
```

Alternatively, you can run both the server and game using `testi.py`:

```bash
python tests/testi.py
```

## File Descriptions

### Main Game Files

- **network.py**: Handles the network connection for the client, including connecting to the server, sending data, and receiving data.
- **server12.py**: Sets up a server that listens for connections and handles multiple clients using threads.
- **client.py**: Implements a Pygame client that connects to the server, handles player movement, and draws the game state.
- **Interface_game.py**: The main game interface implemented using Pygame, including player movement, enemy interaction, and level design.

### User Interface Files

- **first.py**: Uses Tkinter and OpenCV to create a GUI application with a video background, playing a sound using Pygame.
- **sign-in.py**: Implements a sign-in form using Tkinter, connects to a MySQL database to validate user credentials, and starts a new interface on successful login.
- **sign-up.py**: Implements a registration form using Tkinter, connects to a MySQL database to store user information, and sends a verification email with a code to the user.
- **verfication_email.py**: Provides an interface for users to input a verification code sent to their email.
- **playerInterface.py**: Uses Tkinter and OpenCV for another GUI application, possibly a player interface, and interacts with the database.
- **parametre.py**: Provides a settings interface for the game, allowing the user to change their name, email, and password.

### Supporting Files

- **db.sql**: Contains SQL commands to set up the database for the game.
- **testi.py**: Runs the server and then the game using subprocesses. It ensures the server is started before launching the game.
- **tempCodeRunnerFile.py**: A temporary file likely used for testing purposes.

## Usage

1. **Starting the Server**: Run `server12.py` to start the game server.
2. **Running the Client**: Run `client.py` to start the game client and connect to the server.
3. **Registration and Login**:
   - Run `sign-up.py` to create a new user account.
   - Run `sign-in.py` to log in with an existing account.
   - Run `verfication_email.py` to verify email addresses.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with your changes.

## Developers

- [@Simo Nachit](https://github.com/your-github-username)
- [@Ayoub ezzaaraoui](https://github.com/ezzaaraoui)

## License

This project is licensed under the MIT License.
