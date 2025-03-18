# E-commerce Product Catalog API

A FastAPI-based RESTful API for managing product catalogs in an e-commerce platform. This API handles product details, categories, and inventory tracking.

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── product.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── product.py
│   └── routes/
│       ├── __init__.py
│       └── product.py
├── tests/
│   ├── __init__.py
│   ├── test_products.py
│   └── conftest.py
├── requirements.txt
└── README.md
```

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **PostgreSQL**: Database for storing product information
- **pytest**: Testing framework

## Implementation Plan

### 1. Project Setup
- Initialize project structure
- Set up virtual environment
- Install required dependencies
- Configure database connection

### 2. Database Models
- Create Product model with fields:
  - id (UUID)
  - name
  - description
  - price
  - category
  - stock_quantity
  - created_at
  - updated_at

### 3. API Schemas
- Define Pydantic models for:
  - Product creation
  - Product update
  - Product response

### 4. API Endpoints

Implement the following RESTful endpoints:

#### Products
- `GET /products`: List all products with pagination
- `GET /products/{product_id}`: Get product details
- `POST /products`: Create new product
- `PUT /products/{product_id}`: Update product
- `DELETE /products/{product_id}`: Delete product

#### Additional Features
- `GET /products/category/{category}`: Filter products by category
- `GET /products/search`: Search products by name/description

### 5. Error Handling
- Implement proper error responses
- Add input validation
- Handle edge cases

### 6. Testing Strategy

#### Unit Tests
- Test individual components (models, schemas)
- Validate input/output schemas
- Test business logic

#### Integration Tests
- Test API endpoints
- Test database operations
- Test error handling

#### Test Coverage
- Aim for >80% code coverage
- Include edge cases and error scenarios

## Setup Instructions

1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables
5. Run database migrations
6. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

Once the server is running, access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development Guidelines

1. Follow PEP 8 style guide
2. Write docstrings for all functions
3. Add type hints
4. Write tests for new features
5. Update documentation when adding features

## Future Enhancements

1. Authentication and authorization
2. Rate limiting
3. Caching layer
4. Image upload support
5. Bulk operations
6. Versioning support