'''
import sublime, sublime_plugin
#import urllib2
#import urllib

class RedditsublimeCommand(sublime_plugin.TextCommand):
	def validate_urls(self, urls):
	  messages = []
	  for url in urls:
	    try:
	      request = urllib.Request(url, headers={ "User-Agent" : "Sublime URL Checker" })
	      response = urllib.urlopen(request, timeout=10)
	      message = '"%s" is a valid URL.' % url
	    except Exception:
	      message = '"%s" is an invalid URL.' % url

	    messages.append(message)
	    return messages


	def run(self, edit):
	  urls = []
	  selections = self.view.sel()
	  for selection in selections:
	    urls.append(self.view.substr(selection))

	  messages = self.validate_urls(urls)
	  self.show_quick_panel(messages, self.view.window())

	def show_quick_panel(self, messages, window):
	  window.show_quick_panel(messages, None, sublime.MONOSPACE_FONT)
'''

import sublime
import sublime_plugin
import urllib
import json
url = 'https://news.ycombinator.com'
sock = urllib.request.urlopen(url)
print(sock)
content = sock.read()

print(content)

#sock.close()

#print content


class CnpremailerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
