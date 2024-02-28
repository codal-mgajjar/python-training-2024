# check if file exists or not
import errno

try:
    with open("test4.txt") as f:
        f.read()

except IOError as e:
    if e.errno != errno.ENOENT:
        raise
    else:
        print(e)

# check if file is empty or not
import os

print(
    os.stat(
        "C:/Users/mgajjar/Desktop/python-training-2024/week-3/22_jan/emptyfile.txt"
    ).st_size
    == 0
)


# copy file content
with open(
    "C:/Users/mgajjar/Desktop/python-training-2024/week-3/22_jan/test3.txt", "r"
) as in_file, open(
    "C:/Users/mgajjar/Desktop/python-training-2024/week-3/22_jan/emptyfile.txt", "w"
) as out_file:
    for line in in_file:
        out_file.write(line)
