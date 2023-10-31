from typing import List
from multipledispatch import dispatch
import discogs_client
from applayer.artist import Artist
from datalayer.artistnotfound import ArtistNotFound
from discogs_client.exceptions import HTTPError


class DiscogsBridge(object):
    @dispatch(str, str)
    def __init__(self, key: str, secret: str):
        self.__temp_collaborators: list[dict] = []
        self.__dc: discogs_client.Client = discogs_client.Client(
            'CSC2310_Lecture/1.0',
            consumer_key=key,
            consumer_secret=secret
        )

    @dispatch()
    def __init__(self):
        self.__key = "VzCvmsMazrlfprHlhuzB"
        self.__secret: str = "IZonFBtrqyVdBBLbvLFYwXJSpViMGLcH"
        self.__temp_collaborators: list[dict] = []

        self.__dc: discogs_client.Client = discogs_client.Client(
            'CSC2310_Lecture/1.0',
            consumer_key=self.__key,
            consumer_secret=self.__secret
        )

    def get_artist_by_id(self, aid: int, year: int = 1935) -> dict:

        try:
            a = self.__dc.artist(aid)
            rel = a.releases

            for r in rel:
                if hasattr(r, "year"):
                    if r.year == year:
                        for t in r.tracklist:
                            eachartist = t.fetch("extraartists")
                            if eachartist != None:
                                self.__temp_collaborators.append({"collaboratorID": eachartist.id, "collaboratorName": eachartist.name, "releaseID": r.id, "roles": eachartist.role})

            result = {"artistID": aid, "artistName": a.name, "realname": a.real_name, "profile": a.profile, "collaborators": self.__temp_collaborators, "level": 0}

            return result
        except:
            raise(ArtistNotFound("The artist with the given id is NOT found", aid))

        """
        Get a dictionary of information about an artist from Discogs
        :param aid: artist id
        :param year: optional year
        :return: dictionary with artist info
        :raises: ArtistNotFound if the artist is not found in Discogs
        """

    def get_artists_from_list(self, a_list: list[int], year: int = 1935) -> list[dict]:
        """
        Get all the artists from Discogs based on the input list of int ids
        :param a_list: list of integer ids
        :param year: year filter
        """
        result: List[dict] = []
        for i in a_list:
            a = self.get_artist_by_id(i, year)
            if a is not None:
                result.append(a)
        if not result:
            raise ArtistNotFound("No artists found", 404)
        else:
            return result
