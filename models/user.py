from pydantic import BaseModel,Field,model_validator

class User(BaseModel):
    id:int=Field(gt=0)
    name:str=Field(description = "Full name of the user")
    email:str
    age:int=Field(gt=0,lt=120, description="Age of the user")
    is_active:bool=True #default value

# age:int |None, required
# age:int |None =None , optional, default is none

class RegisterUser(BaseModel):
    # (mode="after") example
    # First let Pydantic validate and create the model. 
    # Then run my custom validation logic on the complete model.
    # ex-password == confirm_password,start_date < end_date, age + can_drive,
    password:str
    confirm_password:str

    @model_validator(mode="after")
    def check_passwords(self):
        if self.password !=self.confirm_password:
            raise ValueError("Password do not match")

        return self

    # (mode="before") example
    # before runs on the raw input BEFORE Pydantic 
    # validates/converts it into the model.
    # ex- Rename an old field, Clean the input before validation

    #Suppose users might send a username with spaces:

    name:str
    @model_validator(mode="before")
    @classmethod
    def clean_data(cls,data):
        data["name"]=data["name"].strip()
        return data

class UserCreate(BaseModel):
    name:str
    email:str
    age:int
    is_active:bool

class UserUpdate(BaseModel):
    name: str
    email: str
    age: int
    is_active: bool

class UserPatch(BaseModel):
    name: str | None=None
    email: str | None=None
    age: int | None=None
    is_active: bool | None=None
