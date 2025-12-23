from app import app

# 1. TEST HEADER PRESENCE
def test_header_exists(dash_duo):
    # Start the app
    dash_duo.start_server(app)
    # Wait for the header to appear (timeout after 10s if not found)
    dash_duo.wait_for_element("#header", timeout=10)
    # If code reaches here without error, the test passes
    assert dash_duo.find_element("#header").text != ""

# 2. TEST VISUALIZATION PRESENCE
def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    # Look for the graph
    dash_duo.wait_for_element("#visualization", timeout=10)

# 3. TEST REGION PICKER PRESENCE
def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    # Look for the radio button container
    dash_duo.wait_for_element("#region_selector", timeout=10)