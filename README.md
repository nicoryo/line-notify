# Enviroment
LINE API CODE: https://notify-bot.line.me/ja/
Python: 3

# How to use
- git clone
```
git clone git@github.com:nicoryo/line_notify.git
```

- create `.env` file.
```
# input line api code in ""
line_key = ""
```

- Insert below code in your file
```
# import
from line_notify import line_notify

# notify
# input argment in ()
line_notify.main()

```
