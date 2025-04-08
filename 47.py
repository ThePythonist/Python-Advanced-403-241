header = input("Enter header : ")
par = input("Enter paragraph : ")

html = f"""
<h1>{header}</h1>
<p>{par}</p>
"""

with open("index2.html", "w") as f:
    f.writelines(html)
