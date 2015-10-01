import sys
import os
import time 
import Skype4Py
import random 
def ndsSay(ndsWords):
	ndsIn = str(ndsWords)
	smcd = 'espeak "'+ndsTalk+'"'
	print zmcd
	f=os.popen(zmcd)
	f.close()
	ndsWords=""
	ndsTalk=""
	zmcd=''
	ndsMonkey=''

def OnAttach(status): 
	print 'API status' + skype.Convert.AttachmentStatusToText(status)
	if status == Skype4Py.apiAttachAvailable:
		skype.Attach()

	if status == Skype4Py.apiAttachAvailable:
		print('**************')


def OnMessageStatus(Message, Status):
	if Status == 'RECEIVED':
		print(Message.FromDisplayName + ': ' + Message.Body)
		ndsSay(Message.FromDisplayName)
		ndsSay(Message.Body)

	if Status == 'READ':
		ndsMonkey = 'todo'
		print (Message.FromDisplayName + ': ' + Message.Body)
		ndsSay(Message.FromDisplayName)
		ndsSay(Message.Body)

	if Status == 'SENT':
		print('Myself ' + Message.Body)

skype = Skype4Py.Skype()
skype.OnAttachmentStatus = OnAttach
skype.OnMessageStatus = OnMessageStatus

print('***************')
print 'Connecting to Skype...'

skype.Attach()

#loops until user writes 'exit'
Cmd = ''
while not Cmd == 'exit':
	Cmd = raw_input('')
	