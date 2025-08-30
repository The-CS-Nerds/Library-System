# Overview:

[Library System](github.com/The-CS-Nerds/Library-System) has been written to be used with docker. This documentation only covers dockerised installation[^1].

## Containers:

[Library System](github.com/The-CS-Nerds/Library-System) consists of 4 containers:

### DB:

This is a PostgreSQL container that contains user, book and loan data. We[^2] intend to make a porting system to take the current spreadsheet of data and transport it to this container.[^3]

### Backend:

This container is based on linuix alpine and runs a flask based API to authorise (using Casbin) users to read/write certain database infomation based on their role.

### Frontend:

This container is based on linuix alpine and hosts a vue based webapp to create a final user interface for the system.

### Logto:

Currently not fully implemented. This container is a Logto container that provides SSO, login and authentication for users of the system.

[^1] Or at least until we[^2] can be bothered to rewrite this documentation.

[^2] In this documentation, the terms "we" and "us" refer to [The CS Nerds](github.com/the-cs-nerds) and "you" and "the user" to refer to the reader of this documentation, installers, administrators and users of [Library System](github.com/the-cs-nerds/library-system).

[^3] We[^2] might only use this data storage system for loan and book data if feedback suggests that keeping user data would be unsafe.