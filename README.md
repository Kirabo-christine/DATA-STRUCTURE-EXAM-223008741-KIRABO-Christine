Explanations of the assigned tasks
1. Define struct Date { int day, month, year; }; and allocate Date reservedDates dynamically for each Room.*
•	I created a simple Date structure with three integer fields: day, month, and year.
•	Each Room object maintains a dynamic array of Date objects called reservedDates to keep track of all booked dates.
•	Dynamic allocation (new and delete[]) is used so that the array can grow as bookings increase (instead of a fixed size).
•	We also keep track of how many dates are booked (reservedCount) and the current capacity (reservedCapacity) of the array.
2. Create an abstract class Room with virtual bool isReserved(const Date) = 0; and virtual void book(const Date) = 0;, then derive StandardRoom : Room and PresidentialSuite : Room to demonstrate inheritance and polymorphism.**
•	Room is an abstract base class because it declares pure virtual functions:
o	isReserved(const Date*) — checks if a given date is already booked for that room.
o	book(const Date*) — books the room on the given date.
•	This class cannot be instantiated directly but sets a common interface for all room types.
•	Two classes inherit from Room:
o	StandardRoom
o	PresidentialSuite
•	Both override the virtual functions to provide their specific booking logic.
•	This design demonstrates inheritance (subclasses extend a base class) and polymorphism (calls to isReserved or book on a Room* will execute the derived class’s version at runtime).
3. Store Room in a dynamic Room*** rooms; calling rooms[i]->isReserved(date) and rooms[i]->book(date) dispatches correctly.
•	The hotel manages all rooms via a dynamic array of pointers: Room** rooms.
•	Each element rooms[i] points to a Room object (StandardRoom or PresidentialSuite).
•	Using this array, I can loop through rooms and call virtual methods on them.
•	Because of polymorphism, when I  call rooms[i]->isReserved(date) or rooms[i]->book(date), the correct derived class method runs depending on the actual room type.
•	This enables flexible handling of multiple room types using a uniform interface.
4. Use pointer arithmetic on reservedDates to detect conflicts and append new reservations.
•	The dynamic array reservedDates is a raw pointer to Date.
•	To check if a date is already booked, I used  pointer arithmetic like *(reservedDates + i) to access each booked date.
•	When booking a new date:
o	If the array is full (reservedCount == reservedCapacity), I  will resize it (allocate a bigger array, copy old dates).
o	Then I will append the new booking at the position reservedDates + reservedCount.
•	Pointer arithmetic here demonstrates low-level memory manipulation and dynamic array management, instead of using higher-level containers like std::vector.
5. Implement addRoom(Room) and removeRoom(int roomId) by resizing Room***.
•	addRoom(Room*) adds a new room to the Room** rooms array:
o	Since the array size is dynamic, to add a room, I will resize the array (allocate a new bigger array, copy old pointers, add new room pointer).
•	removeRoom(int roomId) removes a room by:
o	Finding the room with matching roomId,
o	Deleting that room object,
o	Shifting the rest of the pointers left to fill the gap,
o	Resizing the array to be smaller.
•	This demonstrates manual dynamic memory management and resizing of an array of pointers, simulating a dynamic list without using built-in container classes
How the Hotel Reservation Manager was completed 
Step 1: Designing the Date struct
•	Created a simple Date struct with int day, month, year.
•	Added operator== so that dates can be easily compared to check if a booking date conflicts.
Step 2: Building the abstract base class Room
•	Defined Room with:
o	Member variables:
	roomId — uniquely identifies the room.
	Date* reservedDates — a pointer to a dynamic array of booked dates.
	reservedCount and reservedCapacity — to track how many bookings exist and the capacity of the array.
o	Constructor and destructor to initialize and clean up memory.
o	Pure virtual functions isReserved(const Date*) and book(const Date*), making it abstract.
o	Helper function resizeDatesArray() to grow the bookings array when full.
Step 3: Implementing derived classes: StandardRoom and PresidentialSuite
•	Both classes inherit from Room.
•	Override isReserved:
o	Loop through reservedDates using pointer arithmetic (*(reservedDates + i)).
o	Compare each booked date with the date passed in.
•	Override book:
o	Call isReserved to check if date is free.
o	If not booked, check if the array needs resizing.
o	Append the new date at reservedDates + reservedCount.
o	Increment reservedCount.
Step 4: Managing multiple rooms with Room** rooms in HotelReservationManager
•	The manager class stores rooms in a dynamic array of pointers: Room** rooms.
•	Tracks number of rooms (roomCount).
•	Provides:
o	addRoom(Room*):
	Resizes the rooms array bigger by allocating new array, copying existing pointers, adding new room.
o	removeRoom(int roomId):
	Finds room by ID, deletes it, shifts remaining pointers left, then resizes array smaller.
•	Methods bookRoom and checkAvailability find the correct room by ID, then call the room’s virtual methods polymorphically.
•	Method listRooms prints all rooms currently in the system.
Step 5: Interactive user interface
•	The main() function runs a loop with a simple text menu:
o	Options to add room, remove room, book a room, check availability, list rooms, or exit.
•	After each user input, the program:
o	Prompts for necessary details step-by-step (room type, room ID, date).
o	Executes the operation.
o	Prints confirmation or error messages.
•	This helps test and demonstrate the system easily and clearly, fulfilling the “step by step” input/output requirement.
Step 6: Memory management
•	All dynamic allocations (new) have matching delete or delete[] to avoid leaks:
o	Each Room deletes its reservedDates array on destruction.
o	HotelReservationManager deletes all rooms and the rooms array on destruction.
•	Dynamic resizing is done carefully to maintain data and pointers safely.




