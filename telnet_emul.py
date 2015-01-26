"""
A simple emulation of telnetting port 80 by HTTP requests directly
to web servers.
"""
from socket import socket, gethostbyname, AF_INET, SOCK_STREAM


def http_req(server, request_uri, method, http_version):
    """Issues an HTTP request."""
    # Creating a socket to connect and read from
    s = socket(AF_INET, SOCK_STREAM)

    # Finding server address (assuming port 80)
    adr = (gethostbyname(server), 80)

    # Connecting to server
    s.connect(adr)

    # Sending request
    s.send(' '.join([method, request_uri, http_version, '\n\n']))

    # Printing response
    resp = s.recv(1024)
    while resp != '':
        print(resp)
        resp = s.recv(1024)


if __name__ == '__main__':
    # User specifies server and port, e.g. `www.example.com 80`
    user_input = raw_input('> telnet ').split()

    # User input handler:
    server = user_input[0]
    try:
        port = int(user_input[1])
    except IndexError:
        port = 80
    except ValueError:
        print("telnet: could not resolve {}/{}: Servname not supported for ai_socktype".
              format(server, user_input[1]))
    else:
        print("Trying {}...".format(gethostbyname(server)))
        print("Connected to {}".format(server))
        print("Escape character is '^]'")

    # User types actual http request, e.g. `HEAD / HTTP/1.0`
    # enter should be pressed twice
    request = raw_input().split()
    raw_input()

    # !!! TODO: write a user input handler here
    # Get method, request-URI and HTTP version:
    method = request[0]
    req_uri = request[1]
    http_ver = request[2]

    http_req(server, req_uri, method, http_ver)
    print("Connection closed by foreign host.")
