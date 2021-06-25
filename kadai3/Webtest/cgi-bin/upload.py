#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;


<html>
<link rel="stylesheet" href="../style.css">
<head>
<header>

    <h1>
        <a href="/">1922069 仲程凜太朗</a>
    </h1>

    <nav class="pc-nav">
        <ul>
            <li><a href="#">ABOUT</a></li>
            <li><a href="#">To Do</a></li>
            <li><a href="#">Result</a></li>
        </ul>
    </nav>
</header>

  <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
  <title>画像をアップロードした上で、その画像の特徴量を取得するサイト</title>
</head>
<body>
<div id="contents">
<h1>About</h1>
<p>画像をアップロードした上で、その画像の特徴量を取得するシステムです。</p>
<h1>画像をアップロードした上で、その画像の特徴量を取得するサイト</h1>
<form action="upload.py" method="post" enctype="multipart/form-data">
  <input type="file" name="file" />
  <input type="submit" />
</form>
<p>%s</p>
</div>
<div>%s</div>



</body>
</html>
'''

import cgi
import os, sys
import numpy as np
import pandas as pd
import metadata_ext
import metadata_rep


try:
    import msvcrt
    msvcrt.setmode(0, os.O_BINARY)
    msvcrt.setmode(1, os.O_BINARY)
except ImportError:
    pass

content=''
files=[]
form = cgi.FieldStorage()
df_html=''
if 'file' in form:
    item = form['file']
    if item.file:
        fout = open(os.path.join('./img/', item.filename), 'wb')
        while True:
            chunk = item.file.read(1000000)
            if not chunk:
                break
            fout.write(chunk)
        fout.close()

    # /cgi-bin/tmpが置かれている場所を指定
    filepath='./img/'+item.filename
    df=metadata_ext.metadata_rgb_write(filepath)
    df_html=metadata_rep.generate_df_html(df)

    content='<img src=".'+filepath+'" width="25%" height="auto">'

print (html % (content,df_html))