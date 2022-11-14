# Projects
If/when you clone this repository, I highly recommended changing into the directory of the specific project that you want to start up.
<details>
  <summary>Project 1: docker-compose</summary>
  <ul>

  ## Project 1: docker-compose
  This project focused on creating a simple HTML, CSS, and/or JavaScript page that displays "Hello BeyondMD!". Then dockerize 
  and run using docker-compose.

  ---
  ### Installation & Running
  Insure that you have docker and docker-compose installed. I also recommend installing Docker Desktop.

  Within your terminal you can type in `docker-compose up`. After that, go to your web browser and type in `localhost:8000`.
  </ul>
</details>
<details>
  <summary>Project 2: React App with MUI</summary>
  <ul>

  ## Project 2: React App with MUI
  This project focused on creating a React app using MUI with different features. In this case, it's able to display "Hello BeyondMD", display my resume (I did not upload my resume), and display data from a free 3rd party API.

  ---
  ### Installation & Running
  When you clone this repository you are missing two things. Those two things are node_modules folder and .env file.

  In your terminal type in `npm ci` to get your node_modules folder.

  Your .env file only will contain one variable. Ensure the .env file is in project 2 directory.
  * `REACT_APP_OPENWEATHERMAP_API="ENTER YOUR OPEN WEATHER MAP API KEY HERE"`
  <br></br>

  You can obtain this API key for free at [Open Weather Map](https://openweathermap.org/api).

  If you have your node_modules folder and .env file set up, you can type in `npm run build` then `npm start`.

  NOTE: I uploaded a resume template instead of my own actual resume.
  </ul>
</details>
<details>
  <summary>Project 3: CRUD Django-Postgres App</summary>
  <ul>

  ## Project 3: CRUD Django-Postgres App
  This project focused on creating a Django-Postgres App with CRUD operations and using data from a free 3rd party API. The project can run with or without docker.

  ---
  ### Dependencies
  If you choose to run this with docker-compose you can ignore this. Just make sure that docker and docker-compose are installed. I also recommend installing Docker Desktop. If you choose not to run with docker-compose you will need to install some dependencies.

  When you clone this repository you will find a requirments.txt file which contains the dependencies to install. You will also need to install postgres. I'm using postgres on WSL (Windows Subsystem for Linux).

  ### Env File
  To get started, you should set up your .env file. Ensure the .env file is in project 3 directory. We will use environment variables instead of hard coding potentially sensitive information. There are a total of 6 variables for non-docker-compose and 9 for docker-compose. For now, we can just use the default database of postgres.
  * `TMDB_KEY="ENTER YOUR THE TMDB API KEY HERE"`
  * `DB_NAME="postgres"`
  * `DB_USER="postgres"`
  * `DB_PASSWORD="postgres"`
  * `DB_HOST="localhost"`
  * `DB_PORT="5432"`
  <br></br>

  If you are running docker-compose, you will need to change one variable and add 3 new variables. For now, we can just use the default database of postgres.
  * `DB_HOST="db"` | *change from "localhost" to "db"*
  * `POSTGRES_DB="postgres"`
  * `POSTGRES_USER="postgres"`
  * `POSTGRES_PASSWORD="postgres"`

  ### Running (without docker-compose)
  We need to start the database before opening the app. We can do so with `sudo service postgresql start`. We also need to create the database tables for the app. We can do so with `python3 manage.py migrate`.

  This should create all the tables in the database and your app is ready to go. Type in `python3 manage.py runserver`. Go to your browser and type in `127.0.0.1:8000`.

  ### Running (with docker-compose)
  If you are running docker-compose and have Docker Desktop, you can type in `docker-compose up`. You will then need to open the terminal of the app in the container on Docker Desktop. Once opened, type in `python3 manage.py migrate`.

  If you are running docker-compose and don't have Docker Desktop, you can type in `docker-compose up -d --build`. Then type in `docker-compose exec app python3 manage.py migrate`.

  This should create all the tables in the database and your app is ready to go. Either way will work and it's up to you. In your browser type in `localhost:8000`.

  ### Useful Links
  More about TMDB's API and how to obtain an API key can be found on [developers.themoviedb.org](https://developers.themoviedb.org/3/getting-started/introduction) or [themoviedb.org](https://www.themoviedb.org/documentation/api?language=en-US).

  Information on how to setup postgres on WSL can be found on [WSL Database](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database)

  Setting up Docker for WSL can be found on [Docker for WSL](https://docs.docker.com/desktop/windows/wsl/).
  </ul>
</details>
