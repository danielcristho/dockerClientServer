#library to request 'index.html' from server
import urllib.request

client_Req = urllib.request.urlopen("http://localhost:1234/")

# correspond to the server response encoded & decode TO DISPLAY
endcode_type = client_Req.read()
decoded_type = endcode_type.decode("utf8")

#display file 'index.html'
print(decoded_type)

client_Req.close()

