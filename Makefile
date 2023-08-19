# =============================== VARIABLES =================================

docker_compose_v2 = docker compose

app_dir = app
compose_dir = docker/compose

main_container = -f $(compose_dir)/main.yml
app_container = -f $(compose_dir)/app.yml
database_container = -f $(compose_dir)/database.yml
alembic_container = -f $(compose_dir)/alembic.yml
redis_container = -f $(compose_dir)/redis.yml
celery_container = -f $(compose_dir)/celery.yml

compose_app = $(docker_compose_v2) $(main_container) $(app_container) $(database_container) $(redis_container) $(celery_container)
compose_migrations = $(docker_compose_v2) $(main_container) $(alembic_container)

# ===========================================================================

# ================================= SYSTEM ==================================

.PHONY: clean
clean:
	rm -rf `find . -type f -name '*.py[co]'`
	rm -rf `find . -type f -name '*~'`
	rm -rf `find . -type f -name '.*~'`
	rm -rf {.cache,.ruff_cache,.mypy_cache,.coverage,htmlcov,.pytest_cache}

# ===========================================================================

# ================================ COMMON ===================================

.PHONY: build all composes
build:
	$(compose_app) build
	$(compose_migrations) build

.PHONY: stop all composes
stop:
	$(compose_app) stop
	$(compose_migrations) stop

.PHONY: down all composes
down:
	$(compose_app) down
	$(compose_migrations) down

.PHONY: destroy all composes
destroy:
	$(compose_app) down -v
	$(compose_migrations) down -v

# ===========================================================================

# ================================== APP ====================================

.PHONY: build app
app-build:
	$(compose_app) build

.PHONY: run app in background 
app-d:
	$(compose_app) up -d

.PHONY: run app
app:
	$(compose_app) up

.PHONY: restart app in background
app-restart-d:
	$(compose_app) stop
	$(compose_app) up -d

.PHONY: restart app
app-restart:
	$(compose_app) stop
	$(compose_app) up

.PHONY: stop app
app-stop:
	$(compose_app) stop

.PHONY: down app
app-down:
	$(compose_app) down

.PHONY: destroy app
app-destroy:
	$(compose_app) down -v

# ===========================================================================

# ============================== MIGRATIONS =================================

.PHONY: build migrations
migrations-build:
	$(compose_migrations) build

.PHONY: run migrations
migrations:
	$(compose_migrations) up

.PHONY: stop migrations
migrations-stop:
	$(compose_migrations) stop

.PHONY: down migrations
migrations-down:
	$(compose_migrations) down

.PHONY: destroy migrations
migrations-destroy:
	$(compose_migrations) down -v

# ===========================================================================
