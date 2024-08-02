from flask import render_template

def navigate_node(node_key, nodes):
    node = nodes.get(node_key, None)
    if node is None:
        return render_template('index.html', story_text="Erreur: nœud non trouvé.", image_url="", choices={})

    story_text = node["text"]
    image_url = node["image"]
    choices = node["choices"]
    
    return render_template('index.html', story_text=story_text, image_url=image_url, choices=choices)
