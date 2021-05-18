from model.mapping import Base, generate_id

from sqlalchemy import Column, String, UniqueConstraint


class Member(Base):
    __tablename__ = 'members'
    __table_args__ = (UniqueConstraint('email'),)

    id = Column(String(36), default=generate_id, primary_key=True)

    email = Column(String(256), nullable=False)
    pseudo = Column(String(50), nullable=False)
    mot_de_passe = Column(String(50), nullable=False)
    genre = Column(String(50), nullable=False)


    def __repr__(self):
        return "<Member(%s %s)>" % (self.email, self.pseudo)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "pseudo": self.pseudo,
            "mot_de_passe": self.mot_de_passe,
            "genre": self.genre
        }
