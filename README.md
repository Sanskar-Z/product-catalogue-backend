# Product Catalogue Backend (Python)

A small Flask + SQLite product catalogue demonstrating CRUD operations, search by name/category/availability, pytest model/API tests, and Behave BDD scenarios.

## Setup

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run the service

```bash
python app.py
```

Endpoints:
- `POST /products` create a product (JSON)
- `GET /products` list all products
- `GET /products?name=lamp` search by name
- `GET /products?category=Home` search by category
- `GET /products?available=true` search by availability
- `GET /products/1` read one product
- `PATCH /products/1` update a product
- `DELETE /products/1` delete a product

## Tests

```bash
pytest -q
```

The BDD feature and step files are included under `features/`. The step definitions exercise the model layer directly and can be run with Behave after installing the requirements.

## Important for Coursera submission

This is a standalone reference implementation created to match the file paths and operations listed in the assignment. Your course may expect additional starter-code conventions or specific UI/browser steps. Run tests and compare with your lab's instructions before submitting. Do not claim this is your original course repository unless you have adapted and verified it.
