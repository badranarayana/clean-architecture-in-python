# clean-architecture-in-python
One of the best approach to build software systems

![Drag Racing](https://habrastorage.org/web/fe8/c82/a32/fe8c82a32b1548b1a297187e24ae755a.png)

# Entities:
These are the enterprise business objects of your application. These should not be affected by any change external to them, and these should be the most stable code within your application.

# Use Cases:
Implement and encapsulate all of the business rules.

# Interface Adapters:
Convert and present data to the use case and entity layers.

# Frameworks and Drivers: 
Contain any frameworks or tools you need to run your application.

# The key concepts here are:
Any layer can only reference a layer below it and know nothing about what’s going on above.
The use cases and entities are the heart of your application and should have a minimal set of external library dependencies.
