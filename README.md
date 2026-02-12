# 🚀 CRUD API with Python & Docker

This is a study project implementing a user registration API (CRUD) using **Python** with the **Flask** framework and **PostgreSQL**, all orchestrated via **Docker**.

---

## 🛠 Tech Stack

* **Language:** Python 3.9
* **Web Framework:** [Flask](https://flask.palletsprojects.com/)
* **Database:** [PostgreSQL](https://www.postgresql.org/)
* **Database Driver:** Psycopg2
* **Containerization:** Docker & Docker Compose

---

## 🏗 Project Structure

The project runs two main services:
1.  **App:** The Flask application running on port `8000`.
2.  **DB:** The PostgreSQL database running on port `5432`.

---

## 🚦 How to Run

You need to have **Docker** and **Docker Compose** installed on your machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Deni-jpg/Docker-CRUD.git](https://github.com/Deni-jpg/Docker-CRUD.git)
    cd Docker-CRUD
    ```

2.  **Spin up the containers:**
    ```bash
    docker-compose up --build
    ```

3.  **Initialize the Database:**
    Open your browser and visit the following route to automatically create the `users` table:
    > `http://localhost:8000/init`

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Checks if the database connection is OK |
| `GET` | `/init` | Creates the `users` table in the database |
| `GET` | `/users` | Returns a list of all registered users |
| `POST` | `/users` | Creates a new user (Expects JSON body) |
| `GET` | `/health` | Simple health check for the API |

---

## 📝 Testing with Postman

1. Open **Postman** and create a new request.
2. Set the method to **POST** and the URL to `http://localhost:8000/users`.
3. Go to the **Body** tab, select **raw**, and change the type to **JSON**.
4. Paste the following JSON:
   ```json
   {
     "name": "John Doe"
   }
