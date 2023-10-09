1. Fork this repo, make sure you're on the **main** branch, pull changes
1. Create an .env file in the root with that vars:

    ```
    #* general
    DEBUG=true
    RELOAD=true
    APP_HOSTNAME=
    APP_PORT_EXPOSE=80
    OPENAPI_URL=/openapi.json
    DOCS_URL=/docs
    REDOC_URL=/redoc

    #* telegram bot
    BOT_TOKEN=

    #* database
    DATABASE_DRIVER=postgresql+asyncpg
    DATABASE_USERNAME=postgres
    DATABASE_PASSWORD=postgres
    DATABASE_HOSTNAME=database
    DATABASE_PORT=5432
    DATABASE_PORT_EXPOSE=5432
    DATABASE_NAME=postgres

    #* redis
    REDIS_HOST=redis
    REDIS_PORT=6379

    #* redis commander
    REDIS_COMMANDER_PORT=18777
    REDIS_COMMANDER_USER=rcommander
    REDIS_COMMANDER_PASSWORD=rcommander
    ```
    Fill in all the empty variables (don't forget to enter your bot token in the .env file)
    </br>

1. Install all dependencies via [poetry](https://python-poetry.org/docs/):

    ```
    poetry install
    ```
    It's needed for all packages to be seen by your ide in the imports
    </br>

1. Activate your virtual environment with:
    ```
    poetry shell
    ```

1. Install pre-commit hook for auto locking poetry:

    ```
    pre-commit install
    ```

1. Build the project with command: 
    ```
    make build
    ```

1. Migrate models to db with command:
    ```
    make migrations
    ```

1. Run the project with command:
    ```
    make app
    ```

For more useful commands see **Makefile**.
</br>
Don't forget to setup webhook for your bot (use **nginx** or **cloudflare** tunnel if you're developping locally).

</br>


Have fun developing ✌️
