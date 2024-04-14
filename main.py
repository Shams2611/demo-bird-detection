from taipy import Gui, Config
from taipy.gui import GuiApp
import folium  # for creating maps

# Configuring the server
Config.configure_from_file('config.cfg')

# Initialize the GUI object
gui = Gui()

# Global state for storing the uploaded video and bird data
state = {"video": None, "bird_data": [], "map": None}

# Function to handle video uploads
def upload_video(state, video):
    state["video"] = video
    # Here you would add your YOLOv8 integration to process the video
    # For now, we'll just simulate some data
    state["bird_data"] = [{"species": "Sparrow", "location": (40.7128, -74.0060)}]
    update_map(state)
    return state

# Function to update the map based on bird data
def update_map(state):
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
    for bird in state["bird_data"]:
        folium.Marker(
            location=bird["location"],
            popup=f"{bird['species']}",
            icon=folium.Icon(color="green")
        ).add_to(m)
    state["map"] = m._repr_html_()  # Using folium's HTML representation in Taipy

# GUI layout
gui.add_page(name="Main Page", layout="""
<Vertical>
    <FilePicker onchange=upload_video/>
    <Html content={state.map}/>
</Vertical>
""")

# Create and run the GUI application
if __name__ == "__main__":
    app = GuiApp(gui)
    app.run()
