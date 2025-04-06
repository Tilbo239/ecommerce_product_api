# E-commerce Product API

The **E-commerce Product API** is a Django-based application designed to handle core e-commerce functionalities such as user management, product catalog, reviews, discount management, and order processing.

---

## Project Structure

This project consists of the following main Django apps:

- `users`: Manage user accounts and authentication.
- `products`: Manage product catalog and images.
- `reviews`: Handle product reviews.
- `discount`: Manage discounts and promotional offers.
- `orders`: Manage customer orders.

---
## Quick Start

#### Step 1: Create a virtual environment

```bash
python -m venv venv
```

#### Step 2: Activate the virtual environment

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

#### Step 3: Install dependencies

```bash
pip install -r requirements.txt


### 4. Run database migrations

```bash
python manage.py migrate
```

---

### Step 4. Start server

```bash
python manage.py runserver
```

---

### Step 5. Access API Endpoints

You can test the endpoints using Postman or curl. Here's a list of some endpoints:
### User Endpoints

   - **User Registration:** `POST /api/register/`
   - **Token Retrieval:** `POST /api/login/`
   - **Token Refresh:** `POST /api/users/token/refresh/`

     ### Category Endpoints

   - **Category Management:** `GET/POST/PUT/DELETE /api/categories/`

   ### Product Endpoints

   - **Product Management:** `GET/POST/PUT/DELETE /api/products/`
   - **Add Review:** `POST /api/products/<int:pk>/reviews/new/`
   - **Product Reviews:** `GET /api/products/<int:pk>/reviews/`

   ### Review Endpoints

   - **Review List:** `GET /api/reviews/`
   - **Review Detail:** `GET/PUT/DELETE /api/reviews/<int:pk>/`

   ### Wishlist Endpoints

   - **Add to Wishlist:** `POST /api/products/<int:pk>/wishlists/add/`
   - **Wishlist Management:** `GET /api/wishlists/`
   - **Wishlist Detail:** `GET/PUT/DELETE /api/wishlists/<int:pk>/`

   ### Order Endpoints

   - **Order Processing:** `GET/POST /api/orders/`

   ### Discount Endpoints

   - **Discount Management:** `GET/POST/PUT/DELETE /api/discounts/`

 

## API Documentation

This project uses **drf-spectacular** for API schema generation and documentation.

### Documentation Endpoints

- **Schema (YAML):** `http://127.0.0.1:8000/api/schema/`
- **Swagger UI:** `http://127.0.0.1:8000/api/schema/swagger-ui/`
- **Redoc UI:** `http://127.0.0.1:8000/api/schema/redoc/`

### Setup Instructions

Follow this link to know more about 
https://github.com/tfranzel/drf-spectacular/

## Admin Panel

Access Django Admin to manage backend data:

- URL: `http://127.0.0.1:8000/admin/`

---

## Summary

This API provides full-featured e-commerce functionality with robust, well-documented endpoints thanks to `drf-spectacular`. Easily scalable and customizable for any retail application.