import argparse
import logging
from pydoc import doc
import logging_loki
import os
from datetime import datetime
import inspect
import sys


#region definition de constante
APP_NAME = 'OpenClassRoom projet_2 Test' #Nom de l'application pour les logs
DEFAULT_URL = 'http://books.toscrape.com/' #url par défaut sinon précisé par l'utilisateur
DICT_STARS = {
                'One':1,
                'Two':2,
                'Three':3,
                'Four':4,
                'Five':5,
            }
#endregion

#region initialisation du logger
logging_loki.emitter.LokiEmitter.level_tag = "level"
handler = logging_loki.LokiHandler(
    url="http://molp.fr:3100/loki/api/v1/push",
    tags={"application": APP_NAME},
    version="1",
)

logger = logging.getLogger(APP_NAME)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
is_log_to_file = True
log_file = 'log.log'
is_log_to_var = True
log_var = []
is_verbose=False

def log_to_file(time, statuts,message, func_name, data_in, exception, log_file_to = log_file):
    """Enregistre les logs un fichier

    Args:
        time (str): heure
        statuts (str): status du log
        message (str): message du log
        func_name (str): fonction qui log
        data_in (str): données d'entrée
        exception (str): message de l'exception
        log_file (str): fichier du log 
    """
    with open(log_file_to,'a', encoding = 'utf-8') as f:
        f.write(time.ljust(30)+
                statuts.ljust(10)+
                message.ljust(30)+
                func_name.ljust(30)+
                data_in.ljust(30)+
                exception.ljust(30)+
                '\n')

def log_to_var(time, statuts,message, func_name, data_in, exception):
    """Enregistre les logs dans une variable

    Args:
        time (_type_): heure
        statuts (_type_): status du log
        message (_type_): message du log
        func_name (_type_): fonction qui log
        data_in (_type_): données d'entrée
        exception (_type_): message de l'exception
    """
    log_var.append({'time':time,
            'status': statuts,
            'message':message,
            'fonction':func_name,
            'data_in':data_in,
            'exception':exception
            })

def log_to_console(time, statuts='',message='', func_name='', data_in='', exception=''):
    """ Affiche les logs dans la console

    Args:
        time (str): heure
        statuts (str, optional): status du log. Defaults to ''.
        message (str, optional):  message du log. Defaults to ''.
        func_name (str, optional):  fonction qui log. Defaults to ''.
        data_in (str, optional): données d'entrée. Defaults to ''.
        exception (str, optional):  message de l'exception. Defaults to ''.
    """
    print(time, statuts,message,func_name,data_in,exception)
    
def log_error(message,data_in,exception):
    """fonction qui permet de logger une erreur

    Args:
        message (str): status du log
        data_in (Object): données d'entrée
        exception (Exception): exception
    """
    time = datetime.now().isoformat(timespec='seconds', sep=' ')
    try:
        func_name = sys._getframe(1).f_code.co_name
    except Exception as _e:
        func_name = 'main'
    try:
        logger.error('error',extra={"tags": {"message": message, 
                                             "function":func_name, 
                                             "input":str(data_in), 
                                             "exception":str(exception), 
                                             'date-time': time}})
    except Exception as _e:
        logger.error('error',extra={"tags": {"message": message, 
                                             "function":func_name, 
                                             "input":'', 
                                             "exception":str(exception), 
                                             'date-time': time}})
    if is_log_to_file:
        log_to_file(time, 'ERROR', '',func_name,str(data_in),str(exception) )
    if is_log_to_var:
        log_to_var(time, 'ERROR', '',func_name,str(data_in),str(exception) )
    if is_verbose:
        log_to_console(time, 'ERROR', '',func_name,str(data_in),str(exception) )

def log_info(message):
    """Fonction qui permet de logger une info

    Args:
        message (str): message
    """
    time = datetime.now().isoformat(timespec='seconds', sep=' ')
    try:
        func_name = sys._getframe(1).f_code.co_name
    except Exception as _e:
        func_name = 'main'
    logger.info('info',extra={"tags": {"message": message, 
                                       "function":func_name, 
                                       "input":"", 
                                       "exception":"", 
                                       'date-time':time}})
    if is_verbose:
        log_to_console(time, message)