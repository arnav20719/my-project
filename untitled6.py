# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XxQBFSCC1vs_WV8M2fKjdGEPJNERWJrd
"""

pip install matplotlib

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Function to create a box
def create_box(ax, text, xy, width=3.8, height=1, color='lightblue'):
    ax.add_patch(FancyBboxPatch(
        xy, width, height, boxstyle="round,pad=0.3",
        edgecolor='black', facecolor=color, lw=2
    ))
    ax.text(xy[0] + width/2, xy[1] + height/2, text, ha='center', va='center', fontsize=10, fontweight='bold')

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 16)
ax.axis('off')

# Define the positions of the boxes
positions = {
    'Frontend': (3.1, 14),
    'Backend': (3.1, 11),
    'AI Engine': (1, 8),
    'Database': (6, 8),
    'Task Queue': (3.1, 5),
    'Search Engine': (1, 2),
    'External Services': (6, 2),
}

# Create the boxes
create_box(ax, "Frontend\n(React/Angular)\n- User Interface\n- API Requests\n- Data Presentation", positions['Frontend'])
create_box(ax, "Backend\n(Flask/Django)\n- API Request Handling\n- Business Logic\n- Interacts with AI Engine & Database", positions['Backend'], height=1.5)
create_box(ax, "AI Engine\n(TensorFlow, PyTorch, GPT, BERT)\n- Question Gen\n- Sentiment\n- Learning Plans", positions['AI Engine'], height=1.5)
create_box(ax, "Database\n(MySQL/PostgreSQL)\n- User Data\n- Curricula\n- Question Banks\n- Feedback", positions['Database'], height=1.5)
create_box(ax, "Task Queue\n(Celery with RabbitMQ/Redis)\n- Manages Background Tasks\n- Notification Dispatch", positions['Task Queue'], height=1.3)
create_box(ax, "Search Engine\n(Elasticsearch)\n- Indexes Curriculum, Questions\n- Enables Fast Search", positions['Search Engine'], height=1.2)
create_box(ax, "External Services\n- OpenAI GPT API\n- Hugging Face\n- External Storage", positions['External Services'], height=1.2)

# Draw the arrows
ax.annotate("", xy=(5, 13.8), xytext=(5, 12), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(3, 10.5), xytext=(2, 9.5), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(5, 10.5), xytext=(7, 9.5), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(5, 7.7), xytext=(5, 6.2), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(2.8, 4.5), xytext=(2.2, 3.2), arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(6.8, 4.5), xytext=(7.5, 3.2), arrowprops=dict(arrowstyle="->", lw=2))

# Display the flowchart
plt.show()

import matplotlib.pyplot as plt
import networkx as nx

# Initialize the directed graph
G = nx.DiGraph()

# Add nodes for each component in the architecture
components = [
    "UI Layer",
    "Backend Logic Layer",
    "AI Processing Layer",
    "Data Management Layer",
    "Task Management Layer",
    "Search and Indexing Layer",
    "External Services Layer"
]

for component in components:
    G.add_node(component)

# Add edges to represent the data flow and interactions
edges = [
    ("UI Layer", "Backend Logic Layer"),
    ("Backend Logic Layer", "AI Processing Layer"),
    ("Backend Logic Layer", "Data Management Layer"),
    ("Backend Logic Layer", "Task Management Layer"),
    ("Task Management Layer", "Search and Indexing Layer"),
    ("Task Management Layer", "External Services Layer"),
    ("AI Processing Layer", "Data Management Layer"),
    ("AI Processing Layer", "Task Management Layer"),
    ("Search and Indexing Layer", "Backend Logic Layer"),
    ("External Services Layer", "AI Processing Layer"),
]

for edge in edges:
    G.add_edge(*edge)

# Define the layout for the nodes
pos = nx.spring_layout(G)

# Draw the nodes with labels
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Draw the edges with arrows
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='->', arrowsize=20)

# Display the plot
plt.title("Functional Architecture of Automated Question Builder Application")
plt.show()

pip install matplotlib networkx

import matplotlib.pyplot as plt
import networkx as nx

# Initialize the directed graph
G = nx.DiGraph()

# Add nodes for each component in the architecture
components = [
    "Frontend (React/Angular)",
    "Backend (Flask/Django)",
    "AI Engine (TensorFlow/PyTorch, GPT, BERT)",
    "Database (MySQL/PostgreSQL)",
    "Task Queue (Celery with RabbitMQ/Redis)",
    "Search Engine (Elasticsearch)",
    "External Services (OpenAI GPT API, Hugging Face, External Storage)"
]

for component in components:
    G.add_node(component)

# Add edges to represent the data flow and interactions
edges = [
    ("Frontend (React/Angular)", "Backend (Flask/Django)"),
    ("Backend (Flask/Django)", "AI Engine (TensorFlow/PyTorch, GPT, BERT)"),
    ("Backend (Flask/Django)", "Database (MySQL/PostgreSQL)"),
    ("Backend (Flask/Django)", "Task Queue (Celery with RabbitMQ/Redis)"),
    ("Task Queue (Celery with RabbitMQ/Redis)", "Search Engine (Elasticsearch)"),
    ("Task Queue (Celery with RabbitMQ/Redis)", "External Services (OpenAI GPT API, Hugging Face, External Storage)"),
    ("AI Engine (TensorFlow/PyTorch, GPT, BERT)", "Database (MySQL/PostgreSQL)"),
    ("AI Engine (TensorFlow/PyTorch, GPT, BERT)", "Task Queue (Celery with RabbitMQ/Redis)"),
    ("Search Engine (Elasticsearch)", "Backend (Flask/Django)"),
    ("External Services (OpenAI GPT API, Hugging Face, External Storage)", "AI Engine (TensorFlow/PyTorch, GPT, BERT)")
]

for edge in edges:
    G.add_edge(*edge)

# Define the layout for the nodes
pos = nx.spring_layout(G, k=0.5, seed=42)

# Draw the nodes with labels
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightgreen')
nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold', verticalalignment='center')

# Draw the edges with arrows
nx.draw_networkx_edges(G, pos, edgelist=edges, arrowstyle='->', arrowsize=20)

# Display the plot
plt.title("Technical Architecture of Automated Question Builder Application")
plt.show()