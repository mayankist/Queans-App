from flask import Flask, render_template, request, url_for, redirect
from transformers import BertForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline


app = Flask(__name__)

model = BertForQuestionAnswering.from_pretrained("deepset/bert-base-cased-squad2")
tokenizer = AutoTokenizer.from_pretrained("deepset/bert-base-cased-squad2")
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

def myFunc(in1, context):
  nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
  return nlp({ "question": in1, "context": context })

question_answers = []

# print(myFunc(in1,context),"\n")

# @app.route('/')
# def index():
#     return render_template('base.html')

@app.route('/', methods=('GET', 'POST'))
def create():
    answer = None
    context = ""  # Initialize context with an empty string
    in1 = ""      # Initialize in1 with an empty string
    if request.method == 'POST':
        context = request.form['context']
        in1 = request.form['question']

        # conn = get_db_connection()
        # cur = conn.cursor()
        # cur.execute('INSERT INTO tasks (taskname, recipient)'
        #             'VALUES (%s, %s)',
        #             (taskname, recipient))
        # conn.commit()
        # cur.close()
        # conn.close()

        answer = myFunc(in1, context)
        # return redirect(url_for('index', answer = answer))

        question_answers.insert(0, {"question": in1, "answer": answer})

    return render_template('base.html', answer = answer, context = context, in1 = in1, question_answers=question_answers)

# @app.route('/edit/<id>/', methods = ['POST', 'GET'])
# def taskEdit(id):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM tasks WHERE id = %s',(id))
#     data = cur.fetchall()
#     cur.close()
#     conn.close()
#     return render_template("edit.html", tasks=data[0])

# @app.route('/update/<id>/', methods=['POST'])
# def taskUpdate(id):
#     if request.method == 'POST':
#         taskname = request.form['taskname']
#         recipient = request.form['recipient']

#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute("""
#             UPDATE tasks 
#             SET taskname = %s,
#                 recipient = %s
#             WHERE id = %s
#             """,(taskname,recipient,id))
#         conn.commit()
#         cur.close()
#         conn.close()
#         return redirect(url_for('index'))

# @app.route('/delete/<int:id>', methods = ['POST','GET'])
# def taskDelete(id):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("DELETE FROM tasks WHERE id = {0}".format(id))
#     conn.commit()
#     return redirect(url_for('index'))
