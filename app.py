import os
import requests
from flask import Flask, flash, request, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/dataset'
UPLOAD_FOLDER1 = './static/text'


app = Flask(__name__, template_folder='template')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "m4xpl0it"

@app.route('/image')
def image():
    return render_template("image.html")

@app.route('/about')
def about():    
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/text')
def text():
    return render_template("text.html",msg="")

@app.route('/pred_page')
def pred_page():
    pred = session.get('pred_label', None)
    f_name = session.get('filename', None)
    return render_template('pred.html', pred=pred, f_name=f_name)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    import os
    if request.method == 'POST':
        f = request.files['bt_image']
        filename = str(f.filename)
        print("filename ",filename)
        ufn=UPLOAD_FOLDER+"/"+filename
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("ufn ",ufn)
        if filename!='':
            import cv2
            import numpy as np
            import os
            path = "images"
            dir_list = os.listdir(path)
            print(dir_list)
            matchlist=[]
            original = cv2.imread(ufn)
            for x in dir_list:
                try:
                    fpath="images/"+x
                    print("file path ",fpath)
                    duplicate = cv2.imread(fpath)
                    if original.shape == duplicate.shape:
                      difference = cv2.subtract(original, duplicate)
                      b, g, r = cv2.split(difference)

                      if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                        matchlist.append(fpath)
                except AttributeError:
                   pass
            if len(matchlist)>0:
                print("Pal ",matchlist)
                return render_template('pred.html',ml=matchlist,msg="Plagarism Detected")
            else:
                print("not pal")
                return render_template('pred.html',ml="No Plagarism",msg="")

            return render_template('index.html')
           
    return render_template('index.html')

@app.route('/textprediction', methods=['POST', 'GET'])
def textprediction():
    import os
    if request.method == 'POST':
        f = request.files['bt_image']
        filename = str(f.filename)
        print("filename ",filename)
        ufn=UPLOAD_FOLDER+"/"+filename
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("ufn ",ufn)
        if filename!='':
            from difflib import SequenceMatcher
            import difflib
            import os
            path = "textdataset"
            dir_list = os.listdir(path)
            print(dir_list)


            first_file = ufn
            #second_file = "Other Files/g2.txt"

            first_file_lines = str(open(first_file, encoding="utf-8").readlines())
            for x in dir_list:
                second_file=path+"/"+x
                print("Second File is ",second_file)
                second_file_lines = str(open(second_file, encoding="utf-8").readlines())

                first_file_lines1 = open(first_file, encoding="utf-8").readlines()
                second_file_lines1 = open(second_file, encoding="utf-8").readlines()

                # d = difflib.HtmlDiff()
                # print d.make_table(text1_lines, text2_lines)
                difference = difflib.HtmlDiff().make_file(first_file_lines1, second_file_lines1, first_file, second_file)
                difference_report = open('result/'+x.split(".")[0]+'.html', 'w')
                difference_report.write(difference)
                difference_report.close()

                # Program 2.0 starts here
                # This Program 2.0 prints only plagiarized text.

                
                file1 = open(first_file,"r", encoding="utf8")
                text1 = file1.readlines()
                # print("Content of text file 1 in List:")
                # print(text1)


                file2 = open(second_file,"r", encoding="utf8")
                text2 = file2.readlines()
                # print("\n\nContent of text file 2 in List:")
                # print(text2)

                # Convert list to string

                str1=''.join(text1)
                str2=''.join(text2)

                # print("\n\nContent of text file 1:")
                # print(str1)
                # print("\n\nContent of text file 2:")
                # print(str2)
                

                # Split the string

                sent_text1 = str1.split('.')
                sent_text2 = str2.split('.')
                # print(sent_text1)
                # print(sent_text2)

                # Create a for loop that compares two lists

                final_list=[]
                for z in sent_text1:
                    for y in sent_text2:
                        if z == y:
                            final_list.append(z)


                print("\n Plagiarized Content Below:")
                print(final_list)
                print("\n")

                # Program 3.0 for finding similarity percentage


                def similar(a, b):
                    return SequenceMatcher(None, a, b).ratio()


                val = similar(first_file_lines, second_file_lines)*100
                percentage = round(val, 2)
                print(" Similarity Percentage :", percentage, "%")

                print("\nNow,Check for difference report Html file.")

            return render_template('index.html')
    return render_template('index.html')

if __name__=="__main__":
    app.run(port=3000,debug=True)
    
