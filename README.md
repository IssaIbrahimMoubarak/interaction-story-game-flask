# Project Title: Interactive Story Game

#### Description

An interactive story game where users navigate through a story by making choices at various decision points. Each decision affects the outcome of the story, leading to different paths and endings. The game features dynamic background colors and images to enhance the storytelling experience.

#### Features

- Interactive story with multiple paths and endings
- Dynamic background colors based on the mood of the situation
- Unique images for each part of the story
- Simple and intuitive interface

#### Technologies Used

- Flask (Python)
- HTML
- CSS
- JSON

#### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/interactive-story-game.git
   cd interactive-story-game
   ```
2. **Create a virtual environment:**

   ```sh
   python3 -m venv venv
   ```
3. **Activate the virtual environment:**

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. **Install the dependencies:**

   ```sh
   pip install Flask
   ```

#### Usage

1. **Run the Flask app:**

   ```sh
   python app.py
   ```
2. **Open your web browser and navigate to:**

   ```
   http://127.0.0.1:5000
   ```
3. **Start the interactive story by making your choices and exploring different paths.**

#### Project Structure

```
project/
│
├── app.py                      # Flask application
├── data/
│   └── nodes.json              # JSON file containing story nodes
├── static/
│   ├── css/
│   │   └── styles.css          # CSS styles
│   └── images/                 # Folder containing story images
│       ├── forest.jpg
│       ├── wolf.jpg
│       ├── treasure_map.jpg
│       ├── secret_passage.jpg
│       ├── lost_forest.jpg
│       ├── treasure.jpg
│       ├── forest_exit.jpg
│       ├── temple.jpg
│       ├── forest_path.jpg
│       ├── rescue.jpg
│       ├── wealth.jpg
│       ├── safe_exit.jpg
│       └── hero.jpg
└── templates/
    └── index.html              # HTML template for the story
```

#### Customization

To customize the story or add new paths, update the `nodes.json` file in the `data` directory. Each node in the JSON file represents a part of the story and includes the text, image, choices, and background color.

Example node structure in `nodes.json`:

```json
{
    "node_key": {
        "text": "Story text here.",
        "image": "images/your_image.jpg",
        "choices": {
            "Choice 1 text": "next_node_key",
            "Choice 2 text": "another_node_key"
        },
        "color": "#FFFFFF"  // Background color for this node
    }
}
```

#### License

This project is licensed under the MIT License.

#### Contact

For any questions or suggestions, please contact ISSA IBRAHIM Moubarak at 2im.moubarak@gmail.com.
