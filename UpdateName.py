from http import client
import tweepy
import Config

def autenticação():

    #Adicionar os tokens e keys no arquivo 'Config.py'
    consumer_key = Config.consumer_key
    consumer_secret = Config.consumer_secret   
    access_token = Config.access_token
    access_token_secret = Config.access_token_secret

    #Login a partir das chaves
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #Declaração para chamar a api sem espamar
    Api = tweepy.API(auth, wait_on_rate_limit=True)
    
    return Api

def updateName():
    Api = autenticação()
    Nome = "Pedro"
    #retorna um json com todos os dados da conta
    Update = Api.update_profile(name=Nome)

    return Update

deuCerto = updateName()
print(deuCerto)