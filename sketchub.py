import webview

class Api:
    def __init__(self):
        webview.settings['ALLOW_DOWNLOADS'] = True
        webview.settings['OPEN_EXTERNAL_LINKS_IN_BROWSER'] = False
        webview.settings['OPEN_DEVTOOLS_IN_DEBUG'] = False

    def read_cookies(self, window):
        cookies = window.get_cookies()
        for c in cookies:
            print(c.output())

    def clear_cookies(self, window):
        window.clear_cookies()
        print('Cookies cleared')

if __name__ == '__main__':
    api = Api()

    window = webview.create_window(
        'Sketchub Web',
        'https://web.sketchub.in',
        js_api=api,
        confirm_close=True
    )

    webview.start(api.read_cookies, window, user_agent='Custom user agent', private_mode=False) # agent alias
