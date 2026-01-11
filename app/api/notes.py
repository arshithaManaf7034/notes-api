from app.models.note_version import NoteVersion
from sqlalchemy import func
from sqlalchemy.sql import func

from typing import List
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session

from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate, NoteOut
from app.api.deps import get_db, get_current_user
from app.models.user import User

router = APIRouter(tags=["Notes"])

@router.post("/", response_model=NoteOut)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_note = Note(
        title=note.title,
        content=note.content,
        owner_id=current_user.id
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.get("/", response_model=List[NoteOut])
def list_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Note).filter(Note.owner_id == current_user.id).all()

@router.get("/{note_id}", response_model=NoteOut)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    note = db.query(Note).filter(
        Note.id == note_id,
        Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return note

@router.put("/{note_id}", response_model=NoteOut)
def update_note(
    note_id: int,
    note: NoteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_note = (
        db.query(Note)
        .filter(Note.id == note_id, Note.owner_id == current_user.id)
        .first()
    )
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")

    #  Find latest version number
    latest_version = (
        db.query(func.max(NoteVersion.version_number))
        .filter(NoteVersion.note_id == db_note.id)
        .scalar()
    )

    next_version = (latest_version or 0) + 1

    #  Save current content as a version BEFORE update
    version = NoteVersion(
        note_id=db_note.id,
        version_number=next_version,
        content=db_note.content,
        edited_by=current_user.id,
    )
    db.add(version)

    #  Apply updates
    if note.title is not None:
        db_note.title = note.title
    if note.content is not None:
        db_note.content = note.content

    db.commit()
    db.refresh(db_note)
    return db_note


@router.delete("/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    note = db.query(Note).filter(
        Note.id == note_id,
        Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()
    return {"detail": "Note deleted"}
