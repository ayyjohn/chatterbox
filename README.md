todo: write a chatserver

* overview:
The goal of this program is to create a web-application capable of having multiple users message each other, similar to IRC. Users should be able to, in real time, enter text into an input box and hit enter, causing that message to be broadcast to any other members online, allowing them to view it immediately if they are also on the same page.

* context:
As a wise man once told me "if you want to learn a language well, write a chat server in it." The purpose of this project is to gain proficiency in production quality Python, and increase my skills in it beyond toy problem applications. Writing a chat server provides an easy way to have to deal with all the nitty-gritty parts of a language, both on the front and back ends, including the need to deal with concurrency, user management, text formatting, user input sanitization, RTS, and more.

* goals
MVP
* a user should be able to enter text into an input box and hit send, posting that message to all other users
* a user should be able to view messages posted while in the application
* two or more users should be able to navigate to the page at the same time and post messages for others to view
* the application should have basic styling, if no more than a terminal based IRC implementation

potential further features
* users should be able to have persistent accounts with usernames and passwords which they can log in with to distinguish themselves
* users should be able to read messages from before they arrived, up to a certain time limit
** users should be able to configure how long they would like to see scrollback for
* users should be able to select one of any number of "rooms" where they can post messages that will only be available in that "room"
** users should be able to make rooms private and require that other users enter a password (or be invited) to enter a room
* users should be able to send messages to only one specific person without it being visible to anyone else

implementation plans
* use python/django for the backend
* write the frontend using ReactJS and ant.design
* webRTC or something similar to enable realtime communication
