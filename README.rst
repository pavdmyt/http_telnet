A simple Python emulation of telnetting port 80 by HTTP requests directly to web servers.

Example
-------

::

	$ python telnet_emul.py

	# telnetting google:
	> telnet www.google.com 80
	Trying 173.194.113.211...
	Connected to www.google.com
	Escape character is '^]'

	# Actual HTTP request:
	>> HEAD / HTTP/1.0

	# Response:
	HTTP/1.0 302 Found
	Cache-Control: private
	Content-Type: text/html; charset=UTF-8
	Location: http://www.google.com.ua/?gfe_rd=cr&ei=yqHGVJSuK6Gt8we944HQDw
	Content-Length: 262
	Date: Mon, 26 Jan 2015 20:21:30 GMT
	Server: GFE/2.0
	Alternate-Protocol: 80:quic,p=0.02


	Connection closed by foreign host.
