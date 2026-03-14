from templates.table_generator import generate_table

def render_pillar(content, products):

    table = generate_table(products)

    return f"""
{content}

<h2>Product Comparison</h2>

{table}

<p>As an Amazon Associate we earn from qualifying purchases.</p>
"""
