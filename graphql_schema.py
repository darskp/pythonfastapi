import strawberry

@strawberry.type
class User:
    username:str
    age:int

# equivalent to
# type User{
#     username:String!
#     age:Int!
# }


@strawberry.type
class Query:
    @strawberry.field
    def users(self)->list[User]:
        return [
            User(username="darshan", age=23),
            User(username="darshan1", age=25),
        ]


# equivalent to
# type Query {
#    users:[User!]!
# }

@strawberry.type
class Mutation:
    @strawberry.mutation
    def createUser(self, username:str,age:int) -> User:
        return User(
            username=username,
            age=age
        )

schema = strawberry.Schema(query = Query, mutation=Mutation)