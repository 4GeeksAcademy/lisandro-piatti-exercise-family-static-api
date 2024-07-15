
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        new_member={
            "id": None,
            "last_name":self.last_name,
            "first_name":member["first_name"],
            "age":member["age"],
            "lucky_numbers":member["lucky_numbers"]
        }

        if "id" in member:
            new_member["id"] = member["id"]
        else: 
            new_member["id"] = self._generateId()

        self._members.append(new_member)
        return (new_member)
        
    def delete_member(self, id):
        for family_member in  self._members:
            if family_member["id"] == id:
                self._members.remove(family_member)
                return {"done": True}
        
        return {"done": False}
    
    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                memberToReturn = {
                    "first_name": member["first_name"],
                    "id": member["id"],
                    "age": member["age"],
                    "lucky_numbers": member["lucky_numbers"]
                }
                return memberToReturn
        return None  # Return None if the member is not found

    # def get_member(self, id):
    #     for member in self._members:
    #         if member["id"] == id:
    #             name = member["first_name"]
    #             age = member["age"]
    #             lucky_numbers = member["lucky_numbers"]
    #             memberToReturn = {
    #                 self._member[ name, age, id, lucky_numbers ]
    #                 # "name" : member["first_name"],
    #                 # "id" : member["id"],
    #                 # "age" : member["age"],
    #                 # "lucky_numbers" : member["lucky_numbers"]
                    
    #             }
    #             return memberToReturn
    #     return None


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
