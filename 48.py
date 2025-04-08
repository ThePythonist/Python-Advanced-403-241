students = [
    {"name": "amir", "job": "backend developer", "age": 15},
    {"name": "ali", "job": "database admin", "age": 16},
    {"name": "fatemeh", "job": "product manager", "age": 15},
]

html = """
<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  font-family: Consolas, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
</head>
<body>

<h1>Table of Students</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Job</th>
    <th>Age</th>
  </tr>
"""

for std in students:
    html += f"""
  <tr>
    <td>{std['name']}</td>
    <td>{std['job']}</td>
    <td>{std['age']}</td>
  </tr>
    """

html += """
</table>
</body>
</html>
"""

with open("table.html", "w") as f:
    f.writelines(html)
