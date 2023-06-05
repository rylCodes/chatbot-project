from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from sqlalchemy import create_engine

database_uri = 'postgresql://postgres:password121012@localhost:5432/chatterbc'
engine = create_engine(database_uri)

# Create your views here.
chatBot = ChatBot(
    'chatbot',
    read_only=False,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            #'default_response': 'I am sorry, but I do not understand.',
            #'maximum_similarity_threshold': 0.90
        }
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=database_uri
)
#list_to_train = [
#    'Hi!',
#    'Hello! How may I help you?,'
#    'How to register my DTI business name?',
#    'You can register online or visit a nearest Negosyo Center',
#    'How to register my DTI business name online',
#    'Register your business name online at https://bnrs.dti.gov.ph/registration',
#    'What are the requirements to register with DTI?',
#    'Visit a nearest Negosyo Center. Just bring one government-issued valid ID and fill-out the application form.',
#]

#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(chatBot)
#chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request, 'index.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(chatBot.get_response(userMessage))
    return HttpResponse(chatResponse)

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(chatBot.get_response(userMessage))
    return HttpResponse(chatResponse)