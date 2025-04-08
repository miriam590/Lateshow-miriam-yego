# Late Show API

A Flask API for tracking episodes, guests, and appearances on a late night talk show.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/miriam590/late-show-api.git
   cd late-show-api
   ```
2. Create and activate a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
5. Seed the database (optional):
   ```bash
   python seed.py
   ```
6. Run the application:
   ```bash
   python app.py
   ```

## API Endpoints

### GET /episodes
Returns all episodes in the database.

### GET /episodes/:id
Returns a specific episode with its appearances.

### GET /guests
Returns all guests in the database.

### POST /appearances
Creates a new appearance with:
- rating (1-5)
- episode_id
- guest_id

## Models

- **Episode**: Represents a show episode
- **Guest**: Represents a guest on the show
- **Appearance**: Represents a guest's appearance on an episode

## Validations

- Appearance rating must be between 1 and 5 (inclusive)
