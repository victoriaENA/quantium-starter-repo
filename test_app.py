from app import app
import chromedriver_autoinstaller

# This automatically downloads the correct chromedriver for your computer!
chromedriver_autoinstaller.install()

def test_header_is_present(dash_duo):
    # Start the app
    dash_duo.start_server(app)
    
    # Wait for the H1 heading to appear (timeout after 10 seconds)
    dash_duo.wait_for_element("h1", timeout=10)
    
    # Assert that the text matches our title
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualiser"

def test_visualization_is_present(dash_duo):
    # Start the app
    dash_duo.start_server(app)
    
    # Find the graph by the ID we gave it in app.py
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)

def test_region_picker_is_present(dash_duo):
    # Start the app
    dash_duo.start_server(app)
    
    # Find the radio items filter by its ID
    dash_duo.wait_for_element("#region-filter", timeout=10)