SpaceHack
=========

"Decrease polarity knot to 7!  Set multitronic filter to magenta alert!  Plug in the centrifugal F-screen!"

SpaceHack is an exciting yet light-hearted starship emergency simulator, a hands-on visitor-participation game set aboard the perpetually disaster-prone USS Guppy on its voyage around the universe.  Newly recruited Star Corps cadets must operate their command consoles to flip switches, turn dials, push buttons and more according to a sequence of instructions relayed to them by their fellow crew memebers, or face destruction.  How long can you keep the ship safe?

[![SpaceHack at Maker Faire UK](http://img.youtube.com/vi/oCWH3n4aLJI/0.jpg)](http://www.youtube.com/watch?v=oCWH3n4aLJI)

Client side code
================

"Client" is the game client, which runs on Beaglebone Black and handles communications with physical hardware, and game communications with the server over MQTT.  It is essentially a configurable fairly dumb client which reads its configuration from file, and uses it to set up and poll controls, register its capabilities with the server, display text on its seven LCD displays when sent from the server, and report control state values to the server.  The client software understands the mapping between its hardware control implementations and the server's abstracted control types, but doesn't otherwise have and game logic at all or visibility of any other conencted clients.


Distributing to the consoles
============================

This is stored on the master as pi@server:SpacehackClient.git.  Push it to there and then pull from all of the clients.

The current version is checked out to /opt/SpacehackClient.
