class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string

        self.title = title
        self.contents = contents
        
    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"

        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry

        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.

        length = self.count_words()

        if wpm <= 0:
            raise Exception("Cannot have reading speed <= 0")

        return int(length / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.

        time = self.reading_time(wpm)
        fraction = minutes / time

        if fraction >= 1.0:
            return "You can read everything"

        index = round(fraction * (self.count_words() - 1))

        return " ".join(self.contents.split()[:index+1])

