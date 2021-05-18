from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint


class Music_Like(Base):
    __tablename__ = 'musics_like_by_user'
    __table_args__ = (UniqueConstraint('id'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    id_musique = Column(String(256), nullable=False)
    id_utilisateur = Column(String(256), nullable=False)

    def __repr__(self):
        return "<(%s par %s)>" % (self.id_utilisateur, self.id_musique)

    def to_dict(self):
        return {
            "id": self.id,
            "id_musique": self.id_musique,
            "id_utilisateur": self.id_utilisateur
        }
