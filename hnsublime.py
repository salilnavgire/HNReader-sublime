import sublime
import sublime_plugin
import urllib
import json


class CnpremailerCommand(sublime_plugin.TextCommand):
    def get_top_news(self):
        url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
        sock = urllib.request.urlopen(url)
        top_story_ids = json.loads(sock.read().decode("utf-8", "strict"))
        base_url = 'https://hacker-news.firebaseio.com/v0/item/'

        titles = []
        for res in top_story_ids[0:20]:
            new_url = base_url+str(res)+'.json?print=pretty'
            # print(new_url)
            sock1 = urllib.request.urlopen(new_url)
            strss = json.loads(sock1.read().decode("utf-8", "strict"))
            titles.append(strss['title'])
        return titles

    def run(self, edit):
        urls = []
        selections = self.view.sel()
        for selection in selections:
            urls.append(self.view.substr(selection))

        messages = self.get_top_news()
        self.show_quick_panel(messages, self.view.window())

    def show_quick_panel(self, messages, window):
        window.show_quick_panel(messages, None, sublime.MONOSPACE_FONT)
