def generate_table(products):

    table = """
<table>
<tr>
<th>Product</th>
<th>Link</th>
</tr>
"""

    for p in products:

        table += f"""
<tr>
<td>{p['title']}</td>
<td><a href="{p['url']}">Check Price</a></td>
</tr>
"""

    table += "</table>"

    return table
