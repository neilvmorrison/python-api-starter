.PHONY: setup activate dev

setup:
	touch .env && \
	cp .env.sample .env && \
	python3 -m venv .venv && \
	uv sync

dev:
	export PORT=$$(grep '^PORT' .env | cut -d '=' -f 2) && \
	uvicorn main:app --reload --port $${PORT:-8000}
