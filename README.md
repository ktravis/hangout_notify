hangout_notify
==============

A python listener to catch the latest XMPP (i.e. Google Hangouts) message and store it.

Usage:

  python hangout_notify.py
  
Requires a `.hangout_notify_rc` file in the user's home directory with at least `jid` and `password` parameters.
Available configuration points include 


| parameter     | value         |
| ------------- |:-------------:| 
| jid      | email address without domain | 
| password      | your password (plaintext, sorry)      | 
| format | dzen or *      | 
| contact email | alias      | 
| name_color | basic color      | 
| message_color | basic color      | 



Dzen format will output messages using `^fg()` tags, based on the specified colors (white, red, etc.), for use in dzen2.

Parameters that match email addresses of the message-sender will be truncated to the given alias -- _I really don't need to see '@gmail.com' all over the place._


----------------
##get_time_since

Used to get a lazy estimate of the time since a file was last modified.

Usage:

  get_time_since [(-f | --format) "format string including %s"] /path/to/file
  
So a call of `get_time_since -f "~ %s ~" README.md` on a file README.md that was edited 75 minutes ago would output `~ about an hour ago ~`
