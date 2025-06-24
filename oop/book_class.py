
class Book:
    """A class representing a book with a title, author, and publication year."""

    def __init__(self, title, author, year):
        """Initialize the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a developer-friendly string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
