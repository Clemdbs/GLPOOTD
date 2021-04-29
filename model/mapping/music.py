from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint, Integer


class Music(Base):
    __tablename__ = 'musics'
    __table_args__ = (UniqueConstraint('id'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    titre = Column(String(256), nullable=False)
    artiste = Column(String(256), nullable=False)
    album = Column(String(256), nullable=False)
    type = Column(String(256), nullable=False)
    chemin_musique = Column(String(256), nullable=False)
    chemin_cover_image = Column(String(256), nullable=False)
    stream = Column(Integer, nullable=False)

    def __repr__(self):
        return "<(%s par %s)>" % (self.titre, self.artiste)

    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "artiste": self.artiste,
            "album": self.album,
            "type": self.type,
            "chemin_musique": self.chemin_musique,
            "chemin_cover_image": self.chemin_cover_image,
            "stream": self.stream
        }
