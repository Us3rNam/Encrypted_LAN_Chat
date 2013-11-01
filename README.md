Encrypted_LAN_Chat
==================

A LAN Chat that uses a form of one-time-pad encryption, or repetitive caesar cipher with differing shifts.  The encryption is secure enough for most uses and is quick, atleast for me.  RSA encryption would be the best for this, but that would make things very messy.  Instead I used symmetric encryption.  Every person who wants to communicate must have the same key because of this.

IRC Like Chat features several commands with more to be added.
Commands:
/nick   Changes nick name
/clear  Clears screen
/help   Shows help
/online Shows who is online at the moment

The Server can broadcast messages to anybody connected to it.
The Server must be open for others to connect.  Closing the server will cause all clients to close when they press ENTER (This is a bug I am fixing).
