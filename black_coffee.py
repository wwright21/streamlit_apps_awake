from playwright.sync_api import sync_playwright

streamlit_apps = [
    "https://test-app-247.streamlit.app/",
    "https://baldwin-county-migration.streamlit.app/",
    "https://nashville-dash.streamlit.app/",
    "https://kolter-nashville.streamlit.app/",
    "https://11-10-cleaning.streamlit.app/"
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
