from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import asc

from app.api.deps import get_db, get_current_user
from app.models.note import Note
from app.models.note_version import NoteVersion
from app.models.user import User

router = APIRouter(
    prefix="/notes",
    tags=["Versions"]
)


@router.get("/{note_id}/versions")
def list_versions(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = db.query(Note).filter(
        Note.id == note_id,
        Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    versions = (
        db.query(NoteVersion)
        .filter(NoteVersion.note_id == note_id)
        .order_by(asc(NoteVersion.version_number))
        .all()
    )

    return versions


@router.get("/{note_id}/versions/{version_number}")
def get_version(
    note_id: int,
    version_number: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    version = (
        db.query(NoteVersion)
        .join(Note)
        .filter(
            Note.id == note_id,
            Note.owner_id == current_user.id,
            NoteVersion.version_number == version_number
        )
        .first()
    )

    if not version:
        raise HTTPException(status_code=404, detail="Version not found")

    return version


@router.post("/{note_id}/versions/{version_number}/restore")
def restore_version(
    note_id: int,
    version_number: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = db.query(Note).filter(
        Note.id == note_id,
        Note.owner_id == current_user.id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    version = (
        db.query(NoteVersion)
        .filter(
            NoteVersion.note_id == note_id,
            NoteVersion.version_number == version_number
        )
        .first()
    )

    if not version:
        raise HTTPException(status_code=404, detail="Version not found")

    # restore content
    note.content = version.content
    db.commit()
    db.refresh(note)

    return {
        "message": "Note restored successfully",
        "note_id": note.id,
        "restored_version": version_number
    }
