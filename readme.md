# Admin Panel and API Documentation

## Accessing the Admin Panel

To access the admin panel, use the following credentials:

- **Username:** `admin`
- **Password:** `admin`

## Testing the API

You can test the API using the following endpoints:

### 1. Menu Items

- **Endpoint:** `/api/menu-items/`
- **Description:** Retrieve a list of menu items available with CRUD.

### 2. Restaurant Booking

- **Endpoint:** `/restaurant/booking/`
- **Description:** Manage restaurant bookings. You can create, view, update, or delete bookings through this endpoint.

### 3. API Token Authentication

- **Endpoint:** `/restaurant/api-token-auth/`
- **Description:** Obtain an API token for authenticated requests. This endpoint is used to authenticate users and provide them with a token to access protected resources.

## Usage

1. **Access the Admin Panel:**
   - Navigate to the admin panel URL.
   - Enter the provided credentials to log in.

2. **Test the API Endpoints:**
   - Use tools like `curl`, Postman, or any HTTP client to send requests to the specified endpoints.
   - Ensure you include the necessary headers and parameters for each request.

## Example Requests

### Get Menu Items

```bash
curl -X GET http://127.0.0.1:8000/api/menu-items/
