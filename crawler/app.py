from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route("/<problem_id>")
def scrape(problem_id):
    url = f"https://lcid.cc/{problem_id}"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        html = page.locator("div[data-key='description-content']").inner_html()
        browser.close()
        return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6789)

