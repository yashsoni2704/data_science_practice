
# =========================================================
# SIMPLE CHAT SYSTEM USING OOP IN PYTHON
# =========================================================

# =========================================================
# Message Class
# =========================================================
# This class is used to create message objects.
# Every message will have:
# 1. sender
# 2. message content
# 3. unique message id
# =========================================================

class Message:

    # Class variable
    # Shared by all Message objects
    # Used to generate unique message IDs
    message_counter = 1

    # Constructor
    def __init__(self, sender, content):

        # Store sender object
        self.sender = sender

        # Store actual message text
        self.content = content

        # Assign unique ID to current message
        self.id = Message.message_counter

        # Increase counter for next message
        Message.message_counter += 1

    # String representation of object
    # This runs automatically when print(object) is used
    def __str__(self):

        return f"({self.id}) {self.sender.username}: {self.content}"


# =========================================================
# User Class
# =========================================================
# This class represents a user in the chat system.
#
# Each user can:
# 1. Join a chatroom
# 2. Leave a chatroom
# 3. Send messages
# =========================================================

class User:

    # Constructor
    def __init__(self, username):

        # Store username
        self.username = username

        # Initially user is not connected to any room
        self.chatroom = None

    # =====================================================
    # Method to join a chatroom
    # =====================================================
    def join_chatroom(self, chatroom):

        # Check if user is already inside a room
        if self.chatroom:

            print(f"{self.username} is already in a chatroom.")

        else:

            # Add user into room user list
            chatroom.add_user(self)

            # Store reference of joined room
            self.chatroom = chatroom

            print(f"{self.username} joined {chatroom.name}")

    # =====================================================
    # Method to leave a chatroom
    # =====================================================
    def leave_chatroom(self):

        # Check if user is not inside any room
        if not self.chatroom:

            print(f"{self.username} is not in any chatroom.")

        else:

            # Remove user from room
            self.chatroom.remove_user(self)

            print(f"{self.username} left {self.chatroom.name}")

            # Remove room reference
            self.chatroom = None

    # =====================================================
    # Method to send message
    # =====================================================
    def send_message(self, content):

        # User cannot send message without joining room
        if not self.chatroom:

            print(f"{self.username} cannot send a message "
                  f"(not in a chatroom).")

        else:

            # Send message to chatroom
            self.chatroom.broadcast(self, content)


# =========================================================
# ChatRoom Class
# =========================================================
# This class manages:
# 1. Room name
# 2. User list
# 3. Message history
# =========================================================

class ChatRoom:

    # Constructor
    def __init__(self, name):

        # Store room name
        self.name = name

        # List to store users
        self.users = []

        # List to store messages
        self.messages = []

    # =====================================================
    # Add user into room
    # =====================================================
    def add_user(self, user):

        self.users.append(user)

    # =====================================================
    # Remove user from room
    # =====================================================
    def remove_user(self, user):

        self.users.remove(user)

    # =====================================================
    # Broadcast message to all users
    # =====================================================
    def broadcast(self, sender, content):

        # Create new message object
        message = Message(sender, content)

        # Store message in history
        self.messages.append(message)

        # Print message
        print(message)

    # =====================================================
    # Display all previous messages
    # =====================================================
    def show_chat_history(self):

        print(f"\nChat History of {self.name}:\n")

        # Loop through all messages
        for msg in self.messages:

            print(msg)

        print()


# =========================================================
# MAIN PROGRAM
# =========================================================
# This block runs only when this file is executed directly
# =========================================================

if __name__ == "__main__":

    # =====================================================
    # Create Chatroom
    # =====================================================
    room = ChatRoom("Python Lounge")

    # =====================================================
    # Create Users
    # =====================================================
    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    # =====================================================
    # Users Join Chatroom
    # =====================================================
    u1.join_chatroom(room)
    u2.join_chatroom(room)

    # =====================================================
    # Users Send Messages
    # =====================================================
    u1.send_message("Hello everyone!")

    u2.send_message("Hi Alice!")

    # =====================================================
    # Another user joins
    # =====================================================
    u3.join_chatroom(room)

    # =====================================================
    # Send more messages
    # =====================================================
    u3.send_message("Hey guys, what's up?")

    # =====================================================
    # Show Full Chat History
    # =====================================================
    room.show_chat_history()

    # =====================================================
    # Users Leave Chatroom
    # =====================================================
    u1.leave_chatroom()

    u2.leave_chatroom()

    u3.leave_chatroom()