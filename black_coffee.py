from playwright.sync_api import sync_playwright

streamlit_apps = [
    "https://test-app-247.streamlit.app/",  # app simply for testing purposes
    "https://data-cleaning-app-arc.streamlit.app/",  # WORTH grant cleaning app
    # Baldwin Co. AL migration dashy
    "https://baldwin-county-migration.streamlit.app/",
    "https://nashville-dash.streamlit.app/",  # generic Nashville dashy
    "https://kolter-nashville.streamlit.app/",  # Kolter's Nashville dashy
    # Excel automation cleaning app for Uncle David
    "https://11-10-cleaning.streamlit.app/",
    "https://abi-t1000.streamlit.app/",  # Layla's version 2 app
    "https://gwinnett-housing.streamlit.app/",  # Gwinnett Housing dashy
    "https://dekalb-housing-desktop.streamlit.app/",  # Dekalb Housing dashy

]


def awake_app(app_url):
    with sync_playwright() as p:
        # Set headless=True to run in the background
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 60s timeout to handle loading
        page.goto(app_url, wait_until="networkidle", timeout=60000)

        browser.close()


# Awake all apps in the list
def awake_all_apps():
    for app in streamlit_apps:
        awake_app(app)


if __name__ == "__main__":
    awake_all_apps()
