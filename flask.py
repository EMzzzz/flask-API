#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from flask import Flask, render_template
app = Flask(__name__, static_url_path = "/static", static_folder = "static")

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from Econ_Public_Sent_Static import post_percent, neg_percent,last_up,tweets_analyzed

@app.route('/choice', methods=['GET'])
def sent_results():
    return render_template('flask_template_aws.html', 
                           twit_sent1 = post_percent, twit_sent2 = neg_percent, 
                           time = last_up, tweets = tweets_analyzed) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


# In[ ]:




