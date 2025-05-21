.PHONY: intall-requirements
requirements:
	@echo "📦 Installing requirements..."
	pip install -r requirements.txt

.PHONY: freeze-requirements
freeze-requirements:
	@echo "📦 Freezing requirements..."
	pip freeze > requirements.txt

.PHONY: run
run:
	@echo "🚀 Running agent..."
	PYTHONPATH=. python app/main.py