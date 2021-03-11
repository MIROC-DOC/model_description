import sys
import re

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        body = f.read()

    before_str = r'\\begin{eqnarray}\s*\\begin{align}'
    after_str = r'\\begin{align}'
    body = re.sub(before_str, after_str, body, flags=re.DOTALL)
    before_str = r'\\end{align}\s*\\end{eqnarray}'
    after_str = r'\\end{align}'
    body = re.sub(before_str, after_str, body, flags=re.DOTALL)

    before_str = r'\\begin{eqnarray}\s*\\begin{equation}'
    after_str = r'\\begin{equation}'
    body = re.sub(before_str, after_str, body, flags=re.DOTALL)
    before_str = r'\\end{equation}\s*\\end{eqnarray}'
    after_str = r'\\end{equation}'
    body = re.sub(before_str, after_str, body, flags=re.DOTALL)

    before_str = r'\\begin{eqnarray}\s*\\begin{eqnarray}'
    after_str = r'\\begin{eqnarray}'
    body = re.sub(before_str, after_str, body, flags=re.DOTALL)
    before_str = r'\\end{eqnarray}\s*\\end{eqnarray}'
    after_str = r'\\end{eqnarray}'
    body = re.sub(before_str, after_str, body, flags=re.DOTALL)

    with open(sys.argv[1], 'w') as f:
        f.write(body)
