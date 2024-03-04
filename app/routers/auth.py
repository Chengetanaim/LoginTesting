from fastapi import APIRouter, HTTPException, status, Depends
from .. import schemas, database, models, utils, oauth2
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta


router = APIRouter()


@router.post("/login", response_model=schemas.Token)
def login(
    user_details: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = (
        db.query(models.User).filter(models.User.email == user_details.username).first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials"
        )
    if not utils.verify(user_details.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials"
        )
    # expires_at = datetime.utcnow() + timedelta(60)

    access_token, to_encode = oauth2.create_access_token({"user_id": user.id})
    print(datetime.fromtimestamp(to_encode["exp"]))
    new_session = models.Session(
        expires_at=datetime.fromtimestamp(to_encode["exp"]), user_id=user.id
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return {"access_token": access_token, "token_type": "bearer", "user": user}
