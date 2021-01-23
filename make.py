"""
Copyright 2021 atu4403

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import re
import pathlib

BASE_URL = "https://atu4403-images.netlify.com"
IMAGE_DIR = "assets"

assets = pathlib.Path(IMAGE_DIR)
contents = ""
for p in assets.glob("**/*"):
    _path = str(p)
    _path = str(p).replace(IMAGE_DIR, "")
    if re.match(r".*\.(png|jpeg|jpg|ico|svg|gif)$", _path):
        contents += f"""
        <li>
            <a href="{_path}">
                <img src="{_path}" width="150px">
                <span class='uk-padding'>{_path}</span>
            </a>
        </li>
        """
template = pathlib.Path("template.html").read_text()
html = template.format(contents=contents)
index = assets / "index.html"
index.write_text(html)
