#!/usr/bin/python2.7

import os,sys,xmpp

dump_path = os.environ['HOME']+"/tmp/hangout_status"
config_params = {}

def get_params():
    jidparams = {}

    if os.access(os.environ['HOME']+'/.hangout_notify_rc', os.R_OK):
        for ln in open(os.environ['HOME']+'/.hangout_notify_rc').readlines():
            key,val = ln.strip().split('=',1)
            jidparams[key.lower()] = val

    for mandatory in ['jid', 'password']:
        if mandatory not in jidparams.keys():
            open(os.environ['HOME']+'/.hangout_notify_rc','w').write('#JID=romeo@montague.net\n#PASSWORD=juliet\n') 
            print 'Please ensure the ~/.hangout_notify_rc file has valid JID for sending messages.'
            sys.exit(0)

    return jidparams

#def message_handler(session, stanza):

    #if stanza.getBody() != None:
        #write_out(format_out(stanza.getFrom().getStripped(), stanza.getBody()), dump_path)

def setup(params):
    cl=xmpp.Client('gmail.com', debug=[])

    cl.connect(server=('talk.google.com', 5222))
    cl.auth(params['jid'], params['password'], 'gmail.com')

    cl.RegisterHandler("message", make_message_handler(params))
    cl.sendInitPresence()

    return cl

def format_out(name, message, params):
    dzen_format = False
    if "format" in params.keys():
        dzen_format = params["format"] == "dzen"
    if name in params.keys():
        name = params[name]
    name_color = ""
    message_color = ""
    if dzen_format and "name_color" in params.keys():
        name_color = "^fg(" + params["name_color"] + ")"
    if dzen_format and "message_color" in params.keys():
        message_color = "^fg(" + params["message_color"] + ")"
    out = name_color + name + ": " + \
                message_color + message[0:30] + \
                ['', '...'][len(message) > 30] + ["","^fg()"][dzen_format]
    return out

def write_out(text, path=None):
    if path:
        d = os.path.dirname(path)
        if not os.path.exists(d):
            os.makedirs(d)
        x = open(path, "w")
        x.write(text)
        print text
        x.close()
    else:
        print text

def make_message_handler(params):
    f = lambda session, stanza: stanza.getBody() != None and write_out(format_out(stanza.getFrom().getStripped(), stanza.getBody(), params), dump_path)
    return f

def main():
    config_params = get_params()
    client = setup(config_params)
    if "dzen" in config_params["format"]:
        write_out("^fg(red)Connected^fg() -- ^fg(white)no new messages ~^fg()", dump_path)
    else:
        write_out("Connected -- no new messages ~", dump_path)
    while client.Process(1):
        pass

if __name__ == '__main__':
    main()


