class song:
    """Class to represent song
    Atributes:
    title (str): The title of the song
    aartist (Artist)
    duration (int)
    """

    def __init__(self, title, artist, duration =0):
        """
        :param title: Initialises rthe title attribute
        :param artist: song artist
        :param duration: duration of the song (optional) default = 0
        """

        self.title = title
        self.artist = artist
        self.duration = duration

