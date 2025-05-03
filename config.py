# config.py
ALPHA_VANTAGE_API_KEY = 'YOUR_API_KEY_HERE' # Replace with your Alpha Vantage key

# --- MySQL Credentials ---
# !! Strongly recommend using environment variables or a secure vault !!
# !! Do NOT commit this file with real credentials to public GitHub !!
MYSQL_HOST = 'localhost'  # Or your MySQL server address if different
MYSQL_USER = 'YOUR_MYSQL_USERNAME_HERE' # Replace with your MySQL username (e.g., 'root' or a dedicated user)
MYSQL_PASSWORD = 'YOUR_MYSQL_PASSWORD_HERE' # Replace with your password
MYSQL_DATABASE = 'stock_market_db' # The database you created