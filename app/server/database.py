import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

# MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.appdb

student_collection = database.get_collection("students")


# helpers


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student.get("name"),
        "email": student.get("email"),
        "course_of_study": student.get("course_of_study"),
        "grade": student.get("grade"),
        "year": student.get("year"),
        "GPA": student.get("gpa"),
        "address": address_helper(student.get("address")) if student.get("address") is not None else None,
    }

def address_helper(address) -> dict:
    return {
        "streetAddress": address.get("streetAddress"),
        "city": address.get("city"),
        "zip": address.get("zip"),
        "state": address.get("state"),
    }


# Crud Actions

# Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from the database
async def delete_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(id)})
        return True
