#coding=utf-8

def headers(token=None):
    headers = {"Cookie": token}
    return headers


def headers_json(token=None):
    headers = {'Content-type': 'application/json',
               "Cookie": token}
    return headers

def headers_form_urlencoded(token=None):
    headers = {"Cookie": token,
               'Content-type': 'application/x-www-form-urlencoded'}
    return headers

def headers_text_xml(token=None):
    headers = {'Content-Type': 'text/xml; charset=utf-8',
               "Cookie": token}
    return headers

def headers_multipart_related(token):
    headers = {"Cookie": token,
               'Content-Type': 'multipart/related; charset=utf-8; boundary="==pj+EhsWuSQJxx7przmb8HM+ZkeNcG3HezSNID7LmfDa9J4lfdUL8W1F7TNJK=="; type="application/xop+xml"; start="<SOAP-ENV:Envelope>"; start-info="text/xml',
}
    return headers
