import sublime
import sublime_plugin
import urllib
import json
import webbrowser


class hnreaderCommand(sublime_plugin.WindowCommand):
    def get_top_news(self):
        url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
        sock = urllib.request.urlopen(url)
        top_story_ids = json.loads(sock.read().decode("utf-8", "strict"))
        base_url = 'https://hacker-news.firebaseio.com/v0/item/'

        self.titles = []
        self.urls = []
        self.texts = []
        self.scores = []
        for res in top_story_ids[0:30]:
            new_url = base_url+str(res)+'.json?print=pretty'
            # print(new_url)
            sock1 = urllib.request.urlopen(new_url)
            strss = json.loads(sock1.read().decode("utf-8", "strict"))
            try:
                self.titles.append(strss['title'])
            except KeyError:
                self.titles.append([' '])
            try:
                self.urls.append(strss['url'])
            except KeyError:
                self.urls.append([' '])
            try:
                self.texts.append(strss['text'])
            except KeyError:
                self.texts.append([' '])
            try:
                self.scores.append(strss['score'])
            except KeyError:
                self.scores.append([' '])
        return self.titles, self.urls, self.texts, self.scores

    def run(self):
        messages, urls, texts, scores = self.get_top_news()
        self.show_quick_panel1(messages, urls, texts, scores, self.window)

    def show_quick_panel1(self, messages, urls, texts, scores, window):
        self.feed_text = []
        for i in range(len(messages)):
            self.feed_text.append([str(i + 1) + '. ' + str(messages[i]), 'score:'+str(scores[i])+'   ('+urls[i]+')'])

        window.show_quick_panel(self.feed_text, self.openURL, sublime.MONOSPACE_FONT)

    def openURL(self, index):
        browser_url = self.urls[index]
        webbrowser.open(browser_url)
