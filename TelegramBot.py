from telegram.ext import CommandHandler
from telegram.ext import Updater
import Telegram_CommandList
import __setting__
import threading
import telegram
import schedule

TelegramBotStart = Updater(token=__setting__.__BotTelegramToken__,)
MessageRecvUpdate = TelegramBotStart.dispatcher

class TelegramBot_Run:
    def __init__(self) -> None:

        self.CountCmd = len(Telegram_CommandList.BotStartCommand)
        self.CmdDict = Telegram_CommandList.BotStartCommand
        self._argsMsg = []
    def __str__(self) -> str:
        return f"<TelegramBot(Cmd_Count=<[{self.CountCmd}])>"

    def Cmd_Add(self):
        """
        <Command variable> = CommandHandler(<command>, self.TelegramStart._<command>)
        """
        global MessageRecvUpdate

        for TelegramCommand , TelegramSendText in self.CmdDict.items():
            CommandAdd = CommandHandler(TelegramCommand, (lambda Telegram_UpdateChat_id, NetxSend_MessAge: NetxSend_MessAge.bot.send_message(chat_id=Telegram_UpdateChat_id.effective_chat.id, text=TelegramSendText)))
            MessageRecvUpdate.add_handler(CommandAdd)

    def FuncCmd_Add(self, Cmd, ObjectClass, args = (), kwargs = None, _FuncFind = None, _Funcargs = (), _Funckwargs = {}) -> None:
        """
        TelegramBot.FunctionCmd_Add(<Command>, <Function or Class Name>)
        """
        global MessageRecvUpdate

        self.args = args
        self.Find_ = None
        self._FuncFind = None
        self._Funcargs = None
        self._Funckwargs = None
        self.ObjClass = ObjectClass
        self.kwargs = kwargs = {} if kwargs is None else kwargs
        self.Check_List = [str, int, bool, float, tuple, list, dict, None]

        if _FuncFind:
            self._FuncFind = _FuncFind
            self._Funcargs = _Funcargs
            self._Funckwargs = _Funckwargs
        try:
            _lambda = self._Command
            CommandAdd = CommandHandler(Cmd, _lambda)
            MessageRecvUpdate.add_handler(CommandAdd)

        except:
            del ObjectClass, args, kwargs

    def _Command(self, Telegram_Updater, NextSend) -> None:

        if type(self.args) in self.Check_List:
            return self.Send_Message(Telegram_Updater, NextSend)
        else:
            return self.Send_Message(Telegram_Updater, NextSend, False)

    def Send_Message(self, Chatid, NextSend, _args = True):
        
        self._argsMsg = NextSend.args
        try:
            if self._FuncFind:
                if type(self.args) in self.Check_List:
                    self._FuncFind(self._argsMsg, *self._Funcargs, **self._Funckwargs)
                else:
                    self._FuncFind(self._argsMsg, self._Funcargs, **self._Funckwargs)
                    
            if _args:
                return NextSend.bot.send_message(chat_id=Chatid.effective_chat.id, text=self.ObjClass(self.args, **self.kwargs))
            else:
                return NextSend.bot.send_message(chat_id=Chatid.effective_chat.id, text=self.ObjClass(*self.args, **self.kwargs))
        except AttributeError as A:
            print(A)

    def bot_start(self) -> bool:
        """
        TelegramBot Start
        """
        global TelegramBotStart

        try:
            TelegramBotStart.start_polling()
            return True
        except:
            return False

class TimeStartBotSend:
    def __init__(self) -> None:
        pass

    def _s(self, s, FunctionObject) -> None:
        """
        s variable = time Second 
        """
        schedule.every(s).seconds.do(FunctionObject)

    def _m(self, m, FunctionObject) -> None:
        """
        m variable = time minute
        """
        schedule.every(m).minutes.do(FunctionObject)

    def _h(self, h, FunctionObject) -> None:
        """
        h variable = time hour
        """
        schedule.every(h).hour.do(FunctionObject)

    def _Runh(self,FunctionObject) -> None:
        """
        _Runh(<Run Function Name>)
        1 hour Start
        """
        schedule.every().hour.do(FunctionObject)

    def _day(self, datetime, FunctionObject) -> None:
        """
        _day(<datetime>, <Run Function Name>)

        datetime ex) 00:00 or 12:24
        """
        schedule.every().day.at(datetime).do(FunctionObject)


    def TimeStart(self):
        def RUN():
            while True:
                schedule.run_pending()
        TimeBasedStart = threading.Thread(target=RUN, name='TelegramBotSendTime')
        TimeBasedStart.start()

class _OneSendMsg:
    def __init__(self, Token : str = __setting__.__BotTelegramToken__) -> None:
        self.TelegramBotSned_One = telegram.Bot(token=Token)
    
    def Chat_idSend(self, Chat_id, MsgText) -> bool:
        """
        Send a message to the corresponding chat_id.
        """
        try:
            self.TelegramBotSned_One.send_message(chat_id=Chat_id , text=MsgText)
            return True

        except:
            return False