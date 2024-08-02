from flask import Flask, render_template, request, jsonify, url_for
import json

app = Flask(__name__)

with open('data/nodes.json', 'r', encoding='utf-8') as f:
    nodes = json.load(f)

@app.route('/')
def index():
    start_node = nodes['start']
    return render_template(
        'index.html', 
        story_text=start_node['text'], 
        image_url=url_for('static', filename=start_node['image']),
        choices=start_node['choices'],
        background_color=start_node.get('color', '#FFFFFF')
    )

@app.route('/navigate')
def navigate():
    node_key = request.args.get('node')
    node = nodes[node_key]
    return render_template(
        'index.html', 
        story_text=node['text'], 
        image_url=url_for('static', filename=node['image']),
        choices=node['choices'],
        background_color=node.get('color', '#FFFFFF')
    )

if __name__ == '__main__':
    app.run(debug=True)
