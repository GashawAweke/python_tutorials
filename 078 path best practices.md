Always specify encoding when reading text files.

```py
with open(
"notes.txt",
encoding="utf-8"
) as file:
content = file.read()
```

This prevents many deployment issues.
