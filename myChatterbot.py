from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, request, render_template

# Tạo đối tượng chatbot
#chatbot = ChatBot('Chatterbot', read_only=True, logic_adapters=['chatterbot.logic.BestMatch'])

chatbot = ChatBot(
    'Chatterbot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.70
        }
    ]
)
# Tạo trainer sử dụng tập dữ liệu corpus của ChatterBot
trainer = ChatterBotCorpusTrainer(chatbot)

# Đào tạo chatbot sử dụng tập dữ liệu corpus của ChatterBot
trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.custom.myown")
trainer.train("chatterbot.corpus.english.ai")
trainer.train("chatterbot.corpus.english.food")
trainer.train("chatterbot.corpus.english.money")
trainer.train("chatterbot.corpus.english.movies")
trainer.train("chatterbot.corpus.english.science")
trainer.train("chatterbot.corpus.english.sports")
allAskAnswers = []

myAppBot = Flask(__name__)

@myAppBot.route('/',methods=["GET","POST"])
def home():
    if request.method == "POST":
        question = request.form.get("question")
        answer = chatbot.get_response(question)
        question = '- ' + str(question)
        answer = '-- ' + str(answer)
        allAskAnswers.append(question)
        allAskAnswers.append(answer)
        return render_template('index.html',questions = allAskAnswers)#, "<script> window.scrollTo(0, document.body.scrollHeight); </script>"
    else:
        return render_template('index.html')

if __name__ == '__main__':
    myAppBot.run(debug=True,host='127.0.0.1',port=8000)